
# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入加密模块
import hashlib
# 导入时间模块
import time


def Hash(num, date_time):
    """
    :param num: 页码
    :param date_time: 时间戳
    :return:
    webpack -> 扣代码
    根据经验: 了解到是MD5 --> 可以直接写出来
    """
    string = f'oid=1295132590&pid=321985838&segment_index={num}&type=1&web_location=1315873&wts={date_time}ea1db124af3c7062474693fa704f4ff8'
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    w_rid = MD5.hexdigest()
    return w_rid


for page in range(1, 10):
    date_time = int(time.time())
    w_rid = Hash(page, date_time)
    # print(w_rid)
    """发送请求"""
    url = f'https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?type=1&oid=1295132590&pid=321985838&segment_index={page}&web_location=1315873&w_rid={w_rid}&wts={date_time}'
    # 模拟浏览器 <请求头>
    headers = {
        "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
        "Referer":"https://search.bilibili.com/all?",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    # 发送请求
    response = requests.get(url=url, headers=headers)

    response.encoding = 'utf-8'
    """获取数据"""
    html_data = response.text
    print(html_data)
    """解析数据"""
    content_list = re.findall(':(.*?)@', html_data)
    for index in content_list:
        print(index[1:])
        with open('弹幕.txt', 'a', encoding='utf-8') as f:
            f.write(index[1:] + '\n')