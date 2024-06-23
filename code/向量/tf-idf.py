import math
def compute_tf(document):
    """
    计算文档中各词语的词频（TF）。

    :param document: 文档，形式为词语列表
    :return: 词语到其TF值的映射
    """
    total_words = len(document)
    tf_dict = {}
    for word in document:
        if word in tf_dict:
            tf_dict[word] += 1
        else:
            tf_dict[word] = 1
    # 转换为频率
    for word in tf_dict:
        tf_dict[word] /= total_words
    return tf_dict


def compute_idf(documents):
    """
    计算整个文档集中各词语的逆文档频率（IDF）。

    :param documents: 文档集，每个元素为一个词语列表
    :return: 词语到其IDF值的映射
    """
    N = len(documents)  # 文档总数
    idf_dict = {}
    for document in documents:
        unique_words = set(document)
        for word in unique_words:
            if word not in idf_dict:
                idf_dict[word] = 0
            idf_dict[word] += 1
    # 计算IDF
    for word in idf_dict:
        idf_dict[word] = math.log(N / (idf_dict[word] + 1))  # 加1是为了平滑，避免除以零
    return idf_dict


def compute_tfidf(tf_vector, idf_vector):
    """
    根据给定的TF和IDF向量，计算TF-IDF向量。

    :param tf_vector: 单个文档的TF向量（词语到TF值的映射）
    :param idf_vector: 全部文档的IDF向量（词语到IDF值的映射）
    :return: 单个文档的TF-IDF向量（词语到TF-IDF值的映射）
    """
    tfidf_vector = {}
    for word, tf in tf_vector.items():
        if word in idf_vector:
            tfidf_vector[word] = tf * idf_vector[word]
    return tfidf_vector


# 示例使用
documents = [
    ['我', '喜欢', '看', '电视', '不','喜欢', '看', '电影'],
    ['我', '不', '喜欢', '看', '电视', '也','不', '喜欢', '看', '电影'],
    ['我', '喜欢', '看', '电视', '也', '喜欢', '看', '电影']
]


def compute_corpus_word_frequencies(documents):
    """
    计算整个文档集的词频统计。

    :param documents: 文档集，每个元素为一个词语列表
    :return: 词语到其在整个文档集中出现次数的映射
    """
    word_freqs = {}
    for document in documents:
        for word in document:
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
    return word_freqs


# 使用之前的示例文档集
word_frequency_table = compute_corpus_word_frequencies(documents)

# 打印词频统计表
print("Word Frequency Table:")
for word, freq in sorted(word_frequency_table.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {freq}")

# 计算每个文档的TF
doc_tfs = [compute_tf(doc) for doc in documents]

# 计算整个文档集的IDF
idf_vector = compute_idf(documents)

# 计算第一个文档的TF-IDF
first_doc_tfidf = compute_tfidf(doc_tfs[0], idf_vector)
print("TF:", doc_tfs[0])
print("TF:", doc_tfs[1])
print("TF:", doc_tfs[2])
print("IDF:", idf_vector)
print("TF-IDF:", first_doc_tfidf)
