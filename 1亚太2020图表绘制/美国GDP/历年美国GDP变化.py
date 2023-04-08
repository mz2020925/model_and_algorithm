# with open("美国GDP总量.txt", 'r', encoding='utf-8') as data:
#     print([line.strip() for line in data])

import matplotlib.pyplot as plt
import pylab as pyb

years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
percent = [2.5, 2.4, 2.2, 3.0, 2.7, 2.1, 1.3, 2.9, 1.5, 2.6, 2.4, -5.0, -31.7, 33.1]
GDP = [13.04, 13.81, 14.45, 14.71, 14.45, 14.99, 15.54, 16.2, 16.78, 17.52, 18.22, 18.71, 19.49, 20.53, 21.37]


fig = plt.figure(figsize=(8, 5))
ax1 = fig.add_subplot()  # 构造绘图面板对象，逗号可省略

# fig.subplots_adjust(wspace=0)

ax1.tick_params(bottom='off', left='off', direction='in')
result = ax1.plot(years, GDP, color='#DF7401', linewidth=2, alpha=0.9)
plt.grid(axis='y', alpha=0.4, linewidth=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.spines['left'].set_visible(True)
ax1.set_title('GDP of the United States', weight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('GDP(trillion)', fontsize=12)
plt.xticks(fontsize=10, rotation=0)

plt.show()
