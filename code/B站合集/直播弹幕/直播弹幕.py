
# 导入数据请求模块 pip install requests
import requests
# 导入csv模块 内置模块
import csv
# 导入时间模块
import time

# 创建文件对象
f = open('dydata.csv', mode='w', encoding='utf-8', newline='')
# 字典写入
csv_writer = csv.DictWriter(f, fieldnames=['昵称', '时间', '弹幕'])
# 写入表头
csv_writer.writeheader()
"""发送请求: 模拟浏览器对于url地址发送请求"""
# 模拟浏览器
headers = {
    # User-Agent 用户代理: 表示浏览器/设备基本身份信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
for page in range(1, 21):
    print('=='*20)
    # url地址: 请求网址
    url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=545068&room_type=0'
    # 发送请求
    response = requests.get(url=url, headers=headers)
    """获取数据: 获取服务器返回的响应数据内容"""
    # 获取响应json数据
    json_data = response.json()
    """解析数据: 提取我们需要的数据内容"""
    # 提取弹幕数据所在列表 room
    dm_list = json_data['data']['room']
    # for循环遍历, 提取列表里面元素
    for index in dm_list:
        # 提取昵称
        nickname = index['nickname']
        # 弹幕内容
        text = index['text']
        # 弹幕时间
        timeline = index['timeline']
        # 把数据保存字典里面
        dm_dict = {
            '昵称': nickname,
            '时间': timeline,
            '弹幕': text,
        }
        # 写入数据
        csv_writer.writerow(dm_dict)
        print(nickname, timeline, text)
    time.sleep(2)