import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 4), dpi=200)
ax1 = fig.add_subplot()  # 构造绘图面板对象，逗号可省略
fig.subplots_adjust(wspace=0)

data_df = pd.read_csv("us_covid19_daily.csv")

# data_df = data_df.iloc[0:240, 0]
data_positive = data_df.positive.tolist()
data_positive_sort = sorted(data_positive)

data_day = data_df.date.tolist()
data_day_sort = sorted(data_day)

data_day_str = [str(i) for i in data_day_sort]
x = range(1, len(data_day_str)+1)
# print(x)
ax1.plot(x, data_positive_sort, color='gray')
# ax1.set_ylim([-500000, 7500000])
# plt.xticks(np.arange(250), labels=data_day_str, )
plt.xticks(fontsize=8)
plt.yticks([0., 1000000., 2000000., 3000000., 4000000., 5000000.,6000000., 7000000., 8000000.],
           ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
ax1.set_title('Number of pneumonia in COVID-19', weight='bold')
ax1.set_xlabel('Days')
ax1.set_ylabel('Positive(million)')
# print(ax1.get_yticks())
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.spines['left'].set_visible(True)
plt.show()



# print(data_day_sort, len(data_day_sort))
# print(data_positive_sort, len(data_positive_sort))
# print(len(data_day_str))

