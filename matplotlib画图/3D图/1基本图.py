from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.1)
Y = np.arange(-4, 4, 0.1)

X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.show()


axis = plt.gca().xaxis
ticklocs = axis.get_ticklocs()  # 刻度位置
ticklabels = axis.get_ticklabels()  # 刻度标签
ticklines = axis.get_ticklines()  # 主刻度线数目
ticklines2 = axis.get_ticklines(minor=True)  # 副刻度线数目
print(ticklocs)
print(ticklabels)
print(ticklines)
print(ticklines2)