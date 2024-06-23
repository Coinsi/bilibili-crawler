import pandas as pd

# 读取CSV文件
df = pd.read_csv('test2.csv', encoding='GBK')
# 创建一个新的ID列，这里使用range函数生成递增的ID值
df['id'] = range(1, len(df) + 1)
# 初始化节点和边的集合
nodes = set()
edges = []

# 处理每行数据
for _, row in df.iterrows():
    user = row['用户']
    fan = row['粉丝名称']
    user_img_url = row['头像']
    user_desc = row['desc']
    user_profile_url = row['标题链接']
    id=row['id']
    # 添加节点
    nodes.add((id,user, user_img_url, user_desc, user_profile_url))
    nodes.add((id,fan, user_img_url, user_desc, user_profile_url))

    # 添加边
    edges.append(f"{{from: 1, to: {id}}}")

# 生成节点JavaScript字符串
nodes_js = [
    f"{{id: '{id}', label: '{name}\\n{desc}', shape: 'circularImage', image: '{img}'}}"
    for id, name, img, desc, profile_url in nodes
]

nodes_string = ',\n            '.join(nodes_js)
edges_string = ',\n            '.join(edges)

# 创建完整的HTML内容
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Network Graph</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <style>
        #mynetwork {{
            width: 800px;
            height: 600px;
            border: 1px solid lightgray;
        }}
    </style>
</head>
<body>
    <div id="mynetwork"></div>
    <script>
        // DOM 元素
        var container = document.getElementById('mynetwork');

        // 初始化节点和边
        var nodes = new vis.DataSet([
            {nodes_string}
        ]);

        var edges = new vis.DataSet([
            {edges_string}
        ]);

        // 提供数据
        var data = {{
            nodes: nodes,
            edges: edges
        }};

        // 网络图选项
        var options = {{
            nodes: {{
                borderWidth: 2,
                size: 30,
                color: {{
                    border: '#406897',
                    background: '#6AAFFF'
                }},
                font: {{
                    color: '#eeeeee'
                }}
            }},
            edges: {{
                color: 'lightgray'
            }}
        }};

        // 初始化网络图
        var network = new vis.Network(container, data, options);
    </script>
</body>
</html>
"""

# 打印生成的HTML内容，进行调试
print(html_content)

# 写入到HTML文件，使用UTF-8编码
with open('network_graph.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file has been created.")
