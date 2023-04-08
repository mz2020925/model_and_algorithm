import numpy as np
import pandas as pd
import math

import pyproj


def point_position(x, y, z, c_range):
    # 设定初值x,y,x,ct初值X =-1321536.586;Y =5327607.481;Z =3243191.873;
    c = 3e8
    x0, y0, z0 = 0, 0, 0  # initial coordinate
    for i in range(5):
        R = np.mat(np.zeros((5, 1)))  # approximate geometric distance
        l = np.mat(np.zeros((5, 1)))  # first column of the design matrix
        m = np.mat(np.zeros((5, 1)))  # second column of the design matrix
        n = np.mat(np.zeros((5, 1)))  # third column of the design matrix
        L = np.mat(np.zeros((5, 1)))  # observation vector
        for j in range(len(x)):
            R[j, 0] = np.sqrt((x[j] - x0) ** 2 + (y[j] - y0) ** 2 + (z[j] - z0) ** 2)
            l[j, 0] = (x[j] - x0) / R[j, 0]
            m[j, 0] = (y[j] - y0) / R[j, 0]
            n[j, 0] = (z[j] - z0) / R[j, 0]
            L[j, 0] = c_range[j] - R[j, 0]

        A = np.hstack((l, m, n, np.mat([[c], [c], [c], [c], [c]])))  # design matrix
        X = -(A.T * A).I * A.T * L
        x0, y0, z0 = x0 + X[0, 0], y0 + X[1, 0], z0 + X[2, 0]
    # QY = (A.T * A).I  # cofactor matrix
    # QX = QY[[0, 1, 2]]
    # QX = QX[:, [0, 1, 2]]

    # blh = xyz2blh([x0, y0, z0])  # B--rad,L--rad
    # B, L = blh[0], blh[1]
    # rotate = np.mat([[-np.sin(B) * np.cos(L), -np.sin(B) * np.sin(L), np.cos(B)], [-np.sin(L), np.cos(L), 0],
    #                  [np.cos(B) * np.cos(L), np.sin(B) * np.sin(L), np.sin(B)]])  # rotate matrix
    # QR = rotate * QX * rotate.T
    # try:
    #     HDOP = np.sqrt(QR[0, 0] + QR[1, 1])
    #     VDOP = np.sqrt(QR[2, 2])
    #     PDOP = np.sqrt(QX[0, 0] + QX[1, 1] + QX[2, 2])
    #     TDOP = np.sqrt(QY[3, 3])
    #     GDOP = np.sqrt(QX[0, 0] + QX[1, 1] + QX[2, 2] + QY[3, 3])
    # except Exception as e:
    #     print(QR)
    # print(HDOP, VDOP, PDOP, TDOP, GDOP)
    return x0, y0, z0


def xyz2blh(xyz):
    blh = [0, 0, 0]
    a = 6378137.0
    f = 1.0 / 298.257223563
    e2 = f * (2 - f)
    r2 = xyz[0] * xyz[0] + xyz[1] * xyz[1]
    z = xyz[2]
    zk = 0.0

    while abs(z - zk) >= 0.0001:
        zk = z
        sinp = z / math.sqrt(r2 + z * z)
        v = a / math.sqrt(1.0 - e2 * sinp * sinp)
        z = xyz[2] + v * e2 * sinp

    if r2 > 1E-12:
        blh[0] = math.atan(z / math.sqrt(r2))
        blh[1] = math.atan2(xyz[1], xyz[0])
    else:
        if r2 > 0:
            blh[0] = math.pi / 2.0
        else:
            blh[0] = -math.pi / 2.0
        blh[1] = 0.0

    blh[2] = math.sqrt(r2 + z * z) - v
    return blh


def calculate(sheets, startRow, endRow):
    # print(sheets)
    # data = sheets.values()
    # print(data.size())
    pkArr = []
    for sheet in sheets.values():
        # print(sheet)
        if sheet.index[-1] == 9:
            # print("true")
            df = sheet.iloc[startRow:endRow, 0:3]
            satellite = np.array(df)
            rho = np.array(sheet.iloc[startRow:endRow, 3])
            # I = np.array(sheet.iloc[startRow:endRow, 4])
            # T = np.array(sheet.iloc[startRow:endRow, 5])
            pk = point_position(satellite[:, 0], satellite[:, 1], satellite[:, 2], rho)
            # if np.size(pkArr) == 0:
            #     pkArr = pk
            # else:
            #     pkArr = np.vstack((pkArr, pk))
            pkArr.append(pk)
            print(ecef2lla(pk[0],pk[1],pk[2]))
            # print(pk)
    return pkArr


def ecef2lla(x, y, z):
    transformer = pyproj.Transformer.from_crs(
        {"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'},
        {"proj": 'latlong', "ellps": 'WGS84', "datum": 'WGS84'},
    )
    lon1, lat1, alt1 = transformer.transform(x, y, z, radians=False)
    return lat1, lon1, alt1


sheets = pd.read_excel(io='data.xlsx', sheet_name=None, header=0, usecols="B:G", nrows=11)
# 根据GPS数据，进行估算点坐标解算
pkArr = calculate(sheets, startRow=5, endRow=10)
# print(len(pkArr))
# pkArrLBH = np.array([[]])
# for i in pkArrXYZ:
#     temp = np.array(XYZtoLBH(i[0], i[1], i[2]))
#     if np.size(pkArrLBH) == 0:
#         pkArrLBH = temp
#     else:
#         pkArrLBH = np.vstack((pkArrLBH, temp))
