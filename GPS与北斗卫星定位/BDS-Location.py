"""
北斗卫星导航作业要求:
根据范老师给出的50组卫星导航数据，进行定位解算。
具体步骤依次为估算点坐标解算，估算点位置校正，坐标转换和精度因子的计算，具体参考第五章ppt，
最后得到北斗和GPS的定位解算结果和相应的五个精度因子，报告中应包含定位解算原理，定位解算结果和数据分析。
报告请发到邮箱2950870935@qq.com，截至日期为本学期期末左右。
（备注：sv代表序号，每组前五个为GPS数据，后五个BDS数据，x,y,z为卫星坐标位置，
pse代表伪距，io为电离层折射修正，tr为对流层折射修正，另外有几组数据计算出来偏差较大，需要舍弃）
"""
import pandas as pd
import numpy as np
from GPS与北斗卫星定位.csdn import *
# 读取数据
sheets = pd.read_excel(io='data.xlsx', sheet_name=None, header=0, usecols="B:G", nrows=11)

# 根据GPS数据，进行估算点坐标解算
pkArr = calculate(sheets, startRow=0, endRow=5)
print(len(pkArr))
# 估算点位置校正


# 坐标转换和精度因子的计算


# 得到GPS的定位解算结果和相应的五个精度因子


# 根据北斗数据计算，进行估算点坐标解算
# pkArr = calculate(sheets, startRow=5, endRow=10)

# 估算点位置校正


# 坐标转换和精度因子的计算


# 得到北斗的定位解算结果和相应的五个精度因子




sheets = pd.read_excel(io='data.xlsx', sheet_name=None, header=0, usecols="B:G", nrows=11)
# 根据GPS数据，进行估算点坐标解算
pkArrXYZ = calculate(sheets, startRow=0, endRow=5)
print(pkArrXYZ)
pkArrLBH = []
for i in pkArrXYZ:
    print(i)
    pkArrLBH.append(list(ecef2lla(i[0], i[1], i[2])))

print(len(pkArrLBH))