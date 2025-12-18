"""
四分类前馈神经网络完整实现
功能: 对二维高斯数据进行四分类任务
作者: 贾柠泽
日期: 2025-10-09
"""

import os
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"  # 同步CUDA执行，便于调试（如果使用GPU）

# ==================== 导入必要的库 ====================
import pandas as pd  # 数据处理库，用于读取CSV文件
import numpy as np   # 科学计算库，用于数值运算
import torch  # 深度学习框架PyTorch
import torch.nn as nn  # 神经网络模块
import torch.optim as optim  # 优化算法模块
from torch.utils.data import DataLoader, TensorDataset  # 数据加载工具
from sklearn.model_selection import train_test_split  # 数据集划分工具
from sklearn.preprocessing import StandardScaler  # 数据标准化
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # 评估指标
import matplotlib.pyplot as plt  # 绘图库
import seaborn as sns  # 美化绘图

# ==================== 设置随机种子 ====================
# 设置随机种子可以确保每次运行代码时结果相同，便于调试和复现
torch.manual_seed(42)  # 设置PyTorch的随机种子
np.random.seed(42)     # 设置NumPy的随机种子

# ==================== 1. 数据加载和检查 ====================
print("=== 数据加载和检查 ===")
file_path = 'dataset.csv'
# 读取CSV文件，pandas会自动将数据转换为表格形式
data = pd.read_csv(file_path)
print(f"数据集形状: {data.shape}")  # 打印数据集大小（行数, 列数）
print("数据集前5行:")
print(data.head())  # 显示前5行数据，了解数据结构

# 提取特征和标签
# iloc是pandas的数据选择方法，[行选择, 列选择]
X = data.iloc[:, 0:2].values  # 选择前两列作为特征（二维高斯数据）
y = data.iloc[:, -1].values   # 选择最后一列作为标签（分类标签）

print("\n=== 标签分析 ===")
print(f"原始标签唯一值: {np.unique(y)}")  # 查看有哪些不同的标签
print(f"原始标签范围: {y.min()} 到 {y.max()}")  # 查看标签的最小值和最大值
print("原始标签分布:")
# 统计每个标签出现的次数
unique_vals, counts = np.unique(y, return_counts=True)
for val, count in zip(unique_vals, counts):
    print(f"  标签 {val}: {count} 个样本")

# ==================== 2. 标签规范化 ====================
print("\n=== 标签规范化 ===")
# 深度学习模型通常要求标签从0开始连续编号（0,1,2,3,...）
# 如果原始标签不是从0开始，需要调整以避免"越界"错误
y_normalized = y - y.min()  # 将标签平移，使最小标签变为0
num_classes = len(np.unique(y_normalized))  # 计算实际的类别数量
print(f"规范化后类别数: {num_classes}")
print(f"规范化后标签范围: {y_normalized.min()} 到 {y_normalized.max()}")
print("规范化后标签分布:")
unique_vals, counts = np.unique(y_normalized, return_counts=True)
for val, count in zip(unique_vals, counts):
    print(f"  标签 {val}: {count} 个样本")

# ==================== 3. 数据预处理 ====================
print("\n=== 数据预处理 ===")
# 数据标准化：将特征数据缩放到均值为0，标准差为1的分布
# 这有助于神经网络更快收敛，提高训练效率
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 计算并应用标准化

# ==================== 4. 划分训练集和测试集 ====================
# 将数据分为训练集（90%）和测试集（10%）
# 训练集用于训练模型，测试集用于评估模型在未知数据上的表现
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_normalized, test_size=0.1, random_state=42, stratify=y_normalized
)
# stratify参数确保训练集和测试集中各类别比例相同
print(f"训练集大小: {X_train.shape}, 测试集大小: {X_test.shape}")

# ==================== 5. 转换为PyTorch张量 ====================
# PyTorch使用张量（tensor）作为基本数据结构，类似于NumPy数组但支持GPU加速
X_train_tensor = torch.FloatTensor(X_train)  # 转换为浮点数张量
X_test_tensor = torch.FloatTensor(X_test)
y_train_tensor = torch.LongTensor(y_train)   # 标签需要长整型张量
y_test_tensor = torch.LongTensor(y_test)

# ==================== 6. 创建DataLoader用于mini-batch训练 ====================
# DataLoader可以自动将数据分成小批次（mini-batch），提高训练效率
batch_size = 32  # 每个批次包含32个样本
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)  # 组合特征和标签
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)  # 训练集打乱顺序
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)  # 测试集不需要打乱

# ==================== 7. 定义前馈神经网络 ====================
# 神经网络类，继承自nn.Module（PyTorch中所有神经网络的基类）
class FeedForwardNN(nn.Module):
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        """
        初始化神经网络结构
        参数:
            input_size: 输入特征维度（这里是2，因为数据是二维的）
            hidden_size1: 第一隐藏层神经元数量
            hidden_size2: 第二隐藏层神经元数量  
            output_size: 输出层维度（等于类别数）
        """
        super(FeedForwardNN, self).__init__()  # 调用父类初始化方法
        
        # 定义网络层结构
        self.fc1 = nn.Linear(input_size, hidden_size1)  # 第一全连接层：输入层→隐藏层1
        self.fc2 = nn.Linear(hidden_size1, hidden_size2) # 第二全连接层：隐藏层1→隐藏层2
        self.fc3 = nn.Linear(hidden_size2, output_size)  # 第三全连接层：隐藏层2→输出层
        
        # 定义激活函数和正则化方法
        self.relu = nn.ReLU()     # ReLU激活函数，引入非线性能力
        self.dropout = nn.Dropout(0.2)  # Dropout正则化，随机丢弃20%神经元防止过拟合
        
    def forward(self, x):
        """
        定义数据的前向传播过程
        参数:
            x: 输入数据
        返回:
            网络输出结果
        """
        # 第一层：全连接 → ReLU激活 → Dropout正则化
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        
        # 第二层：全连接 → ReLU激活 → Dropout正则化
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        
        # 输出层：全连接（不使用激活函数，因为CrossEntropyLoss内部会处理）
        x = self.fc3(x)
        return x

# ==================== 8. 初始化模型 ====================
input_size = 2        # 输入是二维数据
hidden_size1 = 128   # 第一隐藏层128个神经元
hidden_size2 = 64    # 第二隐藏层64个神经元
output_size = num_classes  # 输出层神经元数等于类别数（重要！）

# 创建神经网络实例
model = FeedForwardNN(input_size, hidden_size1, hidden_size2, output_size)
print(f"\n=== 模型架构 ===")
print(model)  # 打印模型结构
print(f"总参数数量: {sum(p.numel() for p in model.parameters())}")  # 计算模型参数总数
print(f"模型输出维度: {output_size} (匹配类别数)")

# ==================== 9. 定义损失函数和优化器 ====================
# 损失函数：衡量模型预测结果与真实标签的差距
criterion = nn.CrossEntropyLoss()  # 交叉熵损失函数，适用于多分类问题

# 优化器：根据损失函数的梯度更新模型参数
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
# Adam优化器结合了动量法和自适应学习率的优点
# lr=0.001: 学习率，控制参数更新步长
# weight_decay=1e-5: L2正则化强度，防止过拟合

# ==================== 10. 训练前的最终检查 ====================
print("\n=== 训练前最终检查 ===")
print(f"训练标签范围: {y_train.min()} 到 {y_train.max()}")
print(f"测试标签范围: {y_test.min()} 到 {y_test.max()}")
print(f"模型输出维度: {output_size}")

# 断言检查：确保标签值在有效范围内（0到num_classes-1）
# 如果检查失败，程序会报错并停止执行
assert y_train.min() >= 0 and y_train.max() < output_size, "训练标签越界!"
assert y_test.min() >= 0 and y_test.max() < output_size, "测试标签越界!"

# ==================== 11. 训练模型 ====================
num_epochs = 100  # 训练轮数，整个数据集被完整训练一遍称为一个epoch

# 创建列表用于记录训练过程中的损失和准确率
train_losses = []    # 训练损失记录
test_losses = []     # 测试损失记录
train_accuracies = [] # 训练准确率记录
test_accuracies = [] # 测试准确率记录

print("\n=== 开始训练 ===")
print("=" * 60)

# 开始训练循环
for epoch in range(num_epochs):
    # ========== 训练模式 ==========
    model.train()  # 设置模型为训练模式（启用Dropout等）
    epoch_train_loss = 0.0  # 当前epoch的训练损失总和
    correct_train = 0       # 当前epoch正确分类的样本数
    total_train = 0         # 当前epoch总样本数
    
    # Mini-batch训练：将训练数据分成小批次进行训练
    for batch_X, batch_y in train_loader:
        # 前向传播：输入数据通过网络得到预测结果
        outputs = model(batch_X)
        # 计算损失：比较预测结果与真实标签的差异
        loss = criterion(outputs, batch_y)
        
        # 反向传播和优化
        optimizer.zero_grad()  # 清零梯度（重要！避免梯度累积）
        loss.backward()        # 反向传播计算梯度
        optimizer.step()       # 根据梯度更新模型参数
        
        # 统计信息
        epoch_train_loss += loss.item()  # 累加损失值
        _, predicted = torch.max(outputs.data, 1)  # 获取预测类别（取概率最大的类别）
        total_train += batch_y.size(0)    # 累加样本数
        correct_train += (predicted == batch_y).sum().item()  # 累加正确分类数
    
    # 计算当前epoch的平均训练损失和准确率
    avg_train_loss = epoch_train_loss / len(train_loader)
    train_accuracy = 100 * correct_train / total_train
    train_losses.append(avg_train_loss)
    train_accuracies.append(train_accuracy)
    
    # ========== 评估模式 ==========
    model.eval()  # 设置模型为评估模式（禁用Dropout等）
    epoch_test_loss = 0.0
    correct_test = 0
    total_test = 0
    
    # torch.no_grad()表示不计算梯度，节省内存和计算资源
    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            epoch_test_loss += loss.item()
            
            _, predicted = torch.max(outputs.data, 1)
            total_test += batch_y.size(0)
            correct_test += (predicted == batch_y).sum().item()
    
    # 计算测试集平均损失和准确率
    avg_test_loss = epoch_test_loss / len(test_loader)
    test_accuracy = 100 * correct_test / total_test
    test_losses.append(avg_test_loss)
    test_accuracies.append(test_accuracy)
    
    # 每10个epoch打印一次训练进度
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}]')
        print(f'训练损失: {avg_train_loss:.4f}, 训练准确率: {train_accuracy:.2f}%')
        print(f'测试损失: {avg_test_loss:.4f}, 测试准确率: {test_accuracy:.2f}%')
        print("-" * 40)

# ==================== 12. 最终评估 ====================
print("\n=== 最终评估 ===")
model.eval()  # 确保模型在评估模式
with torch.no_grad():
    # 训练集最终评估
    train_outputs = model(X_train_tensor)
    _, train_predicted = torch.max(train_outputs.data, 1)
    final_train_accuracy = accuracy_score(y_train_tensor.numpy(), train_predicted.numpy())
    
    # 测试集最终评估
    test_outputs = model(X_test_tensor)
    _, test_predicted = torch.max(test_outputs.data, 1)
    final_test_accuracy = accuracy_score(y_test_tensor.numpy(), test_predicted.numpy())

print(f"最终训练集准确率: {final_train_accuracy * 100:.2f}%")
print(f"最终测试集准确率: {final_test_accuracy * 100:.2f}%")

# ==================== 13. 绘制训练过程图表 ====================
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体为默认字体，Windows 常用
plt.rcParams['axes.unicode_minus'] = False # 解决负号（'-'）显示为方块的问题
plt.figure(figsize=(15, 5))

# 子图1：损失曲线
plt.subplot(1, 2, 1)
plt.plot(train_losses, label='训练损失')
plt.plot(test_losses, label='测试损失')
plt.xlabel('Epoch')  # X轴：训练轮数
plt.ylabel('Loss')   # Y轴：损失值
plt.title('训练和测试损失曲线')
plt.legend()  # 显示图例
plt.grid(True, alpha=0.3)  # 显示网格

# 子图2：准确率曲线
plt.subplot(1, 2, 2)
plt.plot(train_accuracies, label='训练准确率')
plt.plot(test_accuracies, label='测试准确率')
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')  # Y轴：准确率百分比
plt.title('训练和测试准确率曲线')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()  # 自动调整子图间距
plt.savefig('training_curves.png')  # 保存图片
plt.show()  # 显示图片

# ==================== 14. 混淆矩阵 ====================
# 混淆矩阵可视化模型在各个类别上的分类性能
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test_tensor.numpy(), test_predicted.numpy())
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=[f'Class {i}' for i in range(num_classes)],
            yticklabels=[f'Class {i}' for i in range(num_classes)])
plt.title('混淆矩阵')
plt.ylabel('真实标签')  # Y轴：真实类别
plt.xlabel('预测标签')  # X轴：预测类别
plt.savefig('confusion_matrix.png')
plt.show()

# ==================== 15. 详细分类报告 ====================
print("\n=== 详细分类报告 ===")
# 打印每个类别的精确率、召回率、F1分数等详细指标
print(classification_report(y_test_tensor.numpy(), test_predicted.numpy(), 
                           target_names=[f'Class {i}' for i in range(num_classes)]))

# ==================== 16. 可视化决策边界 ====================
def plot_decision_boundary(model, X, y):
    """
    绘制决策边界：显示模型如何在特征空间中划分不同类别
    参数:
        model: 训练好的神经网络模型
        X: 特征数据
        y: 标签数据
    """
    h = 0.02  # 网格步长（越小越精细，但计算量越大）
    # 计算特征的范围（稍微扩大一点以便显示完整）
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    
    # 创建网格点坐标矩阵
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # 预测网格点的类别
    model.eval()
    with torch.no_grad():
        # 将网格点转换为模型输入格式并预测
        Z = model(torch.FloatTensor(np.c_[xx.ravel(), yy.ravel()]))
        Z = torch.argmax(Z, dim=1).numpy()  # 取概率最大的类别
    
    Z = Z.reshape(xx.shape)  # 调整形状与网格一致
    
    # 绘制决策边界和散点图
    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Spectral)  # 背景色表示决策区域
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Spectral)
    plt.colorbar(scatter)  # 显示颜色条
    plt.title('决策边界')
    plt.xlabel('Feature 1')  # 第一个特征
    plt.ylabel('Feature 2')  # 第二个特征
    plt.savefig('decision_boundary.png')
    plt.show()

# 绘制决策边界
print("\n=== 绘制决策边界 ===")
plot_decision_boundary(model, X_scaled, y_normalized)

print("\n=== 训练完成 ===")