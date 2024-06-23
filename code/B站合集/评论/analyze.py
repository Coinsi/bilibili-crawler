import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':
    df = pd.read_csv('clean.csv', encoding='utf-8')

    df_mood = df.groupby('情感态度').size().sort_values(ascending=False)
    datas = list(zip(df_mood.index.to_list(), df_mood.to_list()))
    # print(datas)
    title = "植物大战僵尸杂交版'的相关评论的情感分析饼状图"
    pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    pie.add("", datas)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        legend_opts=opts.LegendOpts(pos_right="right")
    )
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}: {d}%"))
    pie.render('植物大战僵尸杂交版的相关评论.html')

    make_snapshot(snapshot, "植物大战僵尸杂交版的相关评论.html", "分析统计饼状图.png")