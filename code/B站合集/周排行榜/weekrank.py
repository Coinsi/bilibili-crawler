## 1 导入包
import pandas as pd
import requests  #发送请求
import time
url_dict = {i: f"https://api.bilibili.com/x/web-interface/popular/series/one?number={i}" for i in range(1, 273)}

headers = {

    "Cookie": "buvid3=4810C27F-B434-F23D-534A-0DB1F40F36FB54241infoc; b_nut=1717333054; b_lsid=296D32E9_18FD906D8F2; _uuid=33D3CB105-1779-2EFB-5D6F-51E10102DF4BC755753infoc; buvid_fp=f32397268898cb5bc2af8ac60338b226; enable_web_push=DISABLE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; home_feed_column=4; buvid4=CFAC93C4-7A4D-C365-0828-EFF68AAB9E0A58085-024060212-sOYgqIqMSBrEJm%2FCDmh4iA%3D%3D; header_theme_version=CLOSE; SESSDATA=9e7f18d6%2C1732885111%2C01e2c%2A62CjBxVHbF0ckeArpibOCmp3szp4bC8dABWo8za_jR06D0-RCZFMN5nv54mQktvQxK-h8SVlFYVlJjRXJVaDdHZktlVXF6ZzRrbGxzS19iank5YzlIeGl4ZE9WcHlGaERLbDItMDdVQjZnOTFVQ2o4a1N3QTZYTnY2UTVQZnptUzBUMWdYV2NpVlFBIIEC; bili_jct=c004867f150a4a81a6919fb022698827; DedeUserID=669002132; DedeUserID__ckMd5=bf5619506a92dc5c; sid=5ravg3ju; browser_resolution=450-582",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
all_data_df = pd.DataFrame()
for i in url_dict.items():
    url = i[1]  # url地址
    tab_name = i[0]  # tab页名称
    title_list = []
    play_cnt_list = []  # 播放数
    danmu_cnt_list = []  # 弹幕数
    coin_cnt_list = []  # 投币数
    like_cnt_list = []  # 点赞数
    share_cnt_list = []  # 分享数
    favorite_cnt_list = []  # 收藏数
    author_list = []

    video_url = []
    try:
        r = requests.get(url, headers=headers)
        print(r.status_code)
        #获取目标数据所在数据并转成字典类型
        json_data = r.json()
        list_data = json_data['data']['list']

        for data in list_data:
            title_list.append(data['title'])
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
        print('第{}期爬取成功'.format(tab_name))
    except Exception as e:
        print("爬取失败:{}".format(str(e)))
    #创建dataframe保存数据
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
          '期数':  tab_name ,
         })
    all_data_df = pd.concat([all_data_df, df], ignore_index=True)

    time.sleep(2)  # 每次爬取后暂停2秒，防止请求过于频繁
    #print(df.head())
    #将数据保存到本地
    # df.to_csv('第{}期.csv'.format(tab_name), index=False,encoding='utf_8_sig')  # utf_8_sig修复乱码问题
    # print('写入成功: ' + '第{}期.csv'.format(tab_name))

all_data_df.to_csv('总数据.csv', index=False, encoding='utf_8_sig')
print('所有数据写入成功: 总数据.csv')
