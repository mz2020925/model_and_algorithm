import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]  # [375.0, 75.0, 250.0, 300.0]
ingredients = [x.split()[-1] for x in recipe]  # 扇形的标签['flour', 'sugar', 'butter', 'berries']
# print(data)
# print(ingredients)


def func(pct, allvals):
    # absolute = int(pct/100.*np.sum(allvals))
    absolute = int(pct*10)
    return "{:.1f}%\n({:d} g)".format(pct, absolute)


patches, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                   textprops=dict(color="w"))

# patches -- 各个扇形块对象(地址)组成的列表，这些是matplotlib.patches.Wedge patches，可以直接用作图例的句柄
# texts -- 扇形标签的位置和字组成的列表，
# autotexts -- 占比标签的位置和字组成的列表
ax.legend(patches, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
# 这里我们使用轴坐标（1，0，0.5，1）和位置“中心左”：即图例的左中心点将位于边界框的左中心点，在轴坐标中从（1，0）跨越到（1.5，1）

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()
