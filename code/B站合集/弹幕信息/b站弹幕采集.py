
import requests
import dm_pb2
from google.protobuf import text_format
import re
from datetime import datetime
import csv


with open("danmu.csv", mode='w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["弹幕所在位置", "弹幕内容", "弹幕发布时间"])
headers = {
    'cookie': "buvid3=355AA300-6A61-04E5-A05C-E891D886F69632716infoc; b_nut=1675085932; i-wanna-go-back=-1; _uuid=387EA3810-FBF5-E92C-827E-2510B578C5B9A33232infoc; buvid4=15C69C98-F6A7-EC6A-872F-E69C1840DD6D33724-023013021-1pW1w45e5fZS9RtebDiGZw%3D%3D; nostalgia_conf=-1; rpdid=|(kmJY|k))lY0J'uY~l|)lmY|; b_ut=5; is-2022-channel=1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO3216755179681630; header_theme_version=CLOSE; CURRENT_PID=17897430-d93d-11ed-a1f4-675e4c96ff79; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; fingerprint=58d6d808ef27a6225c943be7ca980284; buvid_fp=58d6d808ef27a6225c943be7ca980284; enable_web_push=DISABLE; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIzODAyNjYsImlhdCI6MTcwMjEyMTAwNiwicGx0IjotMX0.hHZgEl37y35RHgNUEbXnT3y_rtg_w3d1O46vW5TreIQ; bili_ticket_expires=1702380206; SESSDATA=0f019744%2C1717673066%2Ca41c0%2Ac2CjArLmPZFHNFg3B5H60pjRwiqJSLXDG8l2Pb_74Q11o8NmBWyKegdnFb6ivxUL255pwSVjRoaXFXVmFoRlFXY3VCRTAybEpud2ltaXFkRzZXQ25uZ3h0VGxrdGg3bWcxQ2hJN3d4VEZQRjRRTnd5cUx2TmJfUUdlWVZocVRfb281QnJHSklrTkJ3IIEC; bili_jct=f2a37b8a7351e9987d90f80d72dab593; DedeUserID=422789639; DedeUserID__ckMd5=fc4901c78719b545; b_lsid=125EDCFE_18C4E7B181A; home_feed_column=5; browser_resolution=1920-963; sid=6qcgbo4l; PVID=2",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
url = 'https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?type=1&oid=323723441&pid=715024588&segment_index=1&pull_mode=1&ps=0&pe=120000&web_location=1315873&w_rid=8138667fe7c9a9d9aa23f488f69e5c2d&wts=1702124018'
# 1.发送请求
response = requests.get(url=url, headers=headers)
my_seg = dm_pb2.DmSegMobileReply()
data = response.content
my_seg.ParseFromString(data)
for i in my_seg.elems:
    parse_data = text_format.MessageToString(i, as_utf8=True)
    try:
        progress = re.findall('progress: (.*)', parse_data)[0]
    except:
        progress = 1000
    minutes, seconds = divmod(int(progress) // 1000, 60)
    current_time = f'{minutes:02d}:{seconds:02d}'
    content = re.findall('content: (.*)', parse_data)[0]
    ctime = re.findall('ctime: (.*)', parse_data)[0]
    date_time = datetime.fromtimestamp(int(ctime)).strftime('%Y-%m-%d %H:%M:%S')
    print(current_time, content, date_time)
    with open("danmu.csv", mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([current_time, content, date_time])