# B站评论分页爬取
import requests
import csv
import hashlib
import time
from urllib.parse import quote
import re


# 实现翻页爬取

# w_rid: 需要js逆向 md5(jt + wt) Jt = en.join("&") wt="ea1db124af3c7062474693fa704f4ff8"固定值
def hash(data, date):
    en = [
        "mode=3",
        "oid=1100057498",
        f"pagination_str={quote(data)}",
        "plat=1",
        "type=1",
        "web_location=1315875",
        f"wts=f{date}",  # 时间戳
    ]
    wt = "ea1db124af3c7062474693fa704f4ff8"
    Jt = '&'.join(en)
    string = Jt + wt
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    w_rid = MD5.hexdigest()
    print(w_rid)
    return w_rid


def get_content(data):
    date = int(time.time() )
    print(date)
    # {"offset": "{\"type\":1,\"direction\":1,\"session_id\":\"1758607821272706\",\"data\":{}}"}
    pagination_str = '{"offset":"{\\"type\\":1,\\"direction\\":1,"session_id\":\\"1758607821272706\\",\\"data\\":{\\"pn\\":%s}}"}' % data
    print(pagination_str)
    w_rid = hash(pagination_str, date)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
        'Referer': 'https://www.bilibili.com/'
    }
    "https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:1,%5C%22direction%5C%22:1,%5C%22session_id%5C%22:%5C%221758607821272706%5C%22,%5C%22data%5C%22:%7B%7D%7D%22%7D&plat=1&web_location=1315875&w_rid=a174d21d9f7cb5717f784d3632873ebd&wts=1717390474"
    "https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22%3A%22%7B%5C%22type%5C%22%3A1%2C%5C%22direction%5C%22%3A1%2C%22session_id%22%3A%5C%221758607821272706%5C%22%2C%5C%22data%5C%22%3A%7B%5C%22pn%5C%22%3A1%7D%7D%22%7D&plat=1&web_location=1315875&w_rid=f95c276578480b53b1ce5aa29b3c6826&wts=1717392254"
    url = 'https://api.bilibili.com/x/v2/reply/wbi/main?'
    data = {
        'oid': '1852698584',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":"{\\"type\\":1,\\"direction\\":1,"session_id\":\\"1758607821272706\\",\\"data\\":{\\"pn\\":%s}}"}' % data,
        'plat': '1',
        'web_location': '1315875',
        'w_rid': w_rid,
        'wts': date,
    }
    response = requests.get(url=url, params=data, headers=headers)
    prepared_request = requests.Request('Get',url,params=data,headers=headers)
    prepared_request = prepared_request.prepare()
    print(prepared_request.url)
    json_data = response.json()
    print(json_data)
    # 解析数据（字典取值）
    # 提取数据所在的列表
    replies = json_data['data']['replies']

    for index in replies:
        # 提取评论内容
        message = index['content']['message'].replace('\n', ',')  # 评论信息(replace替换换行符）
        like = index['like']  # 点赞数
        name = index['member']['uname']  # 昵称
        sex = index['member']['sex']  # 性别
        location = index['reply_control']['location'].replace('IP属地：', '')  # ip属地
        dit = {
            '昵称': name,
            '性别': sex,
            'IP': location,
            '评论': message,
            '点赞': like,
        }
        csv_writer.writerow(dit)
        print(dit)

    # 提取下一页的参数
    next_offset = json_data['data']['cursor']['pagination_reply']['next_offset']  # 第一个参数的获取
    next_page = re.findall('cursor\":(\d+)', next_offset)[0]
    return next_page


if __name__ == '__main__':

    f = open('data.csv', mode='w', encoding='utf-8', newline='')  # 创建文件对象，保存数据
    csv_writer = csv.DictWriter(f, fieldnames=[
        '昵称',
        '性别',
        'IP',
        '评论',
        '点赞',
    ])
    csv_writer.writeheader()

    for page in range(1, 11):
        next_page = get_content(page)