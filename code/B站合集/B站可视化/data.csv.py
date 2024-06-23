
import time

# 导入数据请求模块 第三方模块 需要安装
import requests
# 导入格式化输出模块
from pprint import pprint
import datetime
# 导入csv模块
import csv
import hashlib

f = open('信息.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '描述',
    'BV号',
    '播放量',
    '弹幕',
    '评论',
    '时长',
    '上传时间',
])
csv_writer.writeheader()
"""
1. 发送请求, 模拟浏览器对于url地址发送请求
    请求链接: 数据包链接
    
- 模拟浏览器: headers 请求头
    字典数据类型, 构建完整键值对形式
    
- 请求链接:
    请求链接和请求参数分开写
        问号前面: 请求链接
        问号后面: 请求参数/查询参数
    批量替换:
        1. 选择替换内容, ctrl+R
        2. 输入正则命令进行匹配替换
            (.*?): (.*)
            '$1': '$2',
            
多写的数据采集 --> 分析请求链接参数变化规律
"""

# 模拟浏览器 -> 基本反反爬虫措施
headers = {
    # 用户代理 表示浏览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
for page in range(1, 11):
    string = f'keyword=&mid=517327498&order=pubdate&order_avoided=true&platform=web&pn={page}&ps=30&tid=0&web_location=1550101&wts={int(time.time())}6eff17696695c344b67618ac7b114f92'
    # 实例化对象
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    # 请求链接
    url = 'https://api.bilibili.com/x/space/wbi/arc/search'
    # 请求参数
    data = {
        'mid': '517327498',
        'ps': '30',
        'tid': '0',
        'pn': page,
        'keyword': '',
        'order': 'pubdate',
        'platform': 'web',
        'web_location': '1550101',
        'order_avoided': 'true',
        'w_rid': md5_hash.hexdigest(),
        'wts': int(time.time()),
    }
    # 发送请求 <Response [200]> 响应对象 表示请求成功
    response = requests.get(url=url, params=data, headers=headers)
    print(response.json())
    """
    2. 获取数据, 获取服务器返回响应数据
        开发者工具: response
    
    获取响应数据:
        - response.json() 获取响应json数据
            <字典数据类型>
        - response.text 获取响应文本数据
            <网页源代码 字符串数据>
        - response.content 获取响应二进制数据数据
            <获取图片/视频/音频/特定格式文件>
    
    3. 解析数据, 提取我们需要的数据内容
        视频基本信息
    
字典数据 --> 键值对取值
    根据冒号左边的内容[键], 提取冒号右边的内容[值]
    
    response.json()['data']['list']['vlist'] --> 返回列表
        列表里面包含整个网页视频信息 <N个视频内容>
    
    列表 / 字典 / 集合 / 元组 --> 数据容器 <装东西的盒子>
    
        lis = [1, 2, 3, 4, 5] --> for循环遍历, 把列表里面内容一个一个单独提取
    for li in lis:
        # 从lis这个盒子里面, 把元素<东西> 拿出来, 用li变量接收
    
    print(index)    输入一行效果
    pprint(index)   多行展开效果
    """
    for index in response.json()['data']['list']['vlist']:
        # 时间戳 时间节点 --> 上传视频时间点
        date = index['created']
        dt = datetime.datetime.fromtimestamp(date)
        dt_time = dt.strftime('%Y-%m-%d')
        dit = {
            '标题': index['title'],
            '描述': index['description'],
            'BV号': index['bvid'],
            '播放量': index['play'],
            '弹幕': index['video_review'],
            '评论': index['comment'],
            '时长': index['length'],
            '上传时间': dt_time,
        }
        # 写入数据
        csv_writer.writerow(dit)
        print(dit)
