import pylab as pyb
import matplotlib.pyplot as plt


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax1.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2.5),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', fontsize=8)
        else:
            ax1.annotate('{}'.format(height),
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         xytext=(0, -6.5),  # 3 points vertical offset
                         textcoords="offset points",
                         ha='center', fontsize=8)


# with open("test.txt", 'r', encoding='utf-8') as data:
#     data_string = data.read()
#     print(data_string.split('\n'))


years = ['2017.2', '2017.3', '2017.4', '2018.1', '2018.2', '2018.3', '2018.4', '2019.1', '2019.2', '2019.3', '2019.4', '2020.1', '2020.2', '2020.3']
percent = [2.5, 2.4, 2.2, 3.0, 2.7, 2.1, 1.3, 2.9, 1.5, 2.6, 2.4, -5.0, -31.7, 33.1]

fig = plt.figure()
ax1 = fig.add_subplot()  # 构造绘图面板对象，逗号可省略
pyb.tick_params(bottom='off', left='off', direction='in')
# fig.subplots_adjust(wspace=0)


result = ax1.bar(years, percent, color='chocolate', linewidth=4)
plt.xticks(fontsize=10, rotation=30)
plt.axhline(0, linestyle='-', color='gray', linewidth=0.8, alpha=0.5)  # 绘制水平线y=0，x轴
# plt.axvline(0, linestyle='--', color='black', linewidth=1)  # 绘制垂直线x=0，y轴
# ax1.set_title('Percent change from preceding quarter', weight='bold')
ax1.set_xlabel('Quarter')
ax1.set_ylabel('Rate of growth(%)')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.spines['left'].set_visible(True)
autolabel(result)
plt.show()






