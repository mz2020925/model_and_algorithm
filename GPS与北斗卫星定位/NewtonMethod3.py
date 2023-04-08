import numpy as np
import pandas as pd
import os
import pyproj
import math

os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def newton(satellite, I, T, rho):
    # 设定初值x,y,x,ct初值X =-1321536.586;Y =5327607.481;Z =3243191.873;
    # -1317014.3846772, 5322708.377186806, 3248101.2068022704
    pk = np.array([-1317014.3846772, 5322708.377186806, 3248101.2068022704])
    c = 3.0e8
    while (True):
        tempxyz = np.ones((5, 3))
        for i in range(5):
            tempxyz[i, :] = pk[:]

        di = np.sqrt(np.sum(np.square(tempxyz - satellite), axis=1))
        aphi = 7.2921150e-5 * di / c
        satelliteTemp = np.ones((5, 3))
        for i in range(5):
            satelliteTemp[i, 0] = np.cos(aphi[i]) * satellite[i, 0] - np.sin(aphi[i]) * satellite[i, 1]
            satelliteTemp[i, 1] = np.sin(aphi[i]) * satellite[i, 0] + np.cos(aphi[i]) * satellite[i, 1]
            satelliteTemp[i, 2] = satellite[i, 2]

        di = np.sqrt(np.sum(np.square(tempxyz - satelliteTemp), axis=1))
        diMat = np.zeros((5, 3))
        for i in range(5):
            diMat[i, :] = np.array([di[i], di[i], di[i]])
        G = np.divide(tempxyz - satelliteTemp, diMat)
        bi = di + c * I + c * T - rho

        # print(G)
        # G0 = np.linalg.inv(G.T @ G)
        # G1 = G0 @ G.T
        # pk = pk - (G1 @ bi.T)
        DeltaPK = np.linalg.pinv(G) @ bi.T
        pk = pk - DeltaPK
        print(pk)
        if (np.sqrt(np.square(pk[0]--1317014.3846772)) < 100):
            # HDOP = np.sqrt(np.sum(np.square(np.diagonal(G0)[:2])))  # 水平精度因子
            # VDOP = np.sqrt(np.sum(np.square(np.diagonal(G0)[2])))  # 高程精度因子
            # PDOP = np.sqrt(np.sum(np.square(np.diagonal(G0)[:3])))  # 三维位置精度因子
            # TDOP = np.abs(np.diagonal(G0)[3])  # 钟差精度因子
            # GDOP = np.sqrt(np.sum(np.square(np.diagonal(G0))))  # 几何精度因子
            # pk = np.append(pk, [HDOP, VDOP, PDOP, TDOP, GDOP])
            break
        print("=================================")
    return pk


def calculate(sheets, startRow, endRow):
    # print(sheets)
    # data = sheets.values()
    # print(data.size())
    pkArr = np.array([[]])
    for sheet in sheets.values():
        # print(sheet)
        if sheet.index[-1] == 9:
            # print("true")
            df = sheet.iloc[startRow:endRow, 0:3]
            satellite = np.array(df)
            rho = np.array(sheet.iloc[startRow:endRow, 3])
            I = np.array(sheet.iloc[startRow:endRow, 4])
            T = np.array(sheet.iloc[startRow:endRow, 5])
            pk = newton(satellite=satellite, I=I, T=T, rho=rho)
            print(pk)
            if np.size(pkArr) == 0:
                pkArr = pk
            else:
                pkArr = np.vstack((pkArr, pk))
    return pkArr


# ECEF坐标系转换为wgs84坐标系
# def LBHtoXYZ(L, B, H):
#     a = 6378137.
#     b = 6356752.3142
#     ee = (np.square(a) - np.square(b)) / np.square(a)
#     N = a / np.sqrt(1 - np.square(ee * np.sin(B)))
#     X = (N + H) * np.cos(B) * np.cos(L)
#     Y = (N + H) * np.cos(B) * np.sin(L)
#     Z = (N * (1 - ee) + H) * np.sin(B)
#     return X, Y, Z


# wgs84坐标系转换为ECEF坐标系
def XYZtoLBH(x, y, z):
    # Convert from ECEF cartesian coordinates to
    # latitude, longitude and height of WGS-84
    x2 = x ** 2
    y2 = y ** 2
    z2 = z ** 2
    pi = 3.14159265359
    a = 6378137.0000  # earth radius in meters
    b = 6356752.3142  # earth semiminor in meters
    e = math.sqrt(1 - (b / a) ** 2)
    b2 = b * b
    e2 = e ** 2
    ep = e * (a / b)
    r = math.sqrt(x2 + y2)
    r2 = r * r
    E2 = a ** 2 - b ** 2
    F = 54 * b2 * z2
    G = r2 + (1 - e2) * z2 - e2 * E2
    c = (e2 * e2 * F * r2) / (G * G * G)
    s = (1 + c + math.sqrt(c * c + 2 * c)) ** (1 / 3)
    P = F / (3 * (s + 1 / s + 1) ** 2 * G * G)
    Q = math.sqrt(1 + 2 * e2 * e2 * P)
    ro = -(P * e2 * r) / (1 + Q) + math.sqrt(
        (a * a / 2) * (1 + 1 / Q) - (P * (1 - e2) * z2) / (Q * (1 + Q)) - P * r2 / 2)
    tmp = (r - e2 * ro) ** 2
    U = math.sqrt(tmp + z2)
    V = math.sqrt(tmp + (1 - e2) * z2)
    zo = (b2 * z) / (a * V)
    height = U * (1 - b2 / (a * V))
    lat = math.atan((z + ep * ep * zo) / r)
    temp = math.atan(y / x)
    if x >= 0:
        long = temp
    elif (x < 0) & (y >= 0):
        long = pi + temp
    else:
        long = temp - pi
    lat0 = lat / (pi / 180)
    lon0 = long / (pi / 180)
    h0 = height
    return lon0, lat0, h0


# ECEF坐标系转换为wgs84坐标系
def ecef2lla(x, y, z):
    # ecef转换为经纬高
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    lon, lat, alt = pyproj.transform(ecef, lla, x, y, z, radians=False)  # 用弧度返回值
    return lon, lat, alt


# wgs84坐标系转换为ECEF坐标系
def lla2ecef(lon, lat, alt):

    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    x, y, z = pyproj.transform(lla, ecef, lon, lat, alt)
    return x, y, z


sheets = pd.read_excel(io='data.xlsx', sheet_name=None, header=0, usecols="B:G", nrows=11)
# 根据GPS数据，进行估算点坐标解算
pkArr = calculate(sheets, startRow=0, endRow=5)
# print(pkArr)
# pkArrLBH = np.array([[]])
# for i in pkArrXYZ:
#     temp = np.array(XYZtoLBH(i[0], i[1], i[2]))
#     if np.size(pkArrLBH) == 0:
#         pkArrLBH = temp
#     else:
#         pkArrLBH = np.vstack((pkArrLBH, temp))
