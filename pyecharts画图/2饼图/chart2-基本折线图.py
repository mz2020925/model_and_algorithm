import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
import random

xaxis_data = ['1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
global_axis = [150, 160, 200, 190, 245, 295, 270, 343, 370, 480, 260,80]
china_axis = [5, 10, 20, 30, 30, 35, 30, 43, 80, 150, 160,70]
us_axis = [5, 15, 30, 57, 55, 60, 70, 90, 80, 100, 60,50]
rb_axis = [5, 10, 20, 30, 35, 40, 50, 60, 48, 70, 38,20]
hg_axis = [0, 0, 0, 0, 0, 5, 10, 15, 10, 20, 30, 10]

print(len(xaxis_data), len(china_axis))
c = (
    Line()
        .add_xaxis(xaxis_data)
        .add_yaxis("全球", global_axis)
        .add_yaxis("中国", china_axis)
        .add_yaxis("韩国", hg_axis)
        .add_yaxis("美国", us_axis)
        # .add_yaxis("日本", rb_axis)
        # .add_yaxis("广东", gd_axis)
        .set_global_opts(title_opts=opts.TitleOpts(title="智能交通技术原创国\n历年专利申请量分布"))
        .render("line_base.html")
)

# import pyecharts.options as opts
# from pyecharts.charts import Line
# from pyecharts.faker import Faker
#
# c = (
#     Line()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", Faker.values())
#     .add_yaxis("商家B", Faker.values())
#     .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
#     .render("line_base.html")
# )
