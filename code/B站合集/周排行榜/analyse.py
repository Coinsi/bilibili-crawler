import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':
    df = pd.read_csv("第272期.csv")  # 打开文件，使用参数df接收所有数据
    df_title = df['视频标题']  # 提取视频标题
    df_watch = df['播放数']  # 提取观看量
    df_dm = df['弹幕数']  # 提取弹幕数
    df_dz = df['点赞数']  # 提取点赞数
    df_tb = df['投币数']  # 提取投币数
    df_sc = df['收藏数']  # 提取收藏数
    df_zf = df['分享数']  # 提取转发数

    # 为所有参数各自新建一个空list
    Title = []
    Watch = []
    Dm = []
    Dz = []
    Tb = []
    Sc = []
    Zf = []

    # 将所有数据写入各自的list
    for element in df_title:
        Title.append(element)

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

    # 自定义bar1为一个Bar类型，并设置 图表主题/宽度/高度
    bar1 = Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE, width="4500px", height="1200px"))

    bar1.add_xaxis(Title)  # x轴参数为各个视频的名称

    # 设置图表标题
    bar1.set_global_opts(
        title_opts=opts.TitleOpts(title="b站第272期周榜数据统计柱状图", pos_left="50%", pos_top="5%"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))

    # 设置y轴参数
    # bar1.add_yaxis('播放量', Watch)
    bar1.add_yaxis('弹幕数', Dm)
    bar1.add_yaxis('点赞数', Dz)
    bar1.add_yaxis('投币数', Tb)
    bar1.add_yaxis('收藏数', Sc)
    bar1.add_yaxis('转发数', Zf)

    # 生成html文件
    bar1.render('b站第272期周榜数据统计柱状图.html')

    # 制作快照，这个代码会生成png图片，但是要安装其他模块（make_snaposhot模块/snapshot_selenium模块/snapshot模块）(其实截图就行了，可选）
    make_snapshot(snapshot, "b站第272期周榜数据统计柱状图.html", "b站第272期周榜数据统计柱状图.png")


