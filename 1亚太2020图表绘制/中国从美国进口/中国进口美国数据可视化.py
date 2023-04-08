import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 4), subplot_kw=dict(aspect="equal"))



recipe = ["Animal and plant products: 17.67%",
          "Food: 1.61%",
          "Chemical products: 25.22%",
          "Clothing products: 5.89%",
          "Metal products: 2.73%",
          "High-tech products: 46.03%",
          "Others: 0.85%"]

# data = [225, 90, 50, 60, 100, 5]
data = [2200972.2, 200572.7, 3141028.7, 733920.2, 340294.2, 5733462.3, 105405.8]
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-45)

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

ax.set_title("China imported goods from the US in October", weight='bold', loc='center', y=1)

plt.show()
