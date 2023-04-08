import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['2006', '2007', '2008', '2009', '2010', '2011',
          '2012', '2013', '2014', '2015', '2016', '2017']
Chinese_exported_to_US = [288, 321, 338, 296, 365, 399, 426, 440, 468, 483, 463, 461]
US_exported_to_Chinese = [54, 63, 70, 70, 92, 104, 111, 122, 124, 116, 116, 117]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Chinese_exported_to_US, width, label='Chinese exported to US')
rects2 = ax.bar(x + width/2, US_exported_to_Chinese, width, label='US exported to Chinese')
ax.tick_params(left=True, bottom=False, direction='in')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper left')
ax.set_title("China-US goods trade", weight='bold', fontsize=14)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(2.5, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
