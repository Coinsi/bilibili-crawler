import pandas as pd
import json

# 读取CSV文件
nodes_df = pd.read_csv('nodes.csv')
edges_df = pd.read_csv('edges.csv')

# 转换节点数据
nodes_list = []
for index, row in nodes_df.iterrows():
    node = {
        'id': row['id'],
        'label': row['用户'],
        'shape': 'circularImage',
        'image': row['头像']
    }
    nodes_list.append(node)

# 转换边数据
edges_list = []
for index, row in edges_df.iterrows():
    edge = {
        'from': row['source'],
        'to': row['target']
    }
    edges_list.append(edge)

# 保存为JSON文件
with open('nodes.json', 'w') as f:
    json.dump(nodes_list, f)

with open('edges.json', 'w') as f:
    json.dump(edges_list, f)

print("JSON文件已生成：nodes.json和edges.json")
