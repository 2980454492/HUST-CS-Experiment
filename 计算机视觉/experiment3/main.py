import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def load_mnist(flatten=True):
    """
    加载MNIST数据集（替代函数）
    """
    try:
        from torchvision import datasets, transforms
        transform = transforms.Compose([transforms.ToTensor()])
        train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
        test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
        
        X_train = train_dataset.data.numpy()
        t_train = train_dataset.targets.numpy()
        X_test = test_dataset.data.numpy()
        t_test = test_dataset.targets.numpy()
        
        if not flatten:
            return X_train, t_train, X_test, t_test
        else:
            return X_train.reshape(X_train.shape[0], -1), t_train, X_test.reshape(X_test.shape[0], -1), t_test
    except:
        # 备用数据生成
        print("使用备用数据生成")
        X_train = np.random.rand(6000, 28, 28).astype(np.float32)
        t_train = np.random.randint(0, 10, 6000)
        X_test = np.random.rand(1000, 28, 28).astype(np.float32)
        t_test = np.random.randint(0, 10, 1000)
        return X_train, t_train, X_test, t_test

def load_and_preprocess_data():
    """
    加载和预处理MNIST数据集
    """
    X_train, t_train, X_test, t_test = load_mnist(flatten=False)
    
    # 数据预处理
    X_train = X_train.astype(np.float32) / 255.0
    X_test = X_test.astype(np.float32) / 255.0
    
    # 添加通道维度 (N, H, W) -> (N, 1, H, W)
    X_train = np.expand_dims(X_train, axis=1)
    X_test = np.expand_dims(X_test, axis=1)
    
    return X_train, t_train, X_test, t_test

class SiameseNetwork(nn.Module):
    """
    孪生网络模型
    """
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        
        # 特征提取网络
        self.conv1 = nn.Conv2d(1, 32, kernel_size=5, padding=2)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        
        self.conv2 = nn.Conv2d(32, 64, kernel_size=5, padding=2)  # 最后一层卷积层
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2)
        
        # 全连接层
        self.fc1 = nn.Linear(64 * 7 * 7, 256)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(256, 128)
        self.relu4 = nn.ReLU()
        
        # 比较层
        self.compare_fc1 = nn.Linear(256, 64)
        self.compare_relu = nn.ReLU()
        self.compare_dropout = nn.Dropout(0.5)
        self.compare_fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward_one(self, x):
        """处理单张图片"""
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        
        x = self.conv2(x)  # 最后一层卷积层
        x = self.relu2(x)
        x = self.pool2(x)
        
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu3(x)
        x = self.fc2(x)
        x = self.relu4(x)
        return x
    
    def forward(self, x1, x2):
        """处理图片对"""
        feature1 = self.forward_one(x1)
        feature2 = self.forward_one(x2)
        
        # 拼接特征并比较
        combined = torch.cat([feature1, feature2], dim=1)
        x = self.compare_fc1(combined)
        x = self.compare_relu(x)
        x = self.compare_dropout(x)
        x = self.compare_fc2(x)
        similarity = self.sigmoid(x)
        return similarity

def create_image_pairs(images, labels, num_pairs=1000, same_prob=0.5):
    """
    创建图片对数据集
    """
    n = len(images)
    pairs = []
    targets = []
    
    images_np = images.numpy() if torch.is_tensor(images) else images
    
    for _ in range(num_pairs):
        if np.random.random() < same_prob:
            # 创建相同数字对
            digit = np.random.randint(0, 10)
            indices = np.where(labels == digit)[0]
            if len(indices) >= 2:
                idx1, idx2 = np.random.choice(indices, 2, replace=False)
                pairs.append([images_np[idx1], images_np[idx2]])
                targets.append(1)
        else:
            # 创建不同数字对
            digit1, digit2 = np.random.choice(10, 2, replace=False)
            indices1 = np.where(labels == digit1)[0]
            indices2 = np.where(labels == digit2)[0]
            if len(indices1) > 0 and len(indices2) > 0:
                idx1 = np.random.choice(indices1)
                idx2 = np.random.choice(indices2)
                pairs.append([images_np[idx1], images_np[idx2]])
                targets.append(0)
    
    # 转换为张量
    pairs_tensor = torch.tensor(np.array(pairs), dtype=torch.float32)
    targets_tensor = torch.tensor(targets, dtype=torch.float32)
    
    return pairs_tensor, targets_tensor

def get_feature_maps(model, test_images):
    """
    获取最后一层卷积层的特征图
    """
    model.eval()
    
    with torch.no_grad():
        # 只使用前向传播到第二个卷积层
        x = test_images
        x = model.conv1(x)
        x = model.relu1(x)
        x = model.pool1(x)
        x = model.conv2(x)  # 最后一层卷积层
        x = model.relu2(x)
        feature_maps = x  # [batch_size, 64, 7, 7]
    
    return feature_maps

def compute_channel_activations(model, test_pairs):
    """
    计算每个通道的平均激活值
    """
    # 获取特征图
    feature_maps = get_feature_maps(model, test_pairs[:, 0])
    
    # 计算每个通道的平均激活（在空间维度和批次维度上平均）
    channel_activations = feature_maps.mean(dim=(0, 2, 3))  # [64]
    
    return channel_activations, feature_maps

def plot_feature_maps_visualization(feature_maps, channel_activations):
    """
    绘制特征图可视化
    """
    # 计算平均特征图（在测试集上平均）
    avg_feature_maps = feature_maps.mean(dim=0)  # [64, 7, 7]
    
    # 确定网格布局
    C, H, W = avg_feature_maps.shape
    cols = 8
    rows = (C + cols - 1) // cols
    
    plt.figure(figsize=(20, 3*rows))
    
    for i in range(C):
        plt.subplot(rows, cols, i+1)
        fm = avg_feature_maps[i].cpu().numpy()
        plt.imshow(fm, cmap='viridis')
        plt.title(f'Ch{i}\nAct:{channel_activations[i]:.3f}')
        plt.axis('off')
        plt.colorbar()
    
    plt.tight_layout()
    plt.savefig('feature_maps_visualization.jpg', dpi=300, bbox_inches='tight')
    plt.show()

def apply_real_pruning(model, channel_activations, K):
    """
    真正的结构化剪枝：创建新的卷积层，只保留重要通道
    """
    # 保存原始模型参数
    original_conv2_weight = model.conv2.weight.data.clone()
    original_conv2_bias = model.conv2.bias.data.clone() if model.conv2.bias is not None else None
    
    # 对通道按激活值排序（从低到高）
    sorted_indices = torch.argsort(channel_activations)
    
    # 确定要保留的通道
    if K >= len(channel_activations):
        K = len(channel_activations) - 1  # 至少保留一个通道
    
    channels_to_keep = sorted_indices[K:]  # 保留激活值高的通道
    channels_to_prune = sorted_indices[:K]  # 剪枝激活值低的通道
    
    print(f"剪枝前通道数: {len(channel_activations)}")
    print(f"剪枝通道数: {K}, 保留通道数: {len(channels_to_keep)}")
    
    if len(channels_to_keep) == 0:
        print("警告：所有通道都被剪枝！")
        return model
    
    # 创建新的卷积层，只保留重要通道
    new_conv2 = nn.Conv2d(
        in_channels=model.conv2.in_channels,
        out_channels=len(channels_to_keep),
        kernel_size=model.conv2.kernel_size,
        stride=model.conv2.stride,
        padding=model.conv2.padding,
        bias=model.conv2.bias is not None
    )
    
    # 设置新权重（只保留重要通道）
    new_conv2.weight.data = original_conv2_weight[channels_to_keep]
    if original_conv2_bias is not None:
        new_conv2.bias.data = original_conv2_bias[channels_to_keep]
    
    # 替换模型中的卷积层
    model.conv2 = new_conv2
    
    # 需要调整后续全连接层的输入尺寸
    new_feature_dim = len(channels_to_keep) * 7 * 7
    
    # 创建新的全连接层
    new_fc1 = nn.Linear(new_feature_dim, 256)
    new_fc2 = nn.Linear(256, 128)
    
    # 重新初始化全连接层
    nn.init.xavier_uniform_(new_fc1.weight)
    nn.init.xavier_uniform_(new_fc2.weight)
    
    # 替换全连接层
    model.fc1 = new_fc1
    model.fc2 = new_fc2
    
    return model, channels_to_keep

def evaluate_model_accuracy(model, test_pairs, test_targets):
    """
    评估模型准确率
    """
    model.eval()
    with torch.no_grad():
        outputs = model(test_pairs[:, 0], test_pairs[:, 1]).squeeze()
        predictions = (outputs > 0.5).float()
        accuracy = (predictions == test_targets).float().mean().item()
    return accuracy

def train_model(model, train_pairs, train_targets, epochs=10):
    """
    训练模型
    """
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        
        # 随机打乱数据
        indices = torch.randperm(len(train_pairs))
        train_pairs_shuffled = train_pairs[indices]
        train_targets_shuffled = train_targets[indices]
        
        for i in range(0, len(train_pairs), 64):
            batch_pairs = train_pairs_shuffled[i:i+64]
            batch_targets = train_targets_shuffled[i:i+64]
            
            img1 = batch_pairs[:, 0]
            img2 = batch_pairs[:, 1]
            
            optimizer.zero_grad()
            outputs = model(img1, img2).squeeze()
            loss = criterion(outputs, batch_targets)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
            # 计算准确率
            preds = (outputs > 0.5).float()
            correct += (preds == batch_targets).sum().item()
            total += len(batch_targets)
        
        if (epoch + 1) % 5 == 0:
            accuracy = correct / total if total > 0 else 0
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {total_loss/len(train_pairs):.4f}, Acc: {accuracy:.4f}')
    
    return model

def run_pruning_experiment(model, test_pairs, test_targets):
    """
    运行剪枝实验
    """
    print("开始剪枝实验...")
    
    # 计算通道激活
    channel_activations, feature_maps = compute_channel_activations(model, test_pairs)
    
    # 绘制特征图
    plot_feature_maps_visualization(feature_maps, channel_activations)
    
    # 总通道数
    P = len(channel_activations)
    print(f"总通道数: {P}")
    
    # 测试不同的剪枝比例
    pruning_ratios = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    K_values = [int(P * ratio) for ratio in pruning_ratios]
    
    accuracies = []
    
    # 保存原始模型状态
    original_state = model.state_dict().copy()
    
    for i, K in enumerate(K_values):
        # 恢复原始模型 - 创建一个新模型实例
        new_model = SiameseNetwork()
        new_model.load_state_dict(original_state)
        
        if K > 0:
            # 应用真正的剪枝
            pruned_model, kept_channels = apply_real_pruning(new_model, channel_activations, K)
        else:
            pruned_model = new_model
            kept_channels = torch.arange(P)
        
        # 评估剪枝后模型
        accuracy = evaluate_model_accuracy(pruned_model, test_pairs, test_targets)
        accuracies.append(accuracy)
        
        print(f"剪枝比例: {pruning_ratios[i]:.1%}, K={K}/{P}, 准确率: {accuracy:.4f}")
        
        # 如果准确率太低，提前停止
        if accuracy < 0.4 and pruning_ratios[i] > 0.3:
            print("准确率过低，停止实验")
            break
    
    return pruning_ratios[:len(accuracies)], accuracies, channel_activations

def plot_pruning_results(pruning_ratios, accuracies, channel_activations):
    """
    绘制剪枝结果
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # 图1: 准确率 vs 剪枝比例
    ax1.plot(pruning_ratios, accuracies, 'b-o', linewidth=2, markersize=6)
    ax1.set_xlabel('剪枝比例 (K/P)')
    ax1.set_ylabel('分类准确率')
    ax1.set_title('剪枝比例对准确率的影响')
    ax1.grid(True, alpha=0.3)
    
    # 标记最佳点
    if len(accuracies) > 0:
        best_idx = np.argmax(accuracies)
        ax1.plot(pruning_ratios[best_idx], accuracies[best_idx], 'ro', markersize=10, 
                label=f'最佳点: {pruning_ratios[best_idx]:.1%}, Acc={accuracies[best_idx]:.3f}')
        ax1.legend()
    
    # 图2: 通道激活分布
    ax2.hist(channel_activations.cpu().numpy(), bins=20, alpha=0.7, color='green')
    ax2.set_xlabel('通道平均激活值')
    ax2.set_ylabel('通道数量')
    ax2.set_title('通道激活值分布')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pruning_results.jpg', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 打印统计信息
    if len(accuracies) > 0:
        print(f"\n=== 剪枝实验统计 ===")
        print(f"总通道数: {len(channel_activations)}")
        print(f"通道激活范围: [{channel_activations.min():.4f}, {channel_activations.max():.4f}]")
        print(f"最佳剪枝比例: {pruning_ratios[best_idx]:.1%}, 准确率: {accuracies[best_idx]:.4f}")
        if len(accuracies) > 1:
            print(f"相对原始准确率变化: {accuracies[best_idx]-accuracies[0]:.4f}")

def main():
    """
    主函数
    """
    # 1. 加载和预处理数据
    print("加载MNIST数据集...")
    X_train, t_train, X_test, t_test = load_and_preprocess_data()
    
    # 使用数据集的10%
    train_indices = np.random.choice(len(X_train), len(X_train)//10, replace=False)
    test_indices = np.random.choice(len(X_test), len(X_test)//10, replace=False)
    
    X_train_sub = X_train[train_indices]
    t_train_sub = t_train[train_indices]
    X_test_sub = X_test[test_indices]
    t_test_sub = t_test[test_indices]
    
    # 转换为张量
    X_train_tensor = torch.tensor(X_train_sub, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test_sub, dtype=torch.float32)
    
    # 2. 创建图片对
    print("创建图片对数据集...")
    train_pairs, train_targets = create_image_pairs(X_train_tensor, t_train_sub, 5000)
    test_pairs, test_targets = create_image_pairs(X_test_tensor, t_test_sub, 1000)
    
    print(f"训练图片对数量: {len(train_pairs)}")
    print(f"测试图片对数量: {len(test_pairs)}")
    print(f"正样本比例: {train_targets.mean().item():.3f}")
    
    # 3. 创建和训练模型
    print("创建和训练孪生网络模型...")
    model = SiameseNetwork()
    
    # 训练模型
    model = train_model(model, train_pairs, train_targets, epochs=20)
    
    # 测试原始模型性能
    original_accuracy = evaluate_model_accuracy(model, test_pairs, test_targets)
    print(f"原始模型准确率: {original_accuracy:.4f}")
    
    # 4. 进行剪枝实验
    pruning_ratios, accuracies, channel_activations = run_pruning_experiment(
        model, test_pairs, test_targets
    )
    
    # 5. 绘制结果
    plot_pruning_results(pruning_ratios, accuracies, channel_activations)
    
    # 6. 绘制压缩率 vs 准确率图
    plt.figure(figsize=(10, 6))
    plt.plot(pruning_ratios, accuracies, 'b-o', linewidth=2, markersize=6)
    plt.xlabel('压缩率 (K/P)')
    plt.ylabel('分类准确率')
    plt.title('模型压缩率 vs 准确率')
    plt.grid(True, alpha=0.3)
    
    # 标记关键点
    if len(pruning_ratios) > 0:
        thresholds = [0.1, 0.3, 0.5]
        for threshold in thresholds:
            # 找到第一个大于等于阈值的点
            valid_indices = [i for i, ratio in enumerate(pruning_ratios) if ratio >= threshold]
            if valid_indices:
                idx = valid_indices[0]
                plt.plot(pruning_ratios[idx], accuracies[idx], 'ro', markersize=8)
                plt.annotate(f'{pruning_ratios[idx]:.1%}\nAcc:{accuracies[idx]:.3f}', 
                            xy=(pruning_ratios[idx], accuracies[idx]),
                            xytext=(10, 10), textcoords='offset points')
    
    plt.tight_layout()
    plt.savefig('compression_accuracy_tradeoff.jpg', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    # 设置随机种子
    torch.manual_seed(42)
    np.random.seed(42)
    
    main()