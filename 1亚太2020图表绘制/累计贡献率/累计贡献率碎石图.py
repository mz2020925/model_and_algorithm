import matplotlib.pyplot as plt

Component = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
Characteristic_value = [4.943, 2.391, .688, .651, .247, .043, .031, .007, .001]

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(Component, Characteristic_value, '-o', color='black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tick_params(top=False, direction='in', labelsize=12)
plt.grid(axis='y', alpha=0.6, linewidth=0.5)
ax.set_xlabel("Component", fontsize=12)
ax.set_ylabel("Characteristic value", fontsize=12)
plt.show()











