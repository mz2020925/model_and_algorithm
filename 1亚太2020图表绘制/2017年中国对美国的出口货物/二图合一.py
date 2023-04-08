import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 8), dpi=200)
ax1 = fig.add_subplot(2, 1, 1)  # 构造绘图面板对象，逗号可省略
ax2 = fig.add_subplot(2,1,2)

# fig, ax11 = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))
recipe = ["Mechanical products: 29.67%",
          "Electronic products: 27.30%",
          "Textile: 18.60%",
          "Chemicals: 7.71%",
          "Metal products: 5.16%",
          "Agricultural products: 4.95%",
          "Automobiles and parts: 3.58%",
          "Stone: 2.19",
          "Resources and minerals: 0.27"]


# data = [225, 90, 50, 60, 100, 5]
total = 4800
data = [1424.16, 1310.4, 892.80, 370.08, 247.68, 237.60, 171.84, 105.12, 12.96]
wedges, texts = ax1.pie(data, wedgeprops=dict(width=0.5), startangle=10)

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
    ax1.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.2*y),
                horizontalalignment=horizontalalignment, **kw)

ax1.set_title("China exported goods to the US in 2017", weight='bold', loc='center', y=1)




# fig, ax2 = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))
recipe = ["Mechanical products: 15.69%",
          "Electronic products: 8.75%",
          "Textile: 1.58%",
          "Ore: 1.77%",  # 矿石
          "Metal products: 4.10%",
          "Agricultural products: 19.38%",
          "Automobiles and parts: 18.27%",
          "Resources and minerals: 6.79",
          "Others: 11.12%"]
# data = [225, 90, 50, 60, 100, 5]
total = 1320
data = [207.12, 115.50, 20.86, 23.36, 54.12, 255.816, 241.164, 89.628, 146.784]
wedges, texts = ax2.pie(data, wedgeprops=dict(width=0.5), startangle=-100)

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
    ax2.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.2*y),
                horizontalalignment=horizontalalignment, **kw)

ax2.set_title("US exported goods to the China in 2017", weight='bold', loc='center', y=1)


plt.show()
