# 导入数据请求模块 pip install requests
import requests
# 导入正则表达式模块
import re
"""发送请求 视频网页源代码中是存在 oid --> cid"""
headers = {

    "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
# url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=1330002174'
url ='https://api.bilibili.com/x/v1/dm/list.so?oid=1567163859'
response = requests.get(url, headers=headers)
# 转码
response.encoding = 'utf-8'
"""获取数据"""
html_data = response.text
print(html_data)
"""解析数据
- re.findall('数据', '数据源') --> 找到所有数据
    从什么地方, 去匹配什么数据
"""
content_list = re.findall('<d p=".*?">(.*?)</d>', html_data)
# 列表合并成字符串
content = '\n'.join(content_list)
with open('弹幕.txt', mode='a', encoding='utf-8') as f:
    f.write(content)
    f.write('\n')
print(content)
