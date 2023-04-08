import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('A tale of 2 subplots')

ax1.plot(x1, y1, 'o-', label='$sinx$')
ax1.legend()
ax1.set_ylabel('Damped oscillation')

ax2.tick_params(axis='both', which='both', direction='in')
ax2.plot(x2, y2, '.-')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')
ax2.xaxis.set_major_locator(MultipleLocator(np.pi/4))
# ax2.xaxis.set_major_formatter(FuncFormatter(pi_formatter))

ax2.xaxis.set_minor_locator(MultipleLocator(np.pi/20))
plt.ylim(-1.2, 1.2)
plt.xticks(fontsize=8, color='r', rotation=45)  # rotation=45,逆时针旋转45度
plt.subplots_adjust(bottom=0.15)  # 设置图的底边距

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

# 方式二
# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 2.0)
#
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
#
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, 'o-')
# plt.title('A tale of 2 subplots')
# plt.ylabel('Damped oscillation')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, '.-')
# plt.xlabel('time (s)')
# plt.ylabel('Undamped')
#
# plt.show()

