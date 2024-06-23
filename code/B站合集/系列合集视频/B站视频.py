"""
[课程内容]: 掌握Python技巧，轻松抓取B站系列合集视频

[授课老师]: 青灯教育-自游 [上课时间]: 20:05  可以点歌 可以问问题

[环境使用]:
    Python 3.8
    Pycharm
    ffmpeg  <需要设置环境变量> 软件的使用 合成视频和音频

[模块使用]:
    import requests >>> pip install requests
    import subprocess

win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加落落老师微信

有基础同学 -> 1
零基础同学 -> 0

对于本节课任何一样代码, 不理解意思 都可以问

爬虫基本流程:

一. 数据来源分析
    1. 明确需求
        - 明确采集的网站以及数据内容
            网址: https://www.bilibili.com/video/BV1cP411v7NR/
            数据: 集合视频内容
    2. 抓包分析
        通过开发者工具进行数据包分析, 分析数据可以在那个链接能够得到
        - F12 打开开发者工具
        - 刷新网页
        - 在开发者工具里面搜索:
            https://api.bilibili.com/x/player/wbi/playurl

数据包: https://api.bilibili.com/x/web-interface/wbi/view/detail
    获取CID参数
数据包: https://api.bilibili.com/x/player/wbi/playurl
    主要改变参数: CID --> 视频ID
目的: 视频信息 <音频链接/音频链接>

二. 代码实现步骤

第一次请求 --> 视频CID / 视频标题
    1. 发送请求
        请求链接地址: https://api.bilibili.com/x/web-interface/wbi/view/detail
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取数据
        视频CID / 视频标题

第二次请求 --> 视频链接 / 音频链接
    4. 发送请求
        请求链接地址: https://api.bilibili.com/x/player/wbi/playurl
            需要传入cid参数 <视频ID参数>
    5. 获取数据, 获取服务器返回响应数据
    6. 解析数据, 提取数据
        视频链接 / 音频链接

    4. 保存数据, 把视频和音频保存本地, 合并一个完整视频内容

想要付费学习的同学 --> 6
    一个月300多的学费, 可以学

系统课程教学的内容:
    核心编程 爬虫开发 数据分析 网站开发 人工智能 自动化办公

加婧琪老师微信: python1018

1. 担心是否能够学会
    你能给我保证:
        按时听课: 坚持学习
        按时完成作业: 多敲多练
        认真学习态度: 不懂多问
    我能给你保证, 你能够学会掌握....

2. 担心是否能够技术变现 < 外包兼职 / 就业工作 >
    外包兼职:
        1. 提供外包接单群
        2. 提供外包接单渠道
        3. 提供外包问题解答

    就业工作:
        1. 提供简历修改和制作
        2. 企业面试试题
        3. 企业面试技巧
        4. 企业开发问题解答

自游老师保障:
    1. 你学完爬虫之后, 想要接单, 你可以直接找我
        我可以一对一提供外包订单给你
    2. 掌握80%左右知识点, 我可以直接给你内推青灯上班
        薪资待遇: 8000-15000左右

课程服务:
    - 直播授课
        一周三节课, 晚上20:00-22:00直播授课
    - 课后 录播 源码 笔记 文档 软件工具 作业 考核
    - 老师解答辅导
        文字 语音 远程操作
    - 班主任老师监督学习, 电话通知听课
    - 免费重修 <小白 0基础福音>
        一遍不扎实, 可以学两遍
        两遍不扎实, 可以学三遍
        三遍不扎实, 基本不可能 --> 课程资料 你可以一直观看学习
    - 外包指导
    - 就业指导
    - 培训合同
    - 发票
    - 毕业证书
    ...

课程学费:
    核心编程: 2260 21
        上: 12大节课 2.5个小时左右
        下: 9大节课
    爬虫开发: 2980
        直播: 20大节课
        三大专题录播:
            JS专题: 26小节
            反爬专题: 34小节
            框架专题: 21小节
    数据分析: 2180 --> 15节
    网站开发: 2980 --> 21节
    自动化办公: 1680 --> 15节
    人工智能: 2680 --> 15节

总计学费: 14760

新班10号上课, 今天第二节课, 你报名可以跟上新班学习

加婧琪老师微信: python1018

    预定300元学费, 可以直接进班学习
    一. 高薪就业课程:
        核心编程 爬虫开发 数据分析 网站开发 人工智能 自动化办公
            原学费: 14760 --> 减免到 8580
        申请分期免息学习<0利息0手续费>: 根据个人经济条件选择
            3/6/9/12/18/24个月支付学费
        最低每个月学费 -> 357.5元
    二. 外包兼职课程:
        核心编程 爬虫开发 数据分析
            原学费: 7420 --> 减免到 6380
        申请分期免息学习<0利息0手续费>: 根据个人经济条件选择
            3/6/9/12/18个月支付学费
        最低每个月学费 -> 354元

接外包水平:
    正常2个月左右时间, 学完爬虫之后可以接单
比如今天报名课程学习, 就预定300元学费, 进班学习
    9月12号, 支付一个月学费 354元
    10月12号, 支付二个月学费 354元

直接来找我, 我提供外包订单给你
    外包订单价格: 200-5000不等
按照200一个外包, 相当于一个月接1-2个左右外包 学费就OK了


岗位:
    爬虫工程师
    开发工程师
    全栈开发
    数据分析师
    算法工程师

薪资:
    应届生: 8000-15000左右 大部分 10000上下浮动
    1-3年: 15000-25000左右 大部分 15000上下浮动
    3-5年: 25000-35000左右 大部分 20000上下浮动

开发经验: 是指用实现相关案例项目所积累的经验
    考核: 个人能力 有没有技术是否扎实
工作经验: 是指从事相关工作所积累经验
    入职工作, 负责开发功能实现 业务需求....
工作经历: 是指从事工作的经验

比如:
    外包: 采集二手房源数据 这个不算开发经验
    外包: 通过分布式大规模二手房源数据采集 可以算开发经验

相对而言没有反爬, 难度不大, 不要写简历里面

    系统课程: 教你企业项目案例

对于报名课程同学:
    1. 在学习的过程中, 遇到任何不懂的地方一定要多问老师, 不要觉得不好意思
        <为了让你学的更好, 学的更扎实>
    2. 平时有任何事情, 可以找任何一个老师进行反馈
        <为了让我们服务做的更好>

"""
import os

# 数据请求模块
import requests
# 子进程
import subprocess
"""
第一次请求 --> 视频CID / 视频标题
    1. 发送请求, 模拟浏览器对于url地址发送请求
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取cid 标题
"""
# 模拟浏览器
headers = {
    # Cookie 用户信息, 常用于检测是否登陆账号 <复制登陆的cookie>
    "Cookie": "buvid3=FCAA2D12-CCF2-8308-7BA8-84DE67F1E52A23502infoc; b_nut=1688827123; _uuid=71FD3619-3F104-35A6-29A5-A537FB747D31023847infoc; buvid_fp=98cc770427c4156eee53192bfc1ff4e9; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; is-2022-channel=1; rpdid=|(kmJY|k)k~l0J'uY)))k~JYm; buvid4=2B0B9D22-8882-4579-1CD3-D8AE5C23184F25066-023070822-8rgUfw%2FZCRVfcf5dliz70g%3D%3D; DedeUserID=406732493; DedeUserID__ckMd5=48c43aca436bb747; CURRENT_FNVAL=4048; LIVE_BUVID=AUTO1616906202637395; i-wanna-go-back=-1; b_ut=5; PVID=1; bp_video_offset_406732493=828221272658804761; b_lsid=3EB111078_189E97DC529; home_feed_column=4; browser_resolution=1255-604; SESSDATA=05e29841%2C1707391483%2C6567b%2A82pfn_BngynKjM2iB6p2Sr2kv2dwrkM1wRq8xI8lzDuB9oePMPLQxBi2YJfr5HKhm-e_BgkgAAXQA; bili_jct=5321908aecd3b15a9aa45b8c6d4f5997; bili_ticket=eyJhbGciOiJFUzM4NCIsImtpZCI6ImVjMDIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTIwOTg3MDgsImlhdCI6MTY5MTgzOTUwOCwicGx0IjotMX0.KBnp-o4LzTnRGwRc5rKHTQqq--6dS6aH5nGVIMrbDmiJLc9rrGWsgWYE6itspHzym8wUNkuJhAQKqKQLIiGB0uEB9bsmtlSWjL_iI7RcPXDZ6H205aIU2DbuMBeTlC1B; bili_ticket_expires=1692098708; sid=5n988cm3",
    # Referer 防盗链, 告诉服务器请求链接是从哪里跳转过来
    "Referer":"https://www.bilibili.com/",
    # User-Agent 用户代理, 表示浏览器基本身份信息
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# 请求链接
url = 'https://api.bilibili.com/x/web-interface/wbi/view/detail?platform=web&bvid=BV1cP411v7NR&aid=315578832&need_operation_card=1&web_rm_repeat=1&need_elec=1&out_referer=https%3A%2F%2Fspace.bilibili.com%2F1424001422%3Fspm_id_from%3D333.337.0.0&page_no=2&p=2&web_location=1446382&w_rid=3d78901ec7653c35b609fbb269116b8c&wts=1691842397'
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取响应json数据 --> 字典数据类型 {}
json_data = response.json()
# 字典取值, 提取信息内容
pages = json_data['data']['View']['pages']
# for循环遍历, 提取列表里面元素
for page in pages: # page 定义变量名
    # 提取cid
    cid = page['cid']
    # 提取标题
    title = page['part']
    """
    第二次请求 --> 视频链接 / 音频链接
    """
    # 字符串格式化方法 cid=a --> f'123{cid}567' -> 123a567
    link = f'https://api.bilibili.com/x/player/wbi/playurl?avid=315578832&bvid=BV1cP411v7NR&cid={cid}&qn=0&fnver=0&fnval=4048&fourk=1&gaia_source=&from_client=BROWSER&session=a8c0ca08931d78cec3186c98d76985b2&web_location=1315873&w_rid=fc29e9773716e368c787e3264426cbd9&wts=1691842396'
    # 发送请求
    link_data = requests.get(url=link, headers=headers).json()
    # 提取视频链接
    video_url = link_data['data']['dash']['video'][0]['baseUrl']
    # 提取音频链接
    audio_url = link_data['data']['dash']['audio'][0]['baseUrl']
    video_content = requests.get(url=video_url, headers=headers).content
    audio_content = requests.get(url=audio_url, headers=headers).content
    with open('video\\' + title + '.mp3', mode='wb') as audio:
        audio.write(audio_content)
    with open('video\\' + title + '.mp4', mode='wb') as video:
        video.write(video_content)
    cmd = f"ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4"
    subprocess.run(cmd)
    os.remove(f"video\\{title}.mp4")
    os.remove(f"video\\{title}.mp3")
    print(cid, title)
    print(video_url)
    print(audio_url)
