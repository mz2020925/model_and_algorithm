import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# plt.style.use('dark_background')
fig = plt.figure()  # 构造底层面板对象
ax2 = fig.add_subplot(2, 1, 1)

L = 6
x = np.linspace(0, L)  # 返回一个从0到L的默认固定间隔的列表
# print(x)
ncolors = len(plt.rcParams['axes.prop_cycle'])
print(ncolors)
ncolors = 5
shift = np.linspace(0, L, ncolors, endpoint=False)
print(shift)
for s in shift:
    ax2.plot(x, np.sin(x + s), '.-')
ax2.tick_params(axis='both', which='both', direction='in')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax2.set_title("'dark_background' style sheet")
plt.axhline(0, linestyle='--', color='r', linewidth=1, )  # 绘制水平线y=0，x轴
plt.legend(('Model length', 'Data length', 'Total message length'),
           loc='lower center', bbox_to_anchor=(0.5, -0.7))
# ax2.legend(('Model length', 'Data length', 'Total message length'),
#            loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)  ##设置ax4中legend的位置，将其放在图外

plt.show()
