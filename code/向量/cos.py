import math


def cosine_similarity(vector1, vector2):
    """
    计算两个向量的余弦相似度。

    参数:
    vector1, vector2: 分别为两个向量，类型为list或np.array，元素需可进行乘法和平方根运算。

    返回:
    两个向量的余弦相似度，类型为float。
    """
    # 确保两个向量长度相同
    if len(vector1) != len(vector2):
        raise ValueError("两个向量的维度必须相同")

    # 计算向量的点积
    dot_product = sum(a * b for a, b in zip(vector1, vector2))

    # 计算向量的模长（欧几里得范数）
    magnitude_v1 = math.sqrt(sum(a ** 2 for a in vector1))
    magnitude_v2 = math.sqrt(sum(b ** 2 for b in vector2))

    # 避免除以零错误
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0  # 向量为零向量时，相似度定义为0

    # 计算并返回余弦相似度
    return dot_product / (magnitude_v1 * magnitude_v2)


# 示例使用
vector_a = [5,2,4,1,3]
vector_b = [1,5,3,5,2]

similarity = cosine_similarity(vector_a, vector_b)
print(f"向量A和向量B的余弦相似度为: {similarity}")
