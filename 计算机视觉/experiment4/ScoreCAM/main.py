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

# 1. 定义PyTorch CNN模型（支持特征提取）
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)
        
        # 注册钩子来获取特征图
        self.feature_maps = None
        self.conv2.register_forward_hook(self.get_feature_maps)
    
    def get_feature_maps(self, module, input, output):
        """获取最后一个卷积层的特征图"""
        self.feature_maps = output.detach()
    
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

# 2. ScoreCAM可解释性分析器
class ScoreCAMExplainer:
    def __init__(self, model, device='cpu'):
        self.model = model
        self.model.eval()
        self.device = device
        
    def normalize(self, x):
        """归一化到[0, 1]范围"""
        x_min = x.min()
        x_max = x.max()
        if x_max - x_min == 0:
            return x
        return (x - x_min) / (x_max - x_min)
    
    def explain(self, image, target_class=None, batch_size=32):
        """
        对单张图像进行ScoreCAM解释
        Args:
            image: 输入图像 (H, W) 或 (1, H, W)
            target_class: 目标类别，如果为None则使用模型预测的类别
            batch_size: 批处理大小
        """
        # 确保图像是2D的
        if len(image.shape) == 3 and image.shape[0] == 1:
            image = image[0]  # 从(1, H, W)变为(H, W)
        
        # 将图像转换为tensor并添加批次维度
        image_tensor = torch.from_numpy(image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
        
        # 获取模型预测和特征图
        with torch.no_grad():
            output = self.model(image_tensor)
            probabilities = torch.exp(output)
            
            if target_class is None:
                target_class = output.argmax(dim=1).item()
            
            baseline_prob = probabilities[0, target_class].item()
        
        # 获取特征图
        feature_maps = self.model.feature_maps
        if feature_maps is None:
            raise ValueError("未获取到特征图，请检查模型前向传播")
        
        # 获取特征图的数量和尺寸
        num_maps, h, w = feature_maps.shape[1], feature_maps.shape[2], feature_maps.shape[3]
        input_h, input_w = image.shape[0], image.shape[1]
        
        print(f"特征图数量: {num_maps}, 特征图尺寸: {h}x{w}, 输入尺寸: {input_h}x{input_w}")
        
        # 归一化每个特征图
        normalized_maps = []
        for i in range(num_maps):
            feature_map = feature_maps[0, i]  # 取第一个批次的第i个特征图
            normalized_map = self.normalize(feature_map)
            normalized_maps.append(normalized_map.cpu().numpy())
        
        # 计算每个特征图的权重（对目标类别的贡献）
        weights = []
        
        # 分批处理特征图
        for i in range(0, num_maps, batch_size):
            batch_maps = normalized_maps[i:i+batch_size]
            batch_weights = []
            
            for j, norm_map in enumerate(batch_maps):
                # 将特征图上采样到输入尺寸
                upsampled_map = torch.from_numpy(norm_map).unsqueeze(0).unsqueeze(0)
                upsampled_map = F.interpolate(upsampled_map, size=(input_h, input_w), 
                                            mode='bilinear', align_corners=False)
                upsampled_map = upsampled_map.squeeze().numpy()
                
                # 创建掩码图像：原始图像 * 上采样后的特征图
                masked_image = image * upsampled_map
                masked_tensor = torch.from_numpy(masked_image.astype(np.float32)).unsqueeze(0).unsqueeze(0).to(self.device)
                
                # 获取目标类别的概率
                with torch.no_grad():
                    masked_output = self.model(masked_tensor)
                    masked_prob = torch.exp(masked_output)[0, target_class].item()
                    batch_weights.append(masked_prob)
            
            weights.extend(batch_weights)
        
        # 计算显著性图
        saliency_map = np.zeros((input_h, input_w))
        
        for i in range(num_maps):
            # 将特征图上采样到输入尺寸
            upsampled_map = torch.from_numpy(normalized_maps[i]).unsqueeze(0).unsqueeze(0)
            upsampled_map = F.interpolate(upsampled_map, size=(input_h, input_w), 
                                        mode='bilinear', align_corners=False)
            upsampled_map = upsampled_map.squeeze().numpy()
            
            # 加权求和
            saliency_map += weights[i] * upsampled_map
        
        # 应用ReLU（移除负值）
        saliency_map = np.maximum(saliency_map, 0)
        
        # 归一化显著性图
        saliency_map = self.normalize(saliency_map)
        
        return saliency_map, target_class, baseline_prob, weights
    
    def plot_explanation(self, image, saliency_map, target_class, baseline_prob, 
                        true_label=None, alpha=0.7):
        """绘制ScoreCAM解释结果"""
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
        axes[1].set_title(f'ScoreCAM Saliency Map\nTarget Class: {target_class}')
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
        plt.savefig(f'scorecam_explanation_{true_label}_{pred_class}.png')
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
            saliency_map, target_class, baseline_prob, weights = explainer.explain(
                image, batch_size=16
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
            print(f"特征图权重范围: {min(weights):.4f} - {max(weights):.4f}")
            
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
                saliency_map, target_class, baseline_prob, _ = explainer.explain(
                    image, target_class=pred_label, batch_size=16
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
                axes[1].set_title(f'ScoreCAM for Wrong Prediction\nTarget: {target_class}')
                axes[1].axis('off')
                plt.colorbar(im, ax=axes[1])
                
                # 叠加图
                axes[2].imshow(image, cmap='gray')
                axes[2].imshow(saliency_map, cmap='jet', alpha=0.6)
                axes[2].set_title(f'Overlay\nProb: {pred_prob:.4f}')
                axes[2].axis('off')
                
                plt.tight_layout()
                plt.savefig(f'scorecam_misclassification_{idx}_{true_label}_{pred_label}.png')
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
    print("开始MNIST手写数字分类的ScoreCAM可解释性分析")
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
    
    # 创建ScoreCAM解释器
    print("5. 创建ScoreCAM解释器...")
    scorecam_explainer = ScoreCAMExplainer(model, device=device)
    
    # 选择一些测试样本进行分析
    print("6. 开始ScoreCAM可解释性分析...")
    sample_indices = [0, 1, 7, 13, 42]
    
    for idx in sample_indices:
        print(f"\n{'='*50}")
        print(f"分析样本 #{idx}")
        print(f"{'='*50}")
        
        # 获取样本
        sample_image = test_images[idx]
        true_label = test_labels[idx]
        
        try:
            # 生成ScoreCAM解释
            saliency_map, target_class, baseline_prob, weights = scorecam_explainer.explain(
                sample_image, batch_size=16
            )
            
            # 绘制结果
            pred_class, pred_prob = scorecam_explainer.plot_explanation(
                sample_image, saliency_map, target_class, baseline_prob, true_label=true_label
            )
            
            # 打印详细信息
            print(f"真实标签: {true_label}")
            print(f"预测标签: {pred_class}")
            print(f"预测概率: {pred_prob:.4f}")
            print(f"目标类别: {target_class}")
            print(f"基线概率: {baseline_prob:.4f}")
            print(f"特征图数量: {len(weights)}")
            print(f"特征图权重范围: {min(weights):.4f} - {max(weights):.4f}")
            print(f"预测正确: {true_label == pred_class}")
            print(f"结果已保存为: scorecam_explanation_{true_label}_{pred_class}.png")
            
        except Exception as e:
            print(f"分析样本 {idx} 时出错: {e}")
            continue
    
    # 批量分析
    print("\n7. 批量分析多个样本...")
    results = batch_analysis(scorecam_explainer, test_images[:10], test_labels[:10], num_samples=5)
    
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
    analyze_misclassifications(scorecam_explainer, test_images, test_labels, num_samples=3)
    
    print("\n" + "="*60)
    print("ScoreCAM可解释性分析完成!")
    print("结果图像已保存到当前目录")
    print("="*60)