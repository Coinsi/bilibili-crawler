"""
[课程内容]: Python采集B站番剧内容

[授课老师]: 青灯教育-自游 [上课时间]: 20:05 可以点歌 可以问问题

[环境使用]:
    Python 3.8
    Pycharm
    ffmpeg  <需要设置环境变量> 软件 找木子老师获取

[模块使用]:
    import requests >>> pip install requests
    import subprocess

win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信

目标网址: https://www.bilibili.com/bangumi/play/ep249469

对于本节课内容, 不懂的地方多问.....

第一步: 抓包分析 / 分析视频内容数据
    通过开发者工具进行抓包分析
    1. 通过 m4s 媒体文件 --> 找到对应数据包
        数据包: https://api.bilibili.com/pgc/player/web/v2/playurl <音频和视频>
    2. 通过 不同集数 数据包参数对比
        avid cid ep_id
    参数对应数据包 -> https://api.bilibili.com/pgc/view/web/season?ep_id=249469

目的: 获取视频画面内容 / 音频内容
需要三个参数: avid cid ep_id --> https://api.bilibili.com/pgc/view/web/season?ep_id=249469

爬虫基本步骤: 发送请求 -> 获取数据 -> 解析数据 -> 保存数据
    发送请求 -> 对于数据所在链接地址请求
    获取数据 -> 获取服务器返回的数据内容
    解析数据 -> 提取你需要的数据
    保存数据 -> 把你需要的数据进行保存

headers 根据不同网站, 添加字段是不一样的
    B站: 登陆账号 视频清晰度更高

批量替换:
    选择替换的内容 -> ctrl + R 输入正则命令 进行匹配替换
        (.*?): (.*) --> 你要匹配什么数据
        '$1': '$2', --> 需要替换添加什么内容

本节课所使用知识点:
- 基础知识点:
    print 输出函数
    for循环遍历
    列表取值 / 字典取值
    字符串创建定义 / 字典创建
    open函数的使用

- 爬虫知识点:
    开发者工具抓包
    requests.get()简单使用
    响应数据获取

基本三节课课程内容 + 三节爬虫基础 = 可以简单实现爬虫案例
    图片 音频 视频 文字 小说 电商....

青灯教育公开课讲解案例: 大多数都爬虫公开课
    简单 --> 效果明显

老师说6节课 --> 系统课程学习6节课
    不是在B站上面看6节课


系统课程: 付费
    从零基础入门到项目实战 --> 达到企业开发水平
        包含: 基础 爬虫 数据分析 网站开发 自动化办公 人工智能

公开课: 免费
    以案例演示为主, 告诉你python可以实现什么案例
        6-10节课程内容就可以掌握, 自助写出来案例水平

课程大纲 / 学习路线图 加清风老师微信: pythonmiss


解答辅导 / 是否有专业人员给予解答辅导....


系统课程教学:
    - 直播授课
        一周三节课, 晚上8-10点直播授课
    - 课程录播 源码 笔记 文档 软件 作业 考核
    - 老师解答辅导
    - 班主任监督学习
    - 免费重修
    - 外包指导
    - 就业指导
    - 培训合同
    - 发票
    ...

一个月337元学费, 用于提升自己学习? 这个应该是OK没有问题吧

1. 是否能够学会?
    答案: 能, 你可能一遍学的不够扎实, 但是咱们可以让你学N遍
    - 零基础入门开始
    - 不懂直接找老师解答辅导, 哪里不懂 解决哪里
一周三节课 --> 一节课平均2.5个小时,
    每天花2.5个小时用于学习python, 这个时间没有吗?

8小时内求生存 <工作时间>
8小时外求发展 <通勤 吃喝拉撒>
8小时睡觉休息

学生:
    8-20 --> 0点之前还有4个小时 中午休息
工作:
    996 -> 10点到家 睡觉2个小时

周末 --> 休息 该玩还是可以玩
    坚持每天学习2.5个小时左右时间

我想要自学看看, 看自己是否有天赋?
    我们大多数的同学 --> 学编程 <就业 实现程序>


软件界面: 肉眼可见的内容
功能:
    下载 --> 爬虫
    上传 --> 爬虫
    可视化 计数器....

"""
# 导入数据请求模块
import requests
import subprocess
import re
# 模拟浏览器 headers请求头 复制
headers = {
    # 用户信息, 常用于检测是否有登陆账号
    'Cookie': 'buvid3=25E54027-80D1-B1E0-DB5B-7B2615931E6C60632infoc; b_nut=1692798760; _uuid=B59E6723-A36D-6FE9-D10F6-6ACD7ABC5D2861093infoc; buvid4=CB3D23B0-8B22-09E0-B688-28E1D84E0A4661983-023082321-j%2BEVJ7V9TtLMVIMXjUkPKw%3D%3D; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1707-861; DedeUserID=406732493; DedeUserID__ckMd5=48c43aca436bb747; LIVE_BUVID=AUTO8416938255547969; b_lsid=2C35F5C8_18A7489B72F; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0MzE0OTcsImlhdCI6MTY5NDE3MjI5NywicGx0IjotMX0.pX9DGdoINVl7jcT-khwuQVX3SIergCMY4K0Gh0XHdig; bili_ticket_expires=1694431497; PVID=1; CURRENT_BLACKGAP=0; SESSDATA=3b4a7ed3%2C1709724305%2C66975%2A92CjDJXj8_Zp-0FhLyrCFHDSmAYXibiDSAGxNk2HxcB7o3SgSV1c3akBZImvgEmrppqZ0SVjc5akZXTTlESE9zbU16TW5WOEEyQl84ZDF4YjczVGp0QmMycXlYY3g2WnpGd2hLNHRLNVBoMjkxVnVQdGJqOEdxaGpvMEU4bHRsd1pPb2VzMHlSYTZBIIEC; bili_jct=1ea1646f846f4a8110f0e446d08b6674; CURRENT_FNVAL=4048; fingerprint=afe9a51874119f1ce34b4c95148f1e32; sid=4nvns51l; buvid_fp=25E54027-80D1-B1E0-DB5B-7B2615931E6C60632infoc; buvid_fp_plain=undefined; rpdid=|(kmJYmkk~k)0J\'uYmRu~kJum',
    # 防盗链, 告诉服务器请求链接是从哪里跳转过来的 <不加视频不能保存>
    'Referer': 'https://www.bilibili.com/bangumi/play/ep249469?spm_id_from=333.337.0.0&from_spmid=666.25.episode.0',
    # 用户代理, 表示浏览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
# 请求链接
url = 'https://api.bilibili.com/pgc/view/web/season?ep_id=249469'
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取数据 获取响应的json数据 字典数据
json_data = response.json()
# 解析数据 -> 获取 aid cid ep_id title
lis = json_data['result']['episodes']
# for循环遍历, 提取列表里面的元素
for li in lis:
    # 键值对取值 -> 根据冒号左边的内容[键], 提取冒号右边的内容[值]
    aid = li['aid']
    cid = li['cid']
    ep_id = li['ep_id']
    title = li['share_copy'].replace(' ', '')
    # 视频/音频数据接口
    link = 'https://api.bilibili.com/pgc/player/web/v2/playurl'
    # 请求参数 --> 复制的内容
    data = {
        'support_multi_audio': 'true',
        'avid': aid,
        'cid': cid,
        'qn': '0',
        'fnver': '0',
        'fnval': '4048',
        'fourk': '1',
        'gaia_source': '',
        'from_client': 'BROWSER',
        'ep_id': ep_id,
        'session': '035c438c744f81aeea992f240c80714f',
        'drm_tech_type': '2',
    }
    #　发送请求获取数据
    link_data = requests.get(url=link, params=data, headers=headers).json()
    # 视频画面链接
    video_url = link_data['result']['video_info']['dash']['video'][0]['baseUrl']
    # 音频链接
    audio_url = link_data['result']['video_info']['dash']['audio'][0]['baseUrl']
    # 保存数据
    video_content = requests.get(url=video_url, headers=headers).content
    audio_content = requests.get(url=audio_url, headers=headers).content
    # 替换特殊字符
    title = re.sub(r'[\\/:*?"<>|]', '', title)
    # 文件路径 -> D:\自游\B站视频\B站番剧采集\video\
    # \ 转义字符 可以把含有特殊含义字符, 转义成除了本身字符以外, 不含有其他特殊意思
    with open('video\\' + title + '.mp3', mode='wb') as audio:
        audio.write(audio_content)
    with open('video\\' + title + '.mp4', mode='wb') as video:
        video.write(video_content)
    # 合并音频和视频 --> ffmpeg 软件
    cmd = f"ffmpeg -hide_banner -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental output\\{title}output.mp4"
    subprocess.run(cmd)
    print(video_url)
    print(audio_url)














