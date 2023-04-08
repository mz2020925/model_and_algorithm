import xlrd
import pandas as pd
import matplotlib.pyplot as plt

filename = "APMCM数据.xlsx"
df_data = pd.read_excel(filename)
Year = df_data.iloc[:, 0].tolist()
GDP = df_data.iloc[:, 1].tolist()
Environment = df_data.iloc[:, 2].tolist()
Infrastructure = df_data.iloc[:, 3].tolist()  # 基础设施
Education = df_data.iloc[:, 4].tolist()
Trade = df_data.iloc[:, 5].tolist()
International_students = df_data.iloc[:, 6].tolist()
Taxation = df_data.iloc[:, 7].tolist()  # 税收
Population = df_data.iloc[:, 8].tolist()
Number_of_unemployed = df_data.iloc[:, 9].tolist()
Medical_investment = df_data.iloc[:, 10].tolist()
print(Year)
print(GDP)
print(Environment)
print(Infrastructure)
print(Education)
print(Trade)
print(International_students)
print(Taxation)
print(Population)
print(Number_of_unemployed)
print(Medical_investment)


# data from United Nations World Population Prospects (Revision 2019)
# https://population.un.org/wpp/, license: CC BY 3.0 IGO
Year = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
population_by_continent = {
    # 'GDP': [13.04, 13.81, 14.45, 14.71, 14.45, 14.99, 15.54, 16.2, 16.78, 17.52, 18.22, 18.71, 19.49, 20.53, 21.37],
    # 'Environment': [27.68, 27.98, 33.06, 31.47, 46.27, 51.41, 41.36, 41.49, 34.56, 35.24, 34.23, 38.59, 37.33, 35.51, 37.85],
    'Infrastructure\n(billion)': [1.14, 1.23, 1.22, 1.24, 1.29, 1.38, 1.46, 1.74, 1.07, 1.68, 1.57, 1.27, 1.3, 1.41, 1.38],
    'Education\n(trillion)': [0.715, 1.0, 0.671, 0.686, 0.399, 0.63, 0.881, 0.406, 0.399, 0.553, 0.881, 0.771, 1.154, 0.702, 0.812],
    # 'Trade': [41192.01, 53673.01, 62936.89, 69732.84, 69496.68, 91911.08, 104121.52, 110516.62, 121746.19, 123657.21, 115873.36, 115594.79, 129997.22, 120289.29, 106447.25],
    # 'International_students': [517764, 524337, 548559, 572914, 600324, 635674, 679338, 724725, 780055, 854639, 896341, 903127, 891330, 872214, 851957],
    'Taxation\n(trillion)': [2.3393759999999997, 2.572803, 2.6920349999999997, 2.616909, 2.26865, 2.468853, 2.59518, 2.72322, 3.166386, 3.32004, 3.4763759999999997, 3.491286, 3.8122439999999997, 3.53116, 3.639311],
    'Population\n(a hundred million)': [2.96, 2.98, 3.01, 3.04, 3.07, 3.09, 3.12, 3.14, 3.16, 3.19, 3.21, 3.23, 3.26, 3.27, 3.28],
    'Medical investment\n(trillion)': [2.1, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0],
    'Number of unemployed\n(a hundred million)': [0.15095999999999998, 0.137676, 0.139062, 0.175712, 0.284589, 0.29664, 0.27924, 0.253398, 0.23384, 0.19777999999999998, 0.17013, 0.157301, 0.14181, 0.12753, 0.12037600000000001]
}
fig = plt.figure(figsize=(8, 4), dpi=200)
ax = fig.add_subplot(1, 4, (1,3))  # 构造绘图面板对象，逗号可省略
ax.stackplot(Year, population_by_continent.values(),
             labels=population_by_continent.keys())

# ax.legend(loc='upper left')

ax.set_title('American investment in various fields', weight='bold')
ax.set_xlabel('Year')
ax.set_ylabel('Capital investment')
ax.tick_params(bottom=True, left=True, direction='in', )
plt.xticks(rotation=45)
ax.text(6, 16.5, "GDP")
# with open("美国GDP总量.txt", 'r', encoding='utf-8') as data:
#     print([line.strip() for line in data])







import matplotlib.pyplot as plt
import pylab as pyb

years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
percent = [2.5, 2.4, 2.2, 3.0, 2.7, 2.1, 1.3, 2.9, 1.5, 2.6, 2.4, -5.0, -31.7, 33.1]
GDP = [13.04, 13.81, 14.45, 14.71, 14.45, 14.99, 15.54, 16.2, 16.78, 17.52, 18.22, 18.71, 19.49, 20.53, 21.37]


# fig = plt.figure(figsize=(8, 5))
# ax1 = fig.add_subplot()  # 构造绘图面板对象，逗号可省略

# fig.subplots_adjust(wspace=0)

# ax.tick_params(bottom='off', left='off', direction='in')
result = ax.plot(years, GDP, color='black', linewidth=2, alpha=0.9, linestyle='-')
ax.legend()
# plt.grid(axis='y', alpha=0.4, linewidth=0.5)
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(True)
# ax.spines['left'].set_visible(True)
# ax.set_title('GDP of the United States', weight='bold')
# ax.set_xlabel('Year', fontsize=12)
# ax.set_ylabel('GDP(trillion)', fontsize=12)
# plt.xticks(fontsize=10, rotation=0)
ax.legend(loc=2, bbox_to_anchor=(1.01, 1.0), borderaxespad=0., fontsize=8)  # 设置ax4中legend的位置，将其放在图外

plt.show()



