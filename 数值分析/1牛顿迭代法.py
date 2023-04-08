#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/9/28 17:01
# @Author : zmz
# @File : 1牛顿迭代法.py
# @Software: PyCharm
import os

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

figure = plt.figure()
ax = Axes3D(figure)  # 设置图像为三维格式
X = np.arange(-10, 10, 0.1)
Y = np.arange(-10, 10, 0.1)  # X,Y的范围
X, Y = np.meshgrid(X, Y)  # 绘制网格
Z = (np.sin(X) * np.sin(Y)) / (X * Y)  # f(x,y)=(sin(x)*sin(y))/(x*y),注意括号
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# 绘制3D图，后面的参数为调节图像的格式
plt.show()  # 展示图片
plt.clf()

