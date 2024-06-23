import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('星穹铁道.csv')

# 确保'评论'列的数据类型为字符串
df['描述'] = df['描述'].astype(str)

# 生成用于词云的文本
text = " ".join(review for review in df['描述'])

# 生成词云图
wordcloud = WordCloud(width=800, height=800,
                      font_path=r'C:/Windows/Fonts/simhei.ttf',
                      background_color='white',
                      min_font_size=10).generate(text)

# 展示词云图
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
