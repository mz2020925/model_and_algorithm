import os
import pyproj
from numpy import *
import pandas as pd
import csv
import matplotlib.pyplot as plt

"""
北斗卫星导航作业要求:
根据范老师给出的50组卫星导航数据，进行定位解算。
具体步骤依次为估算点坐标解算，估算点位置校正，坐标转换和精度因子的计算，具体参考第五章ppt，
最后得到北斗和GPS的定位解算结果和相应的五个精度因子，报告中应包含定位解算原理，定位解算结果和数据分析。
报告请发到邮箱2950870935@qq.com，截至日期为本学期期末左右。
（备注：sv代表序号，每组前五个为GPS数据，后五个BDS数据，x,y,z为卫星坐标位置，
pse代表伪距，io为电离层折射修正，tr为对流层折射修正，另外有几组数据计算出来偏差较大，需要舍弃）
"""


def leastsqaure_newton(satellite, rho):
    """
    不包含c*delta、I、T，不用此函数计算
    :param satellite:
    :param rho:
    :return:
    """
    pk = mat([[0], [0], [0]])
    c = 3.0e8
    for i in range(5):
        pkMatrix = mat(ones((5, 3)))
        for i in range(5):
            pkMatrix[i, :] = reshape(pk[:, 0], (1, 3))
        di = sqrt(sum(square(pkMatrix[:, :3] - satellite), axis=1))
        bi = di - rho
        diMat = mat(zeros((5, 3)))
        for i in range(5):
            diMat[i, :] = reshape([di[i], di[i], di[i]], (1, 3))
        G1 = divide(pkMatrix[:, :3] - satellite, diMat)
        # print(G1)
        G1 = hstack((G1, mat([[c], [c], [c], [c], [c]])))
        deltaPK = dot(dot(linalg.inv(dot(G1.T, G1)), G1.T), bi)
        pk = pk - deltaPK[:3, 0]
    return pk


def leastsqaure_newton2(filename, satellite, rho, I, T):
    """
    包含c*delta、I、T
    :param satellite:
    :param rho:
    :param I:
    :param T:
    :return:
    """
    pk = mat([[0], [0], [0], [0]])
    c = 3.0e8
    for i in range(10):
        pkMatrix = mat(ones((5, 4)))
        for i in range(5):
            pkMatrix[i, :] = reshape(pk[:, 0], (1, 4))

        di = sqrt(sum(square(pkMatrix[:, :3] - satellite), axis=1))
        bi = di + pkMatrix[:, 3] + I + T - rho  # pkMatrix[:, 3] = c * delta

        diMat = mat(zeros((5, 3)))
        for i in range(5):
            diMat[i, :] = reshape([di[i], di[i], di[i]], (1, 3))

        G1 = divide(pkMatrix[:, :3] - satellite, diMat)
        G1 = hstack((G1, mat([[1], [1], [1], [1], [1]])))
        G2 = linalg.inv(dot(G1.T, G1))
        deltaPK = dot(dot(G2, G1.T), bi)
        pk = pk - deltaPK
        if (linalg.norm(deltaPK, 2) < 1):
            lla = ecef2lla(pk[0, 0], pk[1, 0], pk[2, 0])
            if (103 < lla[0] < 104 and 30 < lla[1] < 31 and (500 < lla[2] < 600 or 2900 < lla[2] < 3000)):
                dop = dop5(G2)  # HDOP, VDOP, PDOP, TDOP, GDOP = dop5(G2)
                f = open(filename, "a", newline='')
                ls = [str(i) for i in lla] + [str(j) for j in dop]
                writer = csv.writer(f)
                writer.writerow(ls)
                f.close()
            break


def ecef2lla(x, y, z):
    transformer = pyproj.Transformer.from_crs(
        {"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'},
        {"proj": 'latlong', "ellps": 'WGS84', "datum": 'WGS84'},
    )
    lon1, lat1, alt1 = transformer.transform(x, y, z, radians=False)
    return lon1, lat1, alt1


def dop5(H):
    HDOP = sqrt(sum(square(diagonal(H)[:2])))  # 水平精度因子
    VDOP = sqrt(sum(square(diagonal(H)[2])))  # 高程精度因子
    PDOP = sqrt(sum(square(diagonal(H)[:3])))  # 三维位置精度因子
    TDOP = abs(diagonal(H)[3])  # 钟差精度因子
    GDOP = sqrt(sum(square(diagonal(H))))  # 几何精度因子
    return HDOP, VDOP, PDOP, TDOP, GDOP


def draw(pkArr):
    length = len(pkArr[:, 0])
    x = asarray(pkArr[:, 0]).flatten()
    y = asarray(pkArr[:, 1]).flatten()
    z = asarray(pkArr[:, 2]).flatten()
    delta = asarray(pkArr[:, 3]).flatten()
    haxis = arange(0, length, 1)
    subdraw("X-result", "X", "result", haxis, x)
    subdraw("Y-result", "Y", "result", haxis, y)
    subdraw("Z-result", "Z", "result", haxis, z)
    subdraw("delta-result", "delta", "result", haxis, delta)


def subdraw(title, xlable, ylable, haxis, data):
    # plt.figure(figsize=(10, 15), dpi=100)
    plt.scatter(haxis, data)
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    plt.show()


def calculate(sheets, startRow, endRow, filename):
    pkArr = array([[]])
    for sheet in sheets.values():
        if sheet.index[-1] == 9:
            df = sheet.iloc[startRow:endRow, 0:3]
            satellite = mat(array(df))
            rho = reshape(mat(sheet.iloc[startRow:endRow, 3]), (5, 1))
            I = reshape(mat(sheet.iloc[startRow:endRow, 4]), (5, 1))
            T = reshape(mat(sheet.iloc[startRow:endRow, 5]), (5, 1))
            leastsqaure_newton2(filename=filename, satellite=satellite, rho=rho, I=I, T=T)
            # pk = leastsqaure_newton2(filename=filename, satellite=satellite, rho=rho, I=I, T=T)
            # if size(pkArr) == 0:
            #     pkArr = reshape(pk, (1, 4))
            # else:
            #     pkArr = vstack((pkArr, reshape(pk, (1, 4))))


if __name__ == '__main__':
    sheets = pd.read_excel(io='data.xlsx', sheet_name=None, header=0, usecols="B:G", nrows=11)
    # 根据GPS数据，进行估算点坐标解算
    filename1 = "GPS-LLA-DOP5.csv"
    current_path = os.getcwd()
    if os.path.exists(current_path + '\\' + filename1):
        os.remove(current_path + '\\' + filename1)
    calculate(sheets, startRow=0, endRow=5, filename=filename1)
    gps = pd.read_csv(filename1)
    gps_mean = gps.mean()
    print(gps_mean)
    draw(mat(array(gps))[:, :4])

    # 根据北斗数据，进行估算点坐标解算
    # filename2 = "beidou-LLA-DOP5.csv"
    # current_path = os.getcwd()
    # if os.path.exists(current_path + '\\' + filename2):
    #     os.remove(current_path + '\\' + filename2)
    # calculate(sheets, startRow=5, endRow=10, filename=filename2)
    # beidou = pd.read_csv(filename2)
    # beidou_mean = beidou.mean()
    # print(beidou_mean)
    # draw(mat(array(beidou))[:, :4])


