import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':
    df = pd.read_csv("video_info.csv")
    df_watch = df['播放数']
    df_dm = df['弹幕数']
    df_dz = df['点赞数']
    df_tb = df['投币数']
    df_sc = df['收藏数']
    df_zf = df['分享数']
    df_time = df['采集日期']
    Watch = []
    Dm = []
    Dz = []
    Tb = []
    Sc = []
    Zf = []
    Sj = []
    for element in df_watch:
        Watch.append(element)
    for element in df_dm:
        Dm.append(element)
    for element in df_dz:
        Dz.append(element)
    for element in df_tb:
        Tb.append(element)
    for element in df_sc:
        Sc.append(element)
    for element in df_zf:
        Zf.append(element)
    for element in df_time:
        Sj.append(element)

    line = Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    line.add_xaxis(Sj)
    # line.add_yaxis('播放量', Watch)
    line.add_yaxis('弹幕数', Dm)
    line.add_yaxis('点赞数', Dz)
    line.add_yaxis('投币数', Tb)
    line.add_yaxis('收藏数', Sc)
    line.add_yaxis('转发数', Zf)

    line.set_global_opts(
        title_opts=opts.TitleOpts(title='植物大战僵尸杂交版视频播放', pos_left="25%", pos_top="6%"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="时间"),
        yaxis_opts=opts.AxisOpts(name="参数")
    )

    line.render('植物大战僵尸杂交版视频播放.html')
    make_snapshot(snapshot, '植物大战僵尸杂交版视频播放.html',
                  '植物大战僵尸杂交版视频播放.png')

