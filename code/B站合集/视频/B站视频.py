"""
[课程内容]: python爬虫 --批量采集B站女团舞蹈视频

*python基础入门，0基础学员听完即会哦！！！！！！

[授课老师]：青灯教育-思语老师
[上课时间]：晚上20:05
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信

[相关模块]：
    第三方模块（需要下载）：
        requests >>> pip install requests
        下载方法：win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
    内置模块（不用下载）：
        re
        json
        pprint
        subprocess
        os
[课程内容]：
        1. 网络爬虫
        2. json数据获取
        3. re正则表达式
        4. 列表以及字典取值
        5. ffmpeg合成视频

[开发环境]：python3.8 | Anaconda
[开发工具]: Pycharm 2021.2版本 , ffmpeg <需要设置环境变量>
---------------------------------------------------------------------------------------------------
0基础  0
有基础  1
基本思路:
1.分析数据来源   B站
2.实现代码
2.1 发送请求  浏览器  -->服务器
2.2 获取数据  网页源代码
2.3 解析数据
2.4 保存数据
"""
import requests  # 第三方   需要下载  知道  1  不知道 0 pip install requests  -->> cmd  win+R
import re  # 正则  内置模块  无需下载
import json # 内置模块 无需下载
import pprint  # 内置模块  无需下载
import subprocess # 内置模块  无需下载
import os  # 内置模块  无需下载
"""
2.1 发送请求  浏览器  -->服务器    网页源代码    爬虫()
"""
url = 'https://www.bilibili.com/video/BV1tT4y1Q7zF/?spm_id_from=pageDriver&vd_source=b2da3931eefc454d41eb6bb5b34749d1'
# response 请求状态
# 伪装
headers = {
    # 防盗链
    'referer': 'https://space.bilibili.com/7151101/video',
    # 用户代理   浏览器的基本身份
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=headers)
# <Response [200]>   响应对象  成功
print(response)
"""
2.2 获取数据  网页源代码
"""
print(response.text)

"""
2.3 解析数据
"""
# title 视频的名字
title = re.findall('"title":"(.*?)","pubdate":', response.text)[0].replace(' ', '')
print(title)
title = re.sub(r'[\/:*?"<>|]','',title)

# <script>  网页标签
re_data = re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
# print(re_data)
# json
json_data = json.loads(re_data)
# print(json_data)

# pprint  模块  格式化输出   方便找数据
# pprint.pprint(json_data)
# 视频  声音(音频)
# 声音(音频)链接
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
print(audio_url)
# 视频链接
video_url = json_data['data']['dash']['video'][0]['baseUrl']
print(audio_url)
# 再次发送请求   403  404  访问网页失败  防盗链  200 成功
# 滑动验证码   身份信息    反爬  (vip,豆瓣,大一点网页)
"""
爬虫基础知识  -->>  原理  案例  项目  python基础
找工作  1  1-3个月  核心编程(基础)  +高级开发  +爬虫
    爬虫
    数据分析
    开发  小程序  网站  系统
    人工智能   工厂(智能) 智能机器人  语音助手
    自动化办公  
    ...
兼职外包   2   兼职群+ 兼职渠道+兼职指导
    外包 1   不知道 0
    个人/企业需求   自己做不了   技术    外包(兼职)
    1.应用技术   2.项目,外包   经验
    兼职平台  二手    群 
系统图:999  
找清风老师  --> 预定300学费   3个  --> 1个
    福利:8880  核心编程  + 高级开发  +爬虫  + 数据分析  +前端  + 后端
        1. 分期免息 (0利息0手续费) -->>  18  每个月493   一天16  一杯奶茶钱
           9月14号  -->10月14号  
        2.人工智能  1 +  自动化办公(提高工作效率,升职加薪) 4880  送大家
        3.两年学习权限    系统班7个月
"""

audio_response = requests.get(audio_url,headers=headers)
# print(audio_response.text)
# content 二进制  audio_content音频解析过后数据
audio_content = audio_response.content
# 视频解析
video_response = requests.get(video_url,headers=headers)
# print(video_response.text)
# content 二进制  audio_content音频解析过后数据
video_content = video_response.content
# print(video_content)
"""
4.保存数据  open()
"""
# 保存音频
with open('video\\'+ title +'.mp3', mode='wb') as file:
    file.write(audio_content)
# 保存视频
with open('video\\'+ title +'.mp4', mode='wb') as f:
    f.write(video_content)
# 音频和视频合成
cmd = f"ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4"
subprocess.run(cmd, shell=True)
# 删除合成前的视频和音频
os.remove(f'video\\{title}.mp3')
os.remove(f'video\\{title}.mp4')