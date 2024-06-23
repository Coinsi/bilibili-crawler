import time
import requests
from pprint import pprint
import datetime
import csv
import hashlib
import json

# 打开或创建CSV文件以追加模式
with open('星穹铁道.csv', mode='a', encoding='utf-8', newline='') as f:
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

    # 定义文件名列表
    json_files = ['data1.json', 'data2.json', 'data3.json', 'data4.json', 'data5.json']

    # 遍历每个JSON文件
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)  # 解析当前JSON文件内容

            # 遍历当前文件中的数据并写入CSV
            for index in data['data']['list']['vlist']:
                # 处理时间戳并格式化
                date = index['created']
                dt = datetime.datetime.fromtimestamp(date)
                dt_time = dt.strftime('%Y-%m-%d')

                # 准备写入的数据字典
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

                # 写入数据到CSV
                csv_writer.writerow(dit)
                print(dit)  # 打印当前条目

# 注意：这里外部的with语句确保了CSV文件在所有操作完成后会被正确关闭
