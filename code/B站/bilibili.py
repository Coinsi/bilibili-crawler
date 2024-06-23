import requests
import csv
import hashlib
import time
from urllib.parse import quote
def GetResopnse(url,data=None):


    headers = {
        "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url,data=data,headers=headers)
    prepared_request = requests.Request('Get',url,params=data,headers=headers)
    prepared_request = prepared_request.prepare()
    print(prepared_request.url)
    return response

def GetContent(date,nextpage,w_rid):
    """"获取评论数据内容"""
    # url
    link = 'https://api.bilibili.com/x/v2/reply/wbi/main'
    # link = 'https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=67f2d82e5c9e90b348b5d587494c90a0&wts=1717321963'
    # link =   'https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22%3A%22%22%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=3deacf4190c7e526cf41526ea3d63e1d&wts=1717390169'
    params = {
        'oid': '1852698584',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":""}',
        'plat': '1',
        'seek_rpid': '',
        'web_location': '1315875',
        'w_rid': '67f2d82e5c9e90b348b5d587494c90a0',
        'wts': '1717321963',
    }

    response = GetResopnse(url=link, data=params)
    JsonData = response.json()
    print(JsonData)
    replies = JsonData['data']['replies']
    info_list = []
    for index in replies:
        dict = {
            '昵称': index['member']['uname'],
            '性别': index['member']['sex'],
            '地区': index['reply_control']['location'].replace('IP属地：', ''),
            '评论': index['content']['message'],

        }
        print(dict)
        # 加入列表
        info_list.append(dict)
        next_offset = JsonData['data']['cursor']['pagination_reply']['next_offset']
        return info_list,next_offset

def Hash(date, nextpage):
    next_offset = '{"offset":"%s"}'% nextpage
    print(next_offset)
    print(quote(next_offset))

    en = [
        "mode=3",
        "oid=1852698584",
        f"pagination_str={quote(next_offset)}",
        "plat=1",
        "seek_rpid=",
        "type=1",
        "web_location=1315875",
        f"wts={date}",
    ]
    Jt = "&".join(en)
    string = Jt + "ea1db124af3c7062474693fa704f4ff8"
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    print(MD5.hexdigest())

    return MD5.hexdigest()


if __name__ == '__main__':

    f=open('bilibili.csv','w',encoding='utf-8',newline='')
    writer=csv.DictWriter(f,fieldnames=['昵称','性别','地区','评论'])
    writer.writeheader()
    date = int(time.time())
    nextpage = '""'
    for page in range(1, 100):
        print(f'第{page}页')
        w_rid = Hash(date=date, nextpage=nextpage)
        info_list,nextpage =GetContent(date=date,nextpage=nextpage,w_rid=w_rid)
        for info in info_list:
            writer.writerow(info)
    # w_rid = Hash(date=date, nextpage=nextpage)
    #
    # info_list,nextpage =GetContent(date=date,nextpage=nextpage,w_rid=w_rid)
    #
    # # info_list =GetContent()
    # for info in info_list:
    #     writer.writerow(info)
    GetContent(date=date, nextpage=nextpage, w_rid=w_rid)