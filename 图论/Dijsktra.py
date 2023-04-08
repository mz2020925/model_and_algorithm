import numpy as np

matrix = [[np.inf, 2,      8,      1,      np.inf, np.inf, np.inf, np.inf],
          [2,      np.inf, 6,      np.inf, 1,      np.inf, np.inf, np.inf],
          [8,      6,      np.inf, 7,      4,      2,      2,      np.inf],
          [1,      np.inf, 7,      np.inf, np.inf, np.inf, 9,      np.inf],
          [np.inf, 1,      4,      np.inf, np.inf, 3,      np.inf,      9],
          [np.inf, np.inf, 2,      np.inf, 3,      np.inf, 4,           6],
          [np.inf, np.inf, 2,      9,      np.inf, 4,      np.inf,      2],
          [np.inf, np.inf, np.inf, np.inf, 9,      6,      2,      np.inf]]

length_sign_ls = [-1 for i in range(8)]  # 存储每个顶点的标号（标号是该顶点到起点的最短路径长度）
A = []  # 已标号的顶点的集合（用索引代表顶点）
T = []  # 最短路径的边的集合
# 起点是索引0，终点是索引7，开始寻路
start_v = 0  # 寻路点从a点出发开始寻路，起始点是a点，也就是索引0的点，把它加入到已标号(就是已寻到)的集合A中
length_sign_ls[start_v] = 0  # 起点（索引0）标号为0
A.append(start_v)

while True:
    closest_v_dt = {}
    # 对于集合A中的这个已标号顶点，进行如下操作:
    for signed_v in A:
        # 写出当前这个已标号顶点的与其他所有顶点（包括邻接顶点）的边权值集合
        a_row_of_mat = matrix[signed_v]
        no_sign_next_v = {}
        for i in range(len(a_row_of_mat)):
            # 判断顶点是否是这个已标号顶点的邻接顶点，并且还没有被标号
            if a_row_of_mat[i] != np.inf and length_sign_ls[i] == -1:
                # 未标号邻接顶点的索引作为键，未标号邻接顶点与当前这个已标号顶点的边权值作为值
                no_sign_next_v[i] = a_row_of_mat[i]

        if no_sign_next_v != {}:
            # 求出"未标号""邻接"顶点中边权值最小的那一个（就是离这个已标号顶点"最近的"），返回索引值
            closest_v = min(no_sign_next_v, key=lambda x: no_sign_next_v[x])
            # sum_of_two_num = 这个已标号顶点的标号 + 这个已标号顶点与"最近的""未标号""邻接"顶点之间的边权值
            sum_of_two_num = length_sign_ls[signed_v] + a_row_of_mat[closest_v]
            # "最近的""未标号""邻接"顶点的索引作为键，"最近的""未标号""邻接"顶点与当前这个已标号顶点的边权值作为值
            if closest_v not in closest_v_dt.keys():
                closest_v_dt[closest_v] = [sum_of_two_num, str(signed_v) + '->' + str(closest_v)]
            else:
                if sum_of_two_num < closest_v_dt[closest_v][0]:  # 如果更小，则更新字典中的原有键值
                    closest_v_dt[closest_v] = [sum_of_two_num, str(signed_v) + '->' + str(closest_v)]

    # 经过上面的遍历集合A，求出所有sum_of_two_num中最小的那一个，它就是本次while循环求出的待标号的顶点，返回索引值，
    closest_v = min(closest_v_dt, key=lambda x: closest_v_dt[x][0])
    # 更新待标号的顶点的标号
    length_sign_ls[closest_v] = closest_v_dt[closest_v][0]
    # 更新集合T
    T.append(closest_v_dt[closest_v][1])
    # 更新集合A
    A.append(closest_v)

    # 判断是否到达终点，若是则跳出循环
    if closest_v == 7:
        break

# 寻路过程记录下的边集合包含最短路径的边，但不是仅包含最短路径的边
print(f'寻路过程记录下的边集合：\n{T}')
print(f'顶点0~7的标号值：\n{length_sign_ls}')
