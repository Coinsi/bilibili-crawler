import pandas as pd

# 读取CSV文件
df = pd.read_csv('total.csv', encoding='GBK')

# 删除任何包含空字段的行
df_cleaned = df.dropna()

# 保存处理后的数据到新的CSV文件
df_cleaned.to_csv('cleaned_file.csv', index=False)

print("数据清理完成并保存到cleaned_file.csv")
