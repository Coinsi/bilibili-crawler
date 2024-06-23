from bilibili_api import video
import asyncio

# 实例化
v = video.VideoOnlineMonitor(bvid="BV1AV411x7Gs")

@v.on('ONLINE')
async def on_online_update(event):
    """
    在线人数更新
    """
    print(event)


@v.on('DANMAKU')
async def on_danmaku(event):
    """
    收到实时弹幕
    """
    print(event)

if __name__ == '__main__':
    # 主入口，v.connect() 为连接服务器
    asyncio.get_event_loop().run_until_complete(v.connect())