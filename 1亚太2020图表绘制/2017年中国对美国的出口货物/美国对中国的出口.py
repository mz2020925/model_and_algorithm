import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))


recipe = ["Mechanical products: 15.69%",
          "Electronic products: 8.75%",
          "Textile: 1.58%",
          # "Ore: 1.77%",  # 矿石
          "Metal products: 4.10%",
          "Agricultural products: 19.38%",
          "Automobiles and parts: 18.27%",
          "Resources and minerals: 6.79",
          "Others: 11.12%"]


# data = [225, 90, 50, 60, 100, 5]
total = 1320
data = [207.12, 115.50, 20.86,  54.12, 255.816, 241.164, 89.628, 146.784]
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-100)

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

ax.set_title("US exported goods to the China in 2017", weight='bold', loc='center', y=1)

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

