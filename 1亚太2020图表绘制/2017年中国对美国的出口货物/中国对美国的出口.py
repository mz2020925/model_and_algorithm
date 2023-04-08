import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))


recipe = ["Mechanical products: 29.67%",
          "Electronic products: 27.30%",
          "Textile: 18.60%",
          "Chemicals: 7.71%",
          "Metal products: 5.16%",
          "Agricultural products: 4.95%",
          "Automobiles and parts: 3.58%",
          # "Stone: 2.19",
          # "Resources and minerals: 0.27"
          ]


# data = [225, 90, 50, 60, 100, 5]
total = 4800
data = [1424.16, 1310.4, 892.80, 370.08, 247.68, 237.60, 171.84]
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=10)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

# 代码看不懂
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))  # 角度转弧度
    x = np.cos(np.deg2rad(ang))  # 角度转弧度
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]  # np.sign(x)，x>0函数值=1，x<0函数值=-1，x=0函数值=0
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.2*y),
                horizontalalignment=horizontalalignment, **kw)

ax.set_title("China exported goods to the US in 2017", weight='bold', loc='center', y=1)

plt.show()




# recipe = ["机械类: 29.67%",
#           "电子产品: 27.30%",
#           "纺织品: 18.60%",
#           "化工品: 7.71%",
#           "Metal products: 5.16%",
#           "农产品: 4.95%",
#           "汽车和零部件: 3.58%",
#           "石头: 2.19",
#           "资源和矿物: 0.27"]
# print(dict([tuple(i.strip().replace('%', '').split(":")) for i in recipe]))
# dict_test = dict([tuple(i.strip().replace('%', '').split(":")) for i in recipe])
# print([float(i)/100 for i in dict_test.values()])
# list2 = [float(i)/100 for i in dict_test.values()]
# print([i * 4800 for i in list2])
# print(sum([float(i)/100 for i in dict_test.values()]))