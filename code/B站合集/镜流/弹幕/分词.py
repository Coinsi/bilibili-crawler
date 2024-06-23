import jieba

# 读取弹幕文件
with open('弹幕.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用Jieba进行分词
seg_list = jieba.cut(content, cut_all=False)
seg_result = ' '.join(seg_list)

# 将分词结果写入文件
with open('弹幕分词结果.txt', 'w', encoding='utf-8') as file:
    file.write(seg_result)

print("分词完成，结果已保存到 '弹幕分词结果.txt'")
