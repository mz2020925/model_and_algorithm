# # First create some toy data:
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)
#
# # # Create just a figure and only one subplot
# # fig, ax = plt.subplots()
# # ax.plot(x, y)
# # ax.set_title('Simple plot')
#
#
# # Create two subplots and unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)  # 把连续曲线离散化
# plt.show()


bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")
print(kw)