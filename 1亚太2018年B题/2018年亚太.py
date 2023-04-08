import pandas as pd
import os

dir2015_9_12 = os.listdir("2015")
dir2016 = os.listdir("2016")
dir2017 = os.listdir("2017")
dir2018_1_8 = os.listdir("2018")


def readdata(dir, string):
    df = pd.read_excel(string + '\\' + dir[0])
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('display.width', None)  # 显示宽度是无限
    # print(df.head())                   # 返回数据的前5行
    for filename in dir[1:]:
        df_current = pd.read_excel(string + '\\' + filename)
        df = pd.concat([df, df_current])
    df.columns = df.index(1).tolist()
    # df.drop([0, 1], inplace=True)
    return df


df_2015 = readdata(dir2015_9_12, '2015')
df_2015.to_csv("2015.csv")


# print(df_2015['2015.09.01 -- 2015.09.30  Market Demand Statistics'])
# df_2016 = readdata(dir2016)
# df_2017 = readdata(dir2017)
# df_2018 = readdata(dir2018_1_8)


def excel_to_df(file):
    student_df = pd.efile(skiprows=1, usecols=['年级', '姓名', '性别', '原学院', '原专业', '现转入学院', '现转入专业'])
    # print(student_df.head(10))
    return student_df







