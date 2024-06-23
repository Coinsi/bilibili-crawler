from bilibili_api import hot, sync
import pandas as pd

print(sync(hot.get_hot_videos()))

title_list = []
play_cnt_list = []  # 播放数
danmu_cnt_list = []  # 弹幕数
coin_cnt_list = []  # 投币数
like_cnt_list = []  # 点赞数
share_cnt_list = []  # 分享数
favorite_cnt_list = []  # 收藏数
author_list = []
video_url = []

for data in sync(hot.get_hot_videos()):
    title_list.append(data['list']['title'])
    play_cnt_list.append(data['stat']['view'])
    danmu_cnt_list.append(data['stat']['danmaku'])
    coin_cnt_list.append(data['stat']['coin'])
    like_cnt_list.append(data['stat']['like'])
    # dislike_cnt_list.append(data['stat']['dislike'])
    share_cnt_list.append(data['stat']['share'])
    favorite_cnt_list.append(data['stat']['favorite'])
    author_list.append(data['owner']['name'])
    # score_list.append(data['score'])
    video_url.append('https://www.bilibili.com/video/' + data['bvid'])
    # print('*' * 10)

    df = pd.DataFrame(
        {'视频标题': title_list,
         '视频地址': video_url,
         '作者': author_list,
         '播放数': play_cnt_list,
         '弹幕数': danmu_cnt_list,
         '投币数': coin_cnt_list,
         '点赞数': like_cnt_list,
         '分享数': share_cnt_list,
         '收藏数': favorite_cnt_list,
         })
    df.to_csv('数据.csv', index=False,encoding='utf_8_sig')  # utf_8_sig修复乱码问题