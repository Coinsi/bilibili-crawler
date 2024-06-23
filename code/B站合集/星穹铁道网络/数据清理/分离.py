import pandas as pd

# 读取CSV文件
df = pd.read_csv('total.csv', encoding='GBK')

# 删除包含空字段或仅包含空格的行
df_cleaned = df.dropna().replace(r'^\s*$', float('NaN'), regex=True).dropna()

# 创建节点表，合并“用户”和“粉丝名称”列并去重
all_users = pd.concat([df_cleaned['用户'], df_cleaned['粉丝名称']]).unique()
nodes = pd.DataFrame(all_users, columns=['用户'])
nodes['id'] = nodes.index

# 初始化新的列
nodes['标题链接'] = ''
nodes['头像'] = ''
nodes['个性签名'] = ''

# 创建一个字典来映射用户名称到ID
user_to_id = nodes.set_index('用户').to_dict()['id']

# 填充节点表中的其他字段
for index, row in df_cleaned.iterrows():
    fan_name = row['粉丝名称']
    if fan_name in user_to_id:
        user_id = user_to_id[fan_name]
        nodes.loc[user_id, '标题链接'] = row['标题链接']
        nodes.loc[user_id, '头像'] = row['头像']
        nodes.loc[user_id, '个性签名'] = row['个性签名']

# 创建边表
edges = df_cleaned[['用户', '粉丝名称']].copy()
edges['source'] = edges['用户'].map(user_to_id)
edges['target'] = edges['粉丝名称'].map(user_to_id)

# 删除节点表中包含空字段或仅包含空格的行
nodes_cleaned = nodes.replace(r'^\s*$', float('NaN'), regex=True).dropna()

# 重新创建字典来映射用户名称到ID
user_to_id_cleaned = nodes_cleaned.set_index('用户').to_dict()['id']

# 过滤边表，移除包含被删除用户的边
edges_cleaned = edges[edges['source'].notna() & edges['target'].notna()]
edges_cleaned = edges_cleaned[edges_cleaned['source'].isin(user_to_id_cleaned.values()) & edges_cleaned['target'].isin(user_to_id_cleaned.values())]

# 保存节点表和边表到CSV文件
nodes_cleaned.to_csv('nodes.csv', index=False)
edges_cleaned.to_csv('edges.csv', index=False)
