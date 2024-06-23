import requests
import re
import time
import hashlib
from urllib.parse import quote
def GetResopnse(url,data):


    headers = {
        "Referer": "https://www.bilibili.com/video/BV1Mp421y7aB/?spm_id_from=333.999.0.0&vd_source=041ac3111b97c305b7e8b63eea19f3bf",
        "Cookie": "buvid4=8B886E99-4A18-9FC8-0027-9817B5C4E6CD24845-023052520-YoPclWlyTGeBE4hp66K30w%3D%3D; rpdid=|(k|mmJll)~k0J'uY)l|u)kYY; PVID=1; FEED_LIVE_VERSION=V8; fingerprint=8e22be6ac6c3061de06ee7a2d7c216af; buvid_fp_plain=undefined; buvid_fp=8e22be6ac6c3061de06ee7a2d7c216af; enable_web_push=DISABLE; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; CURRENT_FNVAL=4048; hit-dyn-v2=1; LIVE_BUVID=AUTO8017156967054546; buvid3=054A759D-B56C-DE6D-F22E-80643B5922EB32866infoc; b_nut=1717305032; bsource=search_baidu; _uuid=4FC7CA6B-10A77-AD87-A152-62F759CC9EA1034334infoc; browser_resolution=1280-569; SESSDATA=b69f75b2%2C1732857038%2Ceaed9%2A61CjD6bMio0QNEXLBP9XC8Q35_m3jWhW1Kko1j4-fpuBoWIxOluyE1thipvgCcHXTbsBUSVmpTTHp0SkxKYmF1VHd2eEJTMGhzMFFCYmlnemRaa0FReU5SQ1llZXFSckNocG9JWnhGQlBSTnJkUTBrUEtOMFIwTnM4SWlNRWZZeTVEdmhIODhtSVJnIIEC; bili_jct=1ae6d017ad6e71e99f2a83102154f0e7; header_theme_version=CLOSE; sid=4o5n5ipo; CURRENT_QUALITY=64; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc1Nzg1NzEsImlhdCI6MTcxNzMxOTMxMSwicGx0IjotMX0.jrxYXmAJbTaPn0q28mBLx173AKyMlk6RwAn8RB_9S5c; bili_ticket_expires=1717578511; bp_t_offset_669002132=938366224360800293; b_lsid=55DAAB87_18FD854FB2C",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url,params=data,headers=headers)
    print(response.text)
    return response

def GetContent(data):
    date = (time.time() * 1000)
    pagination_str = '{"offset":"{\\"type\\":1,\\"direction\\":1,\\"data\\":{\\"pn\\":%s}}"}' % data
    w_rid = hash(pagination_str, date)
    # url
    link = 'https://api.bilibili.com/x/v2/reply/wbi/main?'
    # link = 'https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=67f2d82e5c9e90b348b5d587494c90a0&wts=1717321963',
    data = {
        'oid': '1852698584',
        'type': '1',
        'mode': '3',
        'pagination_str': '{"offset":"{\\"type\\":1,\\"direction\\":1,\\"data\\":{\\"pn\\":%s}}"}' % data,
        'plat': '1',
        'web_location': '1315875',
        'w_rid': w_rid,
        'wts': date,
    }

    response = GetResopnse(url=link,data=data)

    JsonData=response.json()
    print(JsonData)
        # replies = JsonData['data']['replies']
        # for index in replies:
        #     dict = {
        #         '昵称': index['member']['uname'],
        #         '性别': index['member']['sex'],
        #         '地区': index['reply_control']['location'].replace('IP属地：',''),
        #         '评论': index['content']['message'],
        #
        #     }
        #     print(dict)

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

if __name__ == '__main__':
    GetContent(1)