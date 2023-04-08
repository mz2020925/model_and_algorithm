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
        list1 = sheet1.row_values(row)
        print(list1)
        list1 = list1.insert(0,'zxc')
        print(list1)
        # list1 = sheet1.row_values(row).insert(0, sheet1_name)
        list_current.append(sheet1.row_values(row))
    # print(list_current)
    return list_current


print(data_per_month('2015\\09.xlsx'))

aList = [123, 'xyz', 'zara', 'abc']

aList.insert(3, 2009)

