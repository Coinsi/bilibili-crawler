
# 导入数据请求模块 (需要安装 pip install requests)
import requests
# 导入csv模块 (不需要安装 内置模块)
import csv
# 导入哈希模块 (不需要安装 内置模块)
import hashlib
# 导入时间模块 (不需要安装 内置模块)
import time
from urllib.parse import quote
# 导入json模块
import json


def GetResponse(url, data):
    """定义发送请求函数: 模拟浏览器对于url地址发送请求
    - def 关键字 用于定义函数
    - GetResponse 自定义函数名
    - url / data 形式参数(名字自定义)
        后续调用 GetResponse 函数的时候, 需要传入两个参数 url(网址) data(查询参数)
    """
    # 模拟浏览器
    headers = {

        "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    # 发送请求
    response = requests.get(url=url, params=data, headers=headers)
    # 返回响应对象
    return response


def GetContent(date, NextPage, w_rid):
    print('获取数据参数:', NextPage)
    """获取评论数据内容"""
    # 请求网址
    link = 'https://api.bilibili.com/x/v2/reply/wbi/main'
    # 查询参数
    params = {
        # 'oid': '1852698584',
        'oid': '1955288088',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":%s}' % NextPage,
        'plat': '1',
        'web_location': '1315875',
        'w_rid': w_rid,
        'wts': date,
    }
    # 调用发送请求函数
    response = GetResponse(url=link, data=params)
    # 获取响应json数据内容
    JsonData = response.json()
    """解析数据: 提取我们需要的数据内容"""
    # 根据字典取值, 提取评论数据所在列表 replies
    replies = JsonData['data']['replies']
    # 定义空列表
    info_list = []
    # for循环遍历, 提取列表里面元素
    for index in replies:
        try:
            # 提取具体数据, 保存字典里面
            dit = {
                '昵称': index['member']['uname'],
                '性别': index['member']['sex'],
                '地区': index['reply_control']['location'].replace('IP属地：', ''),
                '评论': index['content']['message'],
            }
            print(dit)
            # 把字典添加到空列表中
            info_list.append(dit)
        except:
            pass
    # 获取下一页的参数内容
    next_offset = JsonData['data']['cursor']['pagination_reply']['next_offset']
    offset = json.dumps(next_offset)
    # 返回数据内容
    return info_list, offset


def Hash(date, NextPage):
    next_offset = '{"offset":%s}' % NextPage
    pagination_str = quote(next_offset)
    print('加密next_offset:', next_offset)
    print('加密pagination_str:', pagination_str)
    """获取w_rid值"""
    en = [
        "mode=3",
        # "oid=1852698584",
        "oid=1955288088",
        f"pagination_str={pagination_str}",
        "plat=1",
        "type=1",
        "web_location=1315875",
        f"wts={date}"
    ]
    Jt = '&'.join(en)
    string = Jt + "ea1db124af3c7062474693fa704f4ff8"
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    w_rid = MD5.hexdigest()
    print(w_rid)
    return w_rid


if __name__ == '__main__':
    # 创建文件对象
    f = open('pvz.csv', mode='w', encoding='utf-8', newline='')
    # 字典写入方式
    csv_writer = csv.DictWriter(f, fieldnames=['昵称', '性别', '地区', '评论'])
    # 写入表头
    csv_writer.writeheader()
    # 定义第一页参数
    NextPage = '""'
    for page in range(1, 51):
        print(f'正在采集第{page}页的数据内容')
        # 获取当前时间戳
        date = int(time.time())
        # 获取加密参数
        w_rid = Hash(date=date, NextPage=NextPage)
        # 获取数据内容
        info_list, NextPage = GetContent(date, NextPage, w_rid)
        print(NextPage)
        # for循环遍历, 一条一条进行保存
        for info in info_list:
            # 写入数据
            csv_writer.writerow(info)