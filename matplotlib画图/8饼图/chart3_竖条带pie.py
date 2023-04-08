import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

# make figure and assign axis objects
# 构造底层面板对象(9, 5)是英寸，dpi参数指定绘图对象的分辨率，即每英寸多少个像素，默认值是80，本句中创建的图表窗口的宽度是9x80=720像素
fig = plt.figure(figsize=(8, 4), dpi=200)
ax1 = fig.add_subplot(1, 2, 1)  # 构造绘图面板对象，逗号可省略
ax2 = fig.add_subplot(122)
fig.subplots_adjust(wspace=0)

# pie chart parameters  # 画饼图
ratios = [.27, .56, .17]
labels = ['Approve', 'Disapprove', 'Undecided']
explode = [0.1, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * ratios[0]
ax1.pie(ratios, autopct='%1.1f%%', startangle=angle,
        labels=labels, explode=explode)

# bar chart parameters  # 画竖条图
xpos = 0
bottom = 0
ratios = [.33, .54, .07, .06]
width = .2
colors = [[.1, .3, .5], [.1, .3, .3], [.1, .3, .7], [.1, .3, .9]]

for j in range(len(ratios)):
    height = ratios[j]
    ax2.bar(xpos, height, width, bottom=bottom, color=colors[j])
    ypos = bottom + ax2.patches[j].get_height() / 2  # patches[j]从下往上第j块
    bottom += height
    ax2.text(xpos, ypos, "%d%%" % (ax2.patches[j].get_height() * 100),
             ha='center')

ax2.set_title('Age of approvers')
ax2.legend(('50-65', 'Over 65', '35-49', 'Under 35'))
ax2.axis('off')  # 擦去坐标轴
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
# get the wedge data
theta1, theta2 = ax1.patches[0].theta1, ax1.patches[0].theta2  # theta1扇形下边界theta2扇形上边界，逆时针
center, r = ax1.patches[0].center, ax1.patches[0].r
bar_height = sum([item.get_height() for item in ax2.patches])

# draw top connecting line 画上面那条线
x = r * np.cos(np.deg2rad(theta2)) + center[0]
y = r * np.sin(np.deg2rad(theta2)) + center[1]
# print("draw top connecting line:", x, y)
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
# print(ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# draw bottom connecting line 画下面那条线
x = r * np.cos(np.deg2rad(theta1)) + center[0]
y = r * np.sin(np.deg2rad(theta1)) + center[1]
# print("draw bottom connecting line:", x, y)
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)

plt.show()
