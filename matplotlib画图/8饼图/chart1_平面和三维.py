import matplotlib.pyplot as plt

# 官网
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs') 第3个数据突出显示

fig1, (ax1, ax2) = plt.subplots(1, 2)  # 为了使用面向对象的方法实现这一点，我们将首先生成类的对象(或者称为实例)fig1, ax1这相当于我们画图的底板
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# autopct='%1.1f%%' -- 小数点前面的数字对结果没有任何影响，小数点后面的数字表示保留小数点几位，%%是指输出百分号。
# autopct='%1.1f%%'表示sizes在饼图中的显示格式
ax2.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle. 等宽高比确保饼图被绘制成一个圆

plt.show()


# 语雀
# labels = ['Java', 'C', 'Python', 'C++', 'C#', 'VB.net', 'Javascript', 'PHP', 'Other']
# sizes = [16.896, 15.773, 9.704, 5.574, 5.349, 5.287, 2.451, 2.405, 36.561]
# explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0)        # 第3个数据突出显示
#
# plt.axes(aspect=1)                             # 设置参数为1使饼图是圆的
# plt.pie(sizes, explode=explode, labels=labels, labeldistance=1.1,
#         autopct='%2.1f%%', shadow=True, startangle=90, pctdistance=0.7)
# plt.legend(loc='upper left', bbox_to_anchor=(-0.35, 1.1))  # 左上角放置图例
# plt.show()
