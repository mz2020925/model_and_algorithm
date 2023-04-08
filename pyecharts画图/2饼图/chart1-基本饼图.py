from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

angle = 360
key = ["中国", "其他", "荷兰", "德国", "韩国", "日本", "美国"]
values = [64, 10, 1, 2, 5, 7, 11]
c = (
    Pie()
        .add("", [list(z) for z in zip(key, values)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
        .render("pie_base.html")
)


