import pyecharts.options as opts
from pyecharts.charts import Line

xaxis_data = ['50', '100', '150', '250', '300', '350', '400', '600']


y_axis = [87, 188, 447, 507, 599, 716, 707, 997]

print(len(xaxis_data), len(y_axis))
c = (
    Line()
        .add_xaxis(xaxis_data)
        .add_yaxis("专利数", y_axis, is_smooth=True)
        # .add_yaxis("中国", china_axis)
        # .add_yaxis("韩国", hg_axis)
        # .add_yaxis("美国", us_axis)
        # .add_yaxis("日本", rb_axis)
        # .add_yaxis("广东", gd_axis)
        .set_global_opts(title_opts=opts.TitleOpts(title="物联网关键技术在中国申请专利技术\n生命周期分析"))
        .render("line_base.html")
)
