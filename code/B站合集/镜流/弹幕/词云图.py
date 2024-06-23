import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取TXT文件
with open('弹幕分词结果.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', ' ')

# 生成词云图
wordcloud = WordCloud(width=800, height=800,
                      font_path=r'C:/Windows/Fonts/simhei.ttf',  # 确保字体路径正确且可用
                      background_color='white',
                      min_font_size=10).generate(text)

# 展示词云图
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
