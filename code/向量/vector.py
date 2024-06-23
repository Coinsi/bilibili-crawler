import numpy as np


def calculate_eigen(matrix):
    """
    计算给定矩阵的特征值和特征向量。

    参数:
    matrix: 二维numpy数组，表示要计算的矩阵。

    返回:
    eigenvalues: 特征值的一维numpy数组。
    eigenvectors: 特征向量的二维numpy数组，每一列对应一个特征向量。
    """
    # 使用numpy的linalg.eig函数计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


# 示例使用
if __name__ == "__main__":
    # 创建一个示例矩阵
    example_matrix = np.array([[0,1,0,1,0],
                               [1,0,1,1,1],
                               [0,1,0,1,0],
                               [1,1,1,0,0],
                               [0,1,0,0,0]
                               ])

    # 调用函数计算特征值和特征向量
    eigenvalues, eigenvectors = calculate_eigen(example_matrix)

    print("特征值:\n", eigenvalues)
    print("特征向量:\n", eigenvectors)
