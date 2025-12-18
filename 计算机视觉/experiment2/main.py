import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import numpy as np
from 手写数字识别 import load_mnist
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random

def create_image_pairs(images, labels, num_pairs=1000, same_prob=0.5):
    """
    创建图片对数据集
    Args:
        images: 图像数据
        labels: 对应标签
        num_pairs: 要生成的图片对数量
        same_prob: 正样本（相同数字）的比例
    Returns:
        pairs: 图片对张量，形状为 [num_pairs, 2, 28, 28]
        targets: 标签张量，1表示相同数字，0表示不同数字
    """
    n = len(images)
    pairs = []
    targets = []
    
    for _ in range(num_pairs):
        # 随机决定生成相同数字对还是不同数字对
        if random.random() < same_prob:
            # 相同数字：随机选择一个数字，然后找两个该数字的图片
            digit = random.randint(0, 9)
            indices = np.where(labels == digit)[0]
            if len(indices) >= 2:
                idx1, idx2 = np.random.choice(indices, 2, replace=False)
                pairs.append([images[idx1], images[idx2]])
                targets.append(1)
        else:
            # 不同数字：随机选择两个不同的数字
            digit1, digit2 = random.sample(range(10), 2)
            indices1 = np.where(labels == digit1)[0]
            indices2 = np.where(labels == digit2)[0]
            if len(indices1) > 0 and len(indices2) > 0:
                idx1 = np.random.choice(indices1)
                idx2 = np.random.choice(indices2)
                pairs.append([images[idx1], images[idx2]])
                targets.append(0)
    
    return torch.stack([torch.stack(pair) for pair in pairs]), torch.tensor(targets, dtype=torch.float32)

class SiameseNetwork(nn.Module):
    """
    孪生网络：用于比较两张图片是否相同数字
    """
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        
        # 特征提取网络（两个分支共享权重）
        self.feature_extractor = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=5, padding=2),  # 28x28 -> 28x28
            nn.ReLU(),
            nn.MaxPool2d(2),  # 28x28 -> 14x14
            
            nn.Conv2d(32, 64, kernel_size=5, padding=2),  # 14x14 -> 14x14
            nn.ReLU(),
            nn.MaxPool2d(2),  # 14x14 -> 7x7
            
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU()
        )
        
        # 比较层：计算两个特征的相似度
        self.comparison = nn.Sequential(
            nn.Linear(256, 64),  # 输入是两个128维特征的拼接
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, 1),
            nn.Sigmoid()  # 输出相似度概率
        )
    
    def forward_one(self, x):
        """处理单张图片"""
        return self.feature_extractor(x)
    
    def forward(self, x1, x2):
        """处理图片对"""
        # 分别提取特征
        feature1 = self.forward_one(x1)
        feature2 = self.forward_one(x2)
        
        # 计算特征差异，拼接两个特征
        combined = torch.cat([feature1, feature2], dim=1)
        
        # 使用拼接特征进行预测
        similarity = self.comparison(combined)
        return similarity

if __name__ == '__main__':
    # 加载原始MNIST数据
    X_train, t_train, X_test, t_test = load_mnist(flatten=False)  # 保持图像结构
    
    # 随机选择10%的数据（任务要求）
    train_indices = np.random.choice(len(X_train), size=len(X_train)//10, replace=False)
    test_indices = np.random.choice(len(X_test), size=len(X_test)//10, replace=False)
    
    X_train_sub = X_train[train_indices]
    t_train_sub = t_train[train_indices]
    X_test_sub = X_test[test_indices]
    t_test_sub = t_test[test_indices]
    
    print(f"训练图片数量: {len(X_train_sub)}")
    print(f"测试图片数量: {len(X_test_sub)}")
    
    # 数据预处理：归一化并转换为Tensor
    X_train_sub = torch.tensor(X_train_sub, dtype=torch.float32)
    t_train_sub = torch.tensor(t_train_sub, dtype=torch.long)
    X_test_sub = torch.tensor(X_test_sub, dtype=torch.float32)
    t_test_sub = torch.tensor(t_test_sub, dtype=torch.long)
    
    # 添加通道维度（CNN需要）
    X_train_sub = X_train_sub.unsqueeze(1)  # [N, 1, 28, 28]
    X_test_sub = X_test_sub.unsqueeze(1)    # [N, 1, 28, 28]
    
    # 创建图片对数据集
    train_pairs, train_targets = create_image_pairs(X_train_sub, t_train_sub, num_pairs=5000)
    test_pairs, test_targets = create_image_pairs(X_test_sub, t_test_sub, num_pairs=1000)
    
    print(f"训练图片对形状: {train_pairs.shape}")
    print(f"测试图片对形状: {test_pairs.shape}")
    print(f"正样本比例: {train_targets.mean().item():.3f}")
    
    # 创建模型
    model = SiameseNetwork()
    
    # 定义损失函数和优化器
    criterion = nn.BCELoss()  # 二元交叉熵损失
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # 训练参数
    batch_size = 64
    epochs = 40
    
    train_losses = []
    test_losses = []
    train_accuracies = []
    test_accuracies = []
    
    # 训练循环
    for epoch in range(epochs):
        model.train()
        epoch_train_loss = 0
        correct_train = 0
        total_train = 0
        
        # 随机打乱训练数据
        indices = torch.randperm(len(train_pairs))
        train_pairs_shuffled = train_pairs[indices]
        train_targets_shuffled = train_targets[indices]
        
        for i in range(0, len(train_pairs), batch_size):
            # 获取当前batch
            end_idx = min(i + batch_size, len(train_pairs))
            batch_pairs = train_pairs_shuffled[i:end_idx]
            batch_targets = train_targets_shuffled[i:end_idx]
            
            # 分离图片对
            img1 = batch_pairs[:, 0]  # 第一张图片
            img2 = batch_pairs[:, 1]  # 第二张图片
            
            # 前向传播
            optimizer.zero_grad()
            outputs = model(img1, img2).squeeze()
            loss = criterion(outputs, batch_targets)
            
            # 反向传播
            loss.backward()
            optimizer.step()
            
            epoch_train_loss += loss.item()
            
            # 计算准确率
            predictions = (outputs > 0.5).float()
            correct_train += (predictions == batch_targets).sum().item()
            total_train += len(batch_targets)
        
        # 计算训练集准确率
        train_acc = correct_train / total_train
        train_losses.append(epoch_train_loss / (len(train_pairs) // batch_size))
        train_accuracies.append(train_acc)
        
        # 测试集评估
        model.eval()
        with torch.no_grad():
            test_outputs = model(test_pairs[:, 0], test_pairs[:, 1]).squeeze()
            test_loss = criterion(test_outputs, test_targets)
            test_predictions = (test_outputs > 0.5).float()
            test_acc = (test_predictions == test_targets).float().mean().item()
            
            test_losses.append(test_loss.item())
            test_accuracies.append(test_acc)
        
        print(f'迭代轮次 {epoch+1}/{epochs}, '
              f'训练集准确率: {train_acc:.4f}, 测试集准确率: {test_acc:.4f},  '
              f'训练集损失值: {train_losses[-1]:.4f}, 测试集损失值: {test_losses[-1]:.4f}')
    
    # 最终评估
    model.eval()
    with torch.no_grad():
        # 训练集最终准确率
        train_outputs = model(train_pairs[:, 0], train_pairs[:, 1]).squeeze()
        train_predictions = (train_outputs > 0.5).float()
        final_train_acc = (train_predictions == train_targets).float().mean().item()
        
        # 测试集最终准确率
        test_outputs = model(test_pairs[:, 0], test_pairs[:, 1]).squeeze()
        test_predictions = (test_outputs > 0.5).float()
        final_test_acc = (test_predictions == test_targets).float().mean().item()
    
    print(f'\n最终结果:')
    print(f'训练集准确率: {final_train_acc:.4f}')
    print(f'测试集准确率: {final_test_acc:.4f}')
    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体为默认字体，Windows常用
    plt.rcParams['axes.unicode_minus'] = False # 解决负号（'-'）显示为方块的问题
    # 绘制训练曲线
    plt.figure(figsize=(12, 10))
    
    plt.plot(range(1, epochs+1), train_losses, 'b-', label='训练损失')
    plt.plot(range(1, epochs+1), test_losses, 'r-', label='测试损失')
    plt.xlabel('迭代次数')
    plt.ylabel('损失值')
    plt.title('训练和测试损失')
    plt.legend()
    plt.grid(True)
    plt.savefig('损失图.jpg')
    plt.show()
    
    plt.plot(range(1, epochs+1), train_accuracies, 'b-', label='训练准确率')
    plt.plot(range(1, epochs+1), test_accuracies, 'r-', label='测试准确率')
    plt.xlabel('迭代次数')
    plt.ylabel('准确率')
    plt.title('训练和测试准确率')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('准确率图.jpg')
    plt.show()
    
    # 实验分析
    print(f"\n实验分析:")
    print(f"1. 数据集构成: 使用MNIST数据集的10%，生成{len(train_pairs)}个训练图片对和{len(test_pairs)}个测试图片对")
    print(f"2. 网络架构: 孪生网络，包含共享权重的特征提取器和比较层")
    print(f"3. 正负样本比例: {train_targets.mean().item():.3f} (尽量保持平衡)")
    print(f"4. 最终性能: 训练集{final_train_acc:.4f}, 测试集{final_test_acc:.4f}")