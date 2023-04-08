import numpy as np
import matplotlib.pyplot as plt

h = 0.01
t = np.arange(0, 10 + h, h)
g, m2 = 6.67, 5.965e-1

Vx = np.zeros(np.size(t))
Vx[0] = 0

Vy = np.zeros(np.size(t))
Vy[0] = -1

x = np.zeros(np.size(t))
xx = np.zeros(np.size(t))
x[0] = 2
xx[0] = 2

y = np.zeros(np.size(t))
yy = np.zeros(np.size(t))
y[0] = 0
yy[0] = 0

for i in range(1, np.size(t)):
    # 计算改进欧拉法的
    #    Vx,n+1^(k+1)
    x[i] = x[i - 1] + h * Vx[i - 1]
    y[i] = y[i - 1] + h * Vy[i - 1]
    Vx[i] = Vx[i - 1] + 0.5 * h * (
            -1 * x[i - 1] * g * m2 / (np.power(np.power(x[i - 1], 2) + np.power(y[i - 1], 2), 1.5))
            - x[i] * g * m2 / (np.power(np.power(x[i], 2) + np.power(y[i], 2), 1.5)))
    x[i] = x[i - 1] + 0.5 * h * (Vx[i - 1] + Vx[i])

    Vy[i] = Vy[i - 1] + 0.5 * h * (
            -1 * y[i - 1] * g * m2 / (np.power(np.power(x[i - 1], 2) + np.power(y[i - 1], 2), 1.5))
            - y[i] * g * m2 / (np.power(np.power(x[i], 2) + np.power(y[i], 2), 1.5)))

    y[i] = y[i - 1] + 0.5 * h * (Vy[i - 1] + Vy[i])
print(np.size(x), np.size(y))
plt.plot(x, y)
plt.show()
