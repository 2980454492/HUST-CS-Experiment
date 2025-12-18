import numpy as np
import struct
import os
from PIL import Image

def read_idx3_ubyte_images(file_path):
    """
    读取 MNIST idx3-ubyte 格式的图像文件并转换为 NumPy 数组。
    
    参数:
        file_path (str): idx3-ubyte 图像文件的路径。
        
    返回:
        np.ndarray: 形状为 (num_images, rows, cols) 的 numpy 数组，数据类型为 uint8。
        
    异常:
        FileNotFoundError: 当文件不存在时抛出
        ValueError: 当文件格式不正确或数据损坏时抛出
    """
    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    with open(file_path, 'rb') as f:
        # 读取文件头信息
        magic, num_images, rows, cols = struct.unpack('>IIII', f.read(16))
        
        # 验证魔数
        if magic != 2051:
            raise ValueError(f"无效的魔数 {magic}，期望 2051 (图像文件)。")
        
        # 验证文件大小
        file_size = os.path.getsize(file_path)
        expected_size = 16 + num_images * rows * cols
        if file_size != expected_size:
            raise ValueError(f"文件大小不匹配: 期望 {expected_size} 字节，实际 {file_size} 字节")
        
        # 读取图像数据
        buffer = f.read()
        if len(buffer) != num_images * rows * cols:
            raise ValueError("读取的数据量与文件头信息不匹配")
        
        data = np.frombuffer(buffer, dtype=np.uint8)
        data = data.reshape(num_images, rows, cols)
        
    return data

def read_idx1_ubyte_labels(file_path):
    """
    读取 MNIST idx1-ubyte 格式的标签文件并转换为 NumPy 数组。
    
    参数:
        file_path (str): idx1-ubyte 标签文件的路径。
        
    返回:
        np.ndarray: 形状为 (num_labels,) 的 numpy 数组，数据类型为 uint8。
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    with open(file_path, 'rb') as f:
        magic, num_labels = struct.unpack('>II', f.read(8))
        
        if magic != 2049:
            raise ValueError(f"无效的魔数 {magic}，期望 2049 (标签文件)。")
        
        buffer = f.read()
        if len(buffer) != num_labels:
            raise ValueError("读取的标签数量与文件头信息不匹配")
        
        labels = np.frombuffer(buffer, dtype=np.uint8)
    
    return labels

def load_mnist(data_dir='./datasets/',flatten=False):
    """
    加载MNIST训练集和测试集
    
    参数:
        data_dir (str): 数据集目录路径
        flatten (bool): 是否将二维图像展平为一维向量
        
    返回:
        tuple: (X_train, y_train, X_test, y_test)
    """
    # 检查目录是否存在
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"数据集目录不存在: {data_dir}")
    
    try:
        # 加载训练集
        train_image_path = os.path.join(data_dir, 'train-images.idx3-ubyte')
        train_label_path = os.path.join(data_dir, 'train-labels.idx1-ubyte')
        X_train = read_idx3_ubyte_images(train_image_path)
        y_train = read_idx1_ubyte_labels(train_label_path)
        
        # 加载测试集
        test_image_path = os.path.join(data_dir, 't10k-images.idx3-ubyte')
        test_label_path = os.path.join(data_dir, 't10k-labels.idx1-ubyte')
        X_test = read_idx3_ubyte_images(test_image_path)
        y_test = read_idx1_ubyte_labels(test_label_path)
        
        # 验证数据一致性
        assert X_train.shape[0] == y_train.shape[0], "训练集图像和标签数量不匹配"
        assert X_test.shape[0] == y_test.shape[0], "测试集图像和标签数量不匹配"

        # 进行归一化
        X_train = X_train.astype(np.float32) / 255.0
        X_test = X_test.astype(np.float32) / 255.0

        # 是否将二维图像展平为一维向量
        if flatten == True:
            X_train = X_train.reshape((X_train.shape[0], X_train.shape[1] * X_train.shape[2]))
            X_test = X_test.reshape((X_test.shape[0], X_test.shape[1] * X_test.shape[2]))
        
        return X_train, y_train, X_test, y_test
        
    except Exception as e:
        print(f"加载MNIST数据集时出错: {e}")
        raise

def visualize_sample(X, y, index=0):
    """
    可视化单个MNIST样本
    
    参数:
        X: 图像数据
        y: 标签数据  
        index: 样本索引
    """
    import matplotlib.pyplot as plt
    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定黑体为默认字体，Windows 常用
    plt.rcParams['axes.unicode_minus'] = False # 解决负号（'-'）显示为方块的问题
    
    plt.imshow(X[index], cmap='gray')
    plt.title(f'标签: {y[index]}')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    try:
        X_train, y_train, X_test, y_test = load_mnist()
        
        print("=== MNIST数据集加载成功 ===")
        print(f"训练集: {X_train.shape[0]} 个样本, 图像形状: {X_train.shape[1:]}")
        print(f"测试集: {X_test.shape[0]} 个样本, 图像形状: {X_test.shape[1:]}")
        print(f"标签范围: {y_train.min()} - {y_train.max()} (0-9的数字)")
        print(f"像素值范围: [{X_train.min()}, {X_train.max()}]")
        
        # 显示一个样本
        print(f"\n第一个训练样本的数据: {X_train[0]}")
        print(f"\n第一个训练样本的标签: {y_train[0]}")
        visualize_sample(X_train, y_train, 0)  # 取消注释以显示图像
        
    except Exception as e:
        print(f"错误: {e}")
        print("请确保:")
        print("1. datasets/目录存在且包含MNIST数据文件")
        print("2. 数据文件未损坏且格式正确")
        print("3. 文件名为: train-images.idx3-ubyte, train-labels.idx1-ubyte, t10k-images.idx3-ubyte, t10k-labels.idx1-ubyte")