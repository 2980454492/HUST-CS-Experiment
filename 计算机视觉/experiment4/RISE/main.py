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

# 2. RISE可解释性分析器
class RISEExplainer:
    def __init__(self, model, input_size=(28, 28), device='cpu'):
        self.model = model
        self.model.eval()
        self.input_size = input_size
        self.device = device
        
    def generate_masks(self, N=1000, s=8, p1=0.5):
        """生成随机二元掩码"""
        cell_size = np.ceil(np.array(self.input_size) / s)
        up_size = (s + 1) * cell_size
        
        # 生成随机掩码
        grid = np.random.rand(N, s, s) < p1
        grid = grid.astype('float32')
        
        masks = np.empty((N, *self.input_size))
        
        for i in range(N):
            # 随机偏移
            x = np.random.randint(0, cell_size[0])
            y = np.random.randint(0, cell_size[1])
            
            # 线性上采样
            mask = np.repeat(np.repeat(grid[i], up_size[0], axis=0), up_size[1], axis=1)
            
            # 裁剪
            mask = mask[x:x+self.input_size[0], y:y+self.input_size[1]]
            masks[i] = mask
            
        return masks
    
    def explain(self, image, target_class=None, N=1000, s=8, p1=0.5):
        """对单张图像进行RISE解释"""
        # 确保图像是2D的
        if len(image.shape) == 3 and image.shape[0] == 1:
            image = image[0]  # 从(1, H, W)变为(H, W)
        
        # 将图像转换为tensor并添加批次维度
        image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
        
        # 获取模型预测
        with torch.no_grad():
            output = self.model(image_tensor)
            probabilities = torch.exp(output)
            
            if target_class is None:
                target_class = output.argmax(dim=1).item()
            
            baseline_prob = probabilities[0, target_class].item()
        
        # 生成掩码
        masks = self.generate_masks(N, s, p1)
        
        # 计算每个掩码的权重
        weights = []
        
        for i in range(N):
            mask = masks[i]
            # 应用掩码
            masked_image = image * mask
            masked_tensor = torch.from_numpy(masked_image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                output = self.model(masked_tensor)
                prob = torch.exp(output)[0, target_class].item()
                weights.append(prob)
        
        # 计算显著性图
        saliency_map = np.zeros(self.input_size)
        total_weight = 0
        
        for i in range(N):
            saliency_map += weights[i] * masks[i]
            total_weight += weights[i]
        
        if total_weight > 0:
            saliency_map /= total_weight
        
        return saliency_map, target_class, baseline_prob
    
    def plot_explanation(self, image, saliency_map, target_class, baseline_prob, 
                        true_label=None, alpha=0.7):
        """绘制RISE解释结果"""
        # 确保图像是2D的
        if len(image.shape) == 3 and image.shape[0] == 1:
            image = image[0]
        
        # 获取模型预测
        image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
        with torch.no_grad():
            output = self.model(image_tensor)
            probabilities = torch.exp(output)
            pred_class = output.argmax(dim=1).item()
            pred_prob = probabilities[0, pred_class].item()
        
        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        
        # 原始图像
        axes[0].imshow(image, cmap='gray')
        true_title = f'True: {true_label}' if true_label is not None else ''
        axes[0].set_title(f'Original Image\n{true_title}')
        axes[0].axis('off')
        
        # 显著性图
        im = axes[1].imshow(saliency_map, cmap='jet')
        axes[1].set_title(f'RISE Saliency Map\nTarget Class: {target_class}')
        axes[1].axis('off')
        plt.colorbar(im, ax=axes[1])
        
        # 叠加图
        axes[2].imshow(image, cmap='gray')
        axes[2].imshow(saliency_map, cmap='jet', alpha=alpha)
        axes[2].set_title(f'Overlay\nPred: {pred_class} ({pred_prob:.3f})')
        axes[2].axis('off')
        
        # 二值化显著性图
        threshold = np.percentile(saliency_map, 80)  # 取前20%最重要的区域
        binary_saliency = saliency_map > threshold
        axes[3].imshow(image, cmap='gray')
        axes[3].imshow(binary_saliency, cmap='Reds', alpha=0.5)
        axes[3].set_title(f'Important Regions\nBaseline Prob: {baseline_prob:.3f}')
        axes[3].axis('off')
        
        plt.tight_layout()
        plt.savefig(f'rise_explanation_{true_label}_{pred_class}.png')
        plt.close()
        
        return pred_class, pred_prob

# 3. 批量分析函数
def batch_analysis(explainer, test_images, test_labels, num_samples=5):
    """批量分析多个样本"""
    results = []
    
    for i in range(min(num_samples, len(test_images))):
        print(f"\n分析样本 {i+1}/{num_samples}")
        
        image = test_images[i]
        true_label = test_labels[i]
        
        try:
            print(f"样本 {i} 形状: {image.shape}")
            saliency_map, target_class, baseline_prob = explainer.explain(
                image, N=500  # 减少样本数以加快速度
            )
            
            pred_class, pred_prob = explainer.plot_explanation(
                image, saliency_map, target_class, baseline_prob, true_label=true_label
            )
            
            results.append({
                'sample_id': i,
                'true_label': true_label,
                'pred_label': pred_class,
                'pred_prob': pred_prob,
                'target_class': target_class,
                'baseline_prob': baseline_prob,
                'correct': true_label == pred_class
            })
            
            print(f"真实标签: {true_label}, 预测标签: {pred_class}, 正确: {true_label == pred_class}")
            print(f"目标类别: {target_class}, 基线概率: {baseline_prob:.4f}")
            
        except Exception as e:
            print(f"样本 {i} 分析失败: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    return results

# 4. 错误分类分析函数
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
                saliency_map, target_class, baseline_prob = explainer.explain(
                    image, target_class=pred_label, N=400
                )
                
                # 绘制结果
                image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(device)
                with torch.no_grad():
                    output = explainer.model(image_tensor)
                    probabilities = torch.exp(output)
                    actual_pred_class = output.argmax(dim=1).item()
                    actual_pred_prob = probabilities[0, actual_pred_class].item()
                
                # 创建可视化
                fig, axes = plt.subplots(1, 3, figsize=(15, 5))
                
                # 原始图像
                axes[0].imshow(image, cmap='gray')
                axes[0].set_title(f'Original Image\nTrue: {true_label}, Pred: {pred_label}')
                axes[0].axis('off')
                
                # 显著性图
                im = axes[1].imshow(saliency_map, cmap='jet')
                axes[1].set_title(f'RISE for Wrong Prediction\nTarget: {target_class}')
                axes[1].axis('off')
                plt.colorbar(im, ax=axes[1])
                
                # 叠加图
                axes[2].imshow(image, cmap='gray')
                axes[2].imshow(saliency_map, cmap='jet', alpha=0.6)
                axes[2].set_title(f'Overlay\nProb: {pred_prob:.4f}')
                axes[2].axis('off')
                
                plt.tight_layout()
                plt.savefig(f'misclassification_{idx}_{true_label}_{pred_label}.png')
                plt.close()
                
                print(f"真实标签: {true_label}")
                print(f"预测标签: {pred_label}")
                print(f"预测概率: {pred_prob:.4f}")
                print(f"实际预测: {actual_pred_class} ({actual_pred_prob:.4f})")
                print(f"解释目标类别: {target_class}")
                
            except Exception as e:
                print(f"分析错误样本时出错: {e}")
                continue

# 主程序
if __name__ == "__main__":
    print("开始MNIST手写数字分类的RISE可解释性分析")
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
    
    # 创建RISE解释器
    print("5. 创建RISE解释器...")
    rise_explainer = RISEExplainer(model, input_size=(28, 28), device=device)
    
    # 选择一些测试样本进行分析
    print("6. 开始RISE可解释性分析...")
    sample_indices = [0, 1, 7, 13, 42]
    
    for idx in sample_indices:
        print(f"\n{'='*50}")
        print(f"分析样本 #{idx}")
        print(f"{'='*50}")
        
        # 获取样本
        sample_image = test_images[idx]
        true_label = test_labels[idx]
        
        try:
            # 生成RISE解释
            saliency_map, target_class, baseline_prob = rise_explainer.explain(
                sample_image, N=800
            )
            
            # 绘制结果
            pred_class, pred_prob = rise_explainer.plot_explanation(
                sample_image, saliency_map, target_class, baseline_prob, true_label=true_label
            )
            
            # 打印详细信息
            print(f"真实标签: {true_label}")
            print(f"预测标签: {pred_class}")
            print(f"预测概率: {pred_prob:.4f}")
            print(f"目标类别: {target_class}")
            print(f"基线概率: {baseline_prob:.4f}")
            print(f"预测正确: {true_label == pred_class}")
            print(f"结果已保存为: rise_explanation_{true_label}_{pred_class}.png")
            
        except Exception as e:
            print(f"分析样本 {idx} 时出错: {e}")
            continue
    
    # 批量分析
    print("\n7. 批量分析多个样本...")
    results = batch_analysis(rise_explainer, test_images[:10], test_labels[:10], num_samples=5)
    
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
    analyze_misclassifications(rise_explainer, test_images, test_labels, num_samples=3)
    
    print("\n" + "="*60)
    print("RISE可解释性分析完成!")
    print("结果图像已保存到当前目录")
    print("="*60)