
import requests
import re
import datetime

# content_list存放所有弹幕
content_list = []
# 爬取开始日期和结束日期范围内的弹幕
begin = datetime.date(2023, 10, 10)
end = datetime.date(2024, 6, 11)
for i in range((end - begin).days + 1):
    day = begin + datetime.timedelta(days=i)
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=1295132590&date={day}'
    headers = {
        "Cookie":"buvid3=F20F4B52-ACB8-A021-3E0B-C346082E75AE97990infoc; b_nut=1697433797; CURRENT_FNVAL=4048; _uuid=B6E5D859-ECB4-5374-CEB3-ED2BCF41AF61098925infoc; buvid4=A0796219-8C0D-3CEA-74F0-BC1577B4BAAF99316-023101613-j+EVJ7V9TtLMVIMXjUkPKw%3D%3D; rpdid=|(kmJYmkk~k)0J'uYm~RJJ~mm; enable_web_push=DISABLE; header_theme_version=CLOSE; fingerprint=302abb9d1feb7abe011384358e53e1a6; buvid_fp_plain=undefined; SESSDATA=4d5c41d1%2C1713344487%2C042a1%2Aa2CjDCrSgSlisDAAfV8MGqQQGsXpmE5uLZGIM5sfxFreMgKnOnB4mI_UG7YyE6i6-_gqoSVklzTE44cmlJRmxCQnB3b0dLd25GTXBLb0lodWpfUFpPY0lnUUJqX2R2S19fT1hmOVYzRW12VVZaMktnODQwM2FseG9aQmNJak1NY2NpS2dfTFQwUmt3IIEC; bili_jct=d67ef1713484af58707c12c1697b1a8a; DedeUserID=406732493; DedeUserID__ckMd5=48c43aca436bb747; buvid_fp=302abb9d1feb7abe011384358e53e1a6; bp_video_offset_406732493=858548088305877015; LIVE_BUVID=AUTO9616989170857857; CURRENT_QUALITY=80; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTk5NDkxNTEsImlhdCI6MTY5OTY4OTg5MSwicGx0IjotMX0.LgcasmNZYUOxswBAJk2xWPmZ4ZYep-AbnhRucwu3c8A; bili_ticket_expires=1699949091; b_lsid=AE210A71E_18BC86FBB01; PVID=1; home_feed_column=5; browser_resolution=1707-861; sid=8ncrwo4o",
        "Referer":"https://search.bilibili.com/all?",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    temp_list = re.findall('[\u4e00-\u9fa5]+', response.text)
    content_list.extend(temp_list)
    print("爬取", day, "日弹幕,获取到：", len(temp_list), "条弹幕，已经增加到总列表。总列表共有", len(content_list),
          "条弹幕。")
print(content_list)
# 保存数据
content = '\n'.join(content_list)
with open('弹幕.txt', mode='a', encoding='utf-8') as f:
    f.write(content)
print("保存完成")

