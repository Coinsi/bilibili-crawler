import asyncio
import csv
from datetime import datetime
from bilibili_api import video, Credential
#
# SESSDATA = ""
# BILI_JCT = ""
# BUVID3 = ""

async def main():
    # 实例化 Credential 类
    # credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
    # 实例化 Video 类
    v = video.Video(bvid="BV1ay411h74i")
    # 获取视频信息
    data = await v.get_info()
# 获取当前日期
    current_date = datetime.now().strftime('%Y-%m-%d')  # 格式化日期为年-月-日形式

# 准备写入CSV的数据行，新增日期字段
    video_info = [
        data["title"],  # 视频标题
        f"https://www.bilibili.com/video/{data['bvid']}",  # 视频地址
        data["owner"]["name"],  # 作者
        data["stat"]["view"],  # 播放数
        data["stat"]["danmaku"],  # 弹幕数
        data["stat"]["coin"],  # 投币数
        data["stat"]["like"],  # 点赞数
        data["stat"]["share"],  # 分享数
        data["stat"]["favorite"],  # 收藏数
        current_date  # 新增的当前日期字段
]

    # 更新CSV文件的表头
    fieldnames = ['视频标题', '视频地址', '作者', '播放数', '弹幕数', '投币数', '点赞数', '分享数', '收藏数', '采集日期']

    # 写入CSV文件
    with open('video_info.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:  # 使用'a'模式追加写入
        writer = csv.writer(csvfile)

    # 因为表头只在文件为空时写入，所以这里先检查文件是否为空
        if csvfile.tell() == 0:  # 如果文件是空的，写入表头
            writer.writerow(fieldnames)

        # 写入数据行
        writer.writerow(video_info)

print("数据已成功写入CSV文件，包含当前日期。")
if __name__ == '__main__':
    # 主入口
    asyncio.get_event_loop().run_until_complete(main())