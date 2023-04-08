from numpy import *
import numpy as np
#          a                                   b
#          0     1    2    3    4    5    6    7
matrix =\
    [[inf,  2,   8,   1,  inf, inf, inf, inf],  # 0
     [2,   inf,  6,  inf,  1,  inf, inf, inf],  # 1
     [8,    6,  inf,  7,   4,   2,   2,  inf],  # 2
     [1,   inf,  7,  inf, inf, inf,  9,  inf],  # 3
     [inf,  1,   4,  inf, inf,  3,  inf,   9],  # 4
     [inf, inf,  2,  inf,  3,  inf,  4,    6],  # 5
     [inf, inf,  2,   9,  inf,  4,  inf,   2],  # 6
     [inf, inf, inf, inf,  9,   6,   2,  inf]]  # 7


A = []  # 已标号集合
T = []  # 最短路径的边的集合
# 第一步
vertex_index = 0  # 起始点是a点，也就是索引0的点，把它加入到已标号的集合A中
A.append(vertex_index)

# print(argmin(matrix[vertex_index].pop(vertex_index)))
# print(argmin(matrix[vertex_index]))
# length = [inf for i in range(8)]
# print(length==[inf for i in range(8)])


print(str(4)+'->'+str(5))