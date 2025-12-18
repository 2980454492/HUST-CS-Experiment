import os
# 解决OpenMP冲突
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
os.environ['OMP_NUM_THREADS'] = '1'

import numpy as np
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端避免GUI冲突
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import lime
from lime import lime_image
from skimage.segmentation import mark_boundaries
import warnings
warnings.filterwarnings('ignore')

# 设置随机种子
np.random.seed(42)
torch.manual_seed(42)
if torch.cuda.is_available():
    torch.cuda.manual_seed(42)

# 1. 定义PyTorch CNN模型
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# 2. PyTorch模型包装器（用于LIME）
class PyTorchModelWrapper:
    def __init__(self, model, device='cpu'):
        self.model = model
        self.model.eval()
        self.device = device
    
    def predict(self, images):
        """LIME需要的预测函数"""
        with torch.no_grad():
            # 处理不同维度的输入
            if len(images.shape) == 4:  # 批量图像 (batch_size, H, W, 3)
                # 将RGB转换为灰度图
                if images.shape[-1] == 3:
                    # 使用标准RGB到灰度的转换公式
                    images_gray = np.dot(images[..., :3], [0.2989, 0.5870, 0.1140])
                    # 重塑为 (batch_size, 1, H, W)
                    images = images_gray.reshape(images_gray.shape[0], 1, images_gray.shape[1], images_gray.shape[2])
                else:
                    # 如果不是3通道，直接添加通道维度
                    images = images.reshape(images.shape[0], 1, images.shape[1], images.shape[2])
                    
            elif len(images.shape) == 3:  # 单张图像 (H, W, 3) 或 (H, W)
                if images.shape[-1] == 3:  # (H, W, 3)
                    # 转换为灰度
                    images_gray = np.dot(images[..., :3], [0.2989, 0.5870, 0.1140])
                    # 重塑为 (1, 1, H, W)
                    images = images_gray.reshape(1, 1, images_gray.shape[0], images_gray.shape[1])
                else:  # (H, W)
                    # 添加批次和通道维度
                    images = images.reshape(1, 1, images.shape[0], images.shape[1])
            
            # 确保数据类型正确
            images_tensor = torch.from_numpy(images.astype(np.float32)).to(self.device)
            
            outputs = self.model(images_tensor)
            # 转换为概率（因为输出是log_softmax）
            return torch.exp(outputs).cpu().numpy()

# 3. LIME可解释性分析器
class LIMEExplainer:
    def __init__(self, model, device='cpu'):
        self.model = model
        self.device = device
        self.model_wrapper = PyTorchModelWrapper(model, device)
        self.explainer = lime_image.LimeImageExplainer()
        
    def explain(self, image, top_labels=5, hide_color=0, num_samples=1000):
        """
        对单张图像进行LIME解释
        Args:
            image: 输入图像 (H, W) 或 (1, H, W)
            top_labels: 解释的top类别数
            hide_color: 隐藏区域的颜色
            num_samples: 扰动样本数量
        """
        # 确保图像是2D的
        if len(image.shape) == 3 and image.shape[0] == 1:
            image = image[0]  # 从(1, H, W)变为(H, W)
        
        # LIME需要RGB图像，将灰度图转换为伪RGB
        if len(image.shape) == 2:
            image_rgb = np.stack([image, image, image], axis=2)
        else:
            image_rgb = image
        
        # 生成解释
        explanation = self.explainer.explain_instance(
            image_rgb.astype('double'),
            self.model_wrapper.predict,
            top_labels=top_labels,
            hide_color=hide_color,
            num_samples=num_samples
        )
        
        # 获取模型预测
        image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
        with torch.no_grad():
            output = self.model(image_tensor)
            probabilities = torch.exp(output)
            pred_class = output.argmax(dim=1).item()
            pred_prob = probabilities[0, pred_class].item()
        
        return explanation, pred_class, pred_prob
    
    def plot_explanation(self, image, explanation, true_label=None, 
                        positive_only=True, num_features=10, hide_rest=True):
        """绘制LIME解释结果"""
        # 确保图像是2D的
        if len(image.shape) == 3 and image.shape[0] == 1:
            image = image[0]
        
        # LIME需要RGB图像
        if len(image.shape) == 2:
            image_rgb = np.stack([image, image, image], axis=2)
        else:
            image_rgb = image
        
        # 获取模型预测
        image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
        with torch.no_grad():
            output = self.model(image_tensor)
            probabilities = torch.exp(output)
            pred_class = output.argmax(dim=1).item()
            pred_prob = probabilities[0, pred_class].item()
        
        # 获取最重要的标签
        label = explanation.top_labels[0]
        
        # 获取解释
        temp, mask = explanation.get_image_and_mask(
            label,
            positive_only=positive_only,
            num_features=num_features,
            hide_rest=hide_rest
        )
        
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        
        # 原始图像
        axes[0].imshow(image, cmap='gray')
        true_title = f'True: {true_label}' if true_label is not None else ''
        axes[0].set_title(f'Original Image\n{true_title}')
        axes[0].axis('off')
        
        # LIME解释
        axes[1].imshow(mark_boundaries(temp, mask))
        axes[1].set_title(f'LIME Explanation\nPred: {pred_class} ({pred_prob:.3f})')
        axes[1].axis('off')
        
        # 热力图
        ind = explanation.top_labels[0]
        dict_heatmap = dict(explanation.local_exp[ind])
        heatmap = np.vectorize(dict_heatmap.get)(explanation.segments)
        im = axes[2].imshow(heatmap, cmap='RdBu', vmin=-heatmap.max(), vmax=heatmap.max())
        axes[2].set_title('Feature Importance Heatmap')
        axes[2].axis('off')
        plt.colorbar(im, ax=axes[2])
        
        # 仅显示重要区域
        axes[3].imshow(image, cmap='gray')
        axes[3].imshow(mask, cmap='Reds', alpha=0.5)
        axes[3].set_title('Important Regions Only')
        axes[3].axis('off')
        
        plt.tight_layout()
        plt.savefig(f'lime_explanation_{true_label}_{pred_class}.png')
        plt.close()
        
        return pred_class, pred_prob

# 4. 批量分析函数
def batch_analysis(explainer, test_images, test_labels, num_samples=5):
    """批量分析多个样本"""
    results = []
    
    for i in range(min(num_samples, len(test_images))):
        print(f"\n分析样本 {i+1}/{num_samples}")
        
        image = test_images[i]
        true_label = test_labels[i]
        
        try:
            print(f"样本 {i} 形状: {image.shape}")
            explanation, pred_class, pred_prob = explainer.explain(
                image, num_samples=800  # 减少样本数以加快速度
            )
            
            pred_class, pred_prob = explainer.plot_explanation(
                image, explanation, true_label=true_label
            )
            
            results.append({
                'sample_id': i,
                'true_label': true_label,
                'pred_label': pred_class,
                'pred_prob': pred_prob,
                'correct': true_label == pred_class
            })
            
            print(f"真实标签: {true_label}, 预测标签: {pred_class}, 正确: {true_label == pred_class}")
            
        except Exception as e:
            print(f"样本 {i} 分析失败: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    return results

# 5. 错误分类分析函数
def analyze_misclassifications(explainer, test_images, test_labels, num_samples=3):
    """分析模型分类错误的样本"""
    # 获取所有预测
    all_predictions = []
    device = explainer.device
    
    with torch.no_grad():
        # 分批处理避免内存问题
        batch_size = 100
        for i in range(0, len(test_images), batch_size):
            batch_images = test_images[i:i+batch_size]
            batch_tensors = torch.from_numpy(batch_images.astype(np.float32)).unsqueeze(1).to(device)
            outputs = explainer.model(batch_tensors)
            # 修复：将CUDA张量移动到CPU再转换为numpy
            probs = torch.exp(outputs).cpu().numpy()
            all_predictions.extend(probs)
    
    all_predictions = np.array(all_predictions)
    pred_labels = np.argmax(all_predictions, axis=1)
    true_labels = test_labels
    
    # 找到错误分类的索引
    wrong_indices = np.where(pred_labels != true_labels)[0]
    
    print(f"发现 {len(wrong_indices)} 个错误分类样本")
    
    if len(wrong_indices) > 0:
        # 分析前几个错误样本
        for i in range(min(num_samples, len(wrong_indices))):
            idx = wrong_indices[i]
            print(f"\n分析错误样本 #{i+1} (索引: {idx})")
            
            image = test_images[idx]
            true_label = true_labels[idx]
            pred_label = pred_labels[idx]
            pred_prob = all_predictions[idx][pred_label]
            
            try:
                # 对错误预测的类别进行解释
                explanation, actual_pred_class, actual_pred_prob = explainer.explain(
                    image, num_samples=600
                )
                
                explainer.plot_explanation(
                    image, explanation, true_label=true_label,
                    positive_only=False,  # 显示正负特征
                    num_features=15
                )
                
                print(f"真实标签: {true_label}")
                print(f"预测标签: {pred_label}")
                print(f"预测概率: {pred_prob:.4f}")
                print(f"实际预测: {actual_pred_class} ({actual_pred_prob:.4f})")
                
            except Exception as e:
                print(f"分析错误样本时出错: {e}")
                continue

# 6. 详细解释报告函数
def detailed_lime_report(explainer, image, true_label):
    """生成详细的LIME解释报告"""
    explanation, pred_class, pred_prob = explainer.explain(image, num_samples=1500)
    
    print(f"\n详细LIME解释报告:")
    print(f"真实标签: {true_label}")
    print(f"预测标签: {pred_class}")
    print(f"预测概率: {pred_prob:.4f}")
    
    # 显示top-k预测
    image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(explainer.device)
    with torch.no_grad():
        output = explainer.model(image_tensor)
        probabilities = torch.exp(output).cpu().numpy()[0]
    
    top_k = 3
    top_indices = np.argsort(probabilities)[-top_k:][::-1]
    print(f"\nTop-{top_k} 预测:")
    for i, idx in enumerate(top_indices):
        print(f"{i+1}. 数字 {idx}: {probabilities[idx]:.4f}")
    
    # 分析重要特征
    print(f"\nLIME特征重要性分析:")
    for label in explanation.top_labels[:2]:
        print(f"\n对于数字 {label} 的预测:")
        features = explanation.local_exp[label]
        top_features = sorted(features, key=lambda x: abs(x[1]), reverse=True)[:5]
        
        for feature, importance in top_features:
            print(f"  超像素 {feature}: 重要性 {importance:.4f}")
    
    return explanation

# 主程序
if __name__ == "__main__":
    print("开始MNIST手写数字分类的LIME可解释性分析")
    print("=" * 60)
    
    # 设置设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")
    
    # 加载MNIST数据
    from torchvision import datasets, transforms
    
    print("1. 加载MNIST数据集...")
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    # 下载训练集和测试集
    trainset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    testset = datasets.MNIST('./data', train=False, download=True, transform=transform)
    
    train_loader = DataLoader(trainset, batch_size=64, shuffle=True)
    test_loader = DataLoader(testset, batch_size=1000, shuffle=False)
    
    # 创建模型
    print("2. 创建CNN模型...")
    model = CNN().to(device)
    optimizer = torch.optim.Adam(model.parameters())
    
    # 训练模型
    print("3. 训练模型...")
    for epoch in range(3):
        model.train()
        total_loss = 0
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        # 测试准确率
        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                test_loss += F.nll_loss(output, target, reduction='sum').item()
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()
        
        test_loss /= len(test_loader.dataset)
        accuracy = 100. * correct / len(test_loader.dataset)
        print(f'Epoch {epoch+1}: 平均训练损失: {total_loss/len(train_loader):.4f}, '
              f'测试准确率: {accuracy:.2f}%')
    
    # 准备测试数据
    print("4. 准备测试数据...")
    test_images = []
    test_labels = []
    for data, target in test_loader:
        test_images.append(data.cpu().squeeze().numpy())
        test_labels.append(target.cpu().numpy())
    
    test_images = np.concatenate(test_images)
    test_labels = np.concatenate(test_labels)
    
    print(f"测试集形状: {test_images.shape}")
    print(f"测试标签形状: {test_labels.shape}")
    
    # 创建LIME解释器
    print("5. 创建LIME解释器...")
    lime_explainer = LIMEExplainer(model, device=device)
    
    # 选择一些测试样本进行分析
    print("6. 开始LIME可解释性分析...")
    sample_indices = [0, 1, 7, 13, 42]
    
    for idx in sample_indices:
        print(f"\n{'='*50}")
        print(f"分析样本 #{idx}")
        print(f"{'='*50}")
        
        # 获取样本
        sample_image = test_images[idx]
        true_label = test_labels[idx]
        
        try:
            # 生成LIME解释
            explanation, pred_class, pred_prob = lime_explainer.explain(
                sample_image, num_samples=1000
            )
            
            # 绘制结果
            pred_class, pred_prob = lime_explainer.plot_explanation(
                sample_image, explanation, true_label=true_label
            )
            
            # 打印详细信息
            print(f"真实标签: {true_label}")
            print(f"预测标签: {pred_class}")
            print(f"预测概率: {pred_prob:.4f}")
            print(f"预测正确: {true_label == pred_class}")
            print(f"结果已保存为: lime_explanation_{true_label}_{pred_class}.png")
            
        except Exception as e:
            print(f"分析样本 {idx} 时出错: {e}")
            continue
    
    # 批量分析
    print("\n7. 批量分析多个样本...")
    results = batch_analysis(lime_explainer, test_images[:10], test_labels[:10], num_samples=5)
    
    # 统计结果
    if results:
        accuracy = sum(1 for r in results if r['correct']) / len(results)
        avg_prob = np.mean([r['pred_prob'] for r in results])
        
        print(f"\n{'='*50}")
        print("分析结果统计:")
        print(f"{'='*50}")
        print(f"样本数量: {len(results)}")
        print(f"准确率: {accuracy:.3f}")
        print(f"平均预测概率: {avg_prob:.3f}")
    
    # 错误分类分析
    print("\n8. 分析错误分类样本...")
    analyze_misclassifications(lime_explainer, test_images, test_labels, num_samples=3)
    
    # 详细解释报告
    print("\n9. 生成详细解释报告...")
    sample_idx = 13
    try:
        detailed_explanation = detailed_lime_report(
            lime_explainer, 
            test_images[sample_idx], 
            test_labels[sample_idx]
        )
    except Exception as e:
        print(f"生成详细报告时出错: {e}")
    
    print("\n" + "="*60)
    print("LIME可解释性分析完成!")
    print("结果图像已保存到当前目录")
    print("="*60)