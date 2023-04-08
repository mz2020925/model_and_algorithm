import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np


star = mpath.Path.unit_regular_star(6)
circle = mpath.Path.unit_circle()
# concatenate the circle with an internal cutout of the star
verts = np.concatenate([circle.vertices, star.vertices[::-1, ...]])
codes = np.concatenate([circle.codes, star.codes])
cut_star = mpath.Path(verts, codes)

# plt.grid(True, linestyle="--", alpha=0.5)   # 水平垂直网格
plt.grid(True, 'major', 'y', ls='--', lw=0.8, c='k', alpha=.5)  # 水平网格
# plt.plot(np.arange(10)**2, '--',color='gray', marker='o', markersize=15)
plt.plot(np.arange(10)**2, '--', marker='o', markersize=10)
plt.show()