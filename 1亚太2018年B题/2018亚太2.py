import pandas as pd
import os
import xlrd
import xlwt
import matplotlib.pyplot as plt

dir2015 = os.listdir("2015")
dir2016 = os.listdir("2016")
dir2017 = os.listdir("2017")
dir2018 = os.listdir("2018")


def data_per_month(dir_filename):
    xlsx = xlrd.open_workbook(dir_filename)
    sheet1 = xlsx.sheets()[0]  # 获得第1张sheet，索引从0开始
    sheet1_nrows = sheet1.nrows  # 获得行数
    sheet1_name = sheet1.name  # 获得名称
    # sheet1_cols = sheet1.ncols  # 获得列数
    # print(sheet1_name)
    # print(sheet1_nrows)
    # print(sheet1_cols)
    list_current = []
    for row in range(3, sheet1_nrows-1):
        list_current.append(sheet1.row_values(row))
    # print(list_current)
    return list_current


def data_per_year(dir_name, dir_list):
    list_per_year = []
    for i in dir_list:
        list_per_year = list_per_year + data_per_month(dir_name + '\\' + i)
    return list_per_year


# list_2015 = data_per_year('2015')
# list_2016 = data_per_year('2016')
# list_2017 = data_per_year('2017')
# list_2018 = data_per_year('2018')
# # print(list_2015)
# df_2015 = pd.DataFrame(list_2015, columns=['Serial number', 'Sector', 'Total demand (Pers.)', 'Junior middle school',
#                                            'Senior middle school', 'Technical secondary school', 'Junior college',
#                                            "Bachelor's degree", "Master's degree", "Doctor's degree", 'MBA',
#                                            'Unlimited'])
# # pd.set_option('display.max_columns', None)  # 显示所有列
# # pd.set_option('display.max_rows', None)  # 显示所有行
# # pd.set_option('display.width', None)  # 显示宽度是无限
# df_2015.set_index(['Serial number'], inplace=True)  # inplace=True表示对原dataframe进行修改，不加的话必须赋值给另一个dataframe类型的数据
# # df_2015.reset_index()
# print(df_2015)


def dataframe_year(dirname, dirlist):
    list_year = data_per_year(dirname, dirlist)
    df_year = pd.DataFrame(list_year,
                           columns=['Serial number', 'Sector', 'Total demand (Pers.)', 'Junior middle school',
                                    'Senior middle school', 'Technical secondary school', 'Junior college',
                                    "Bachelor's degree", "Master's degree", "Doctor's degree", 'MBA',
                                    'Unlimited'])
    # df_year.set_index(['Serial number'], inplace=True)  # inplace=True表示对原dataframe进行修改，不加的话必须赋值给另一个dataframe类型的数据
    # df_2015.reset_index()
    return df_year


df_2015 = dataframe_year('2015', dir2015)
df_2016 = dataframe_year('2016', dir2016)
df_2017 = dataframe_year('2017', dir2016)
df_2018 = dataframe_year('2018', dir2018)


# y_list = [24641, 29957, 25581, 15767]
# x_list = [1, 2, 3, 4]
# plt.plot(x_list, y_list, color="r", marker='o', linewidth=2.5, linestyle="-", label="cos(x)")
# plt.legend(loc='lower right')                           # 设置线条名显示位置为右下角
# plt.xlabel(u'x(弧度)', fontproperties="SimHei")        # 加x轴标签，指定中文字体
# plt.ylabel(u'y', fontproperties="SimHei")              # 加y轴标签
#
# plt.show()












