import numpy as np
import matplotlib.pyplot as plt
"""
h = 0.01
t = np.arange(0, 10 + h, h)

g, m2 = 6.67, 5.965e-1
vxn, vyn = 0, -1
xn, yn = 2, 0
x = []
y = []
x.append(xn)
y.append(yn)
for i in range(np.size(t) - 1):
    vxn = vxn + h * (-1 * xn * g * m2 / (np.power(np.power(xn, 2) + np.power(yn, 2), 1.5)))
    vyn = vyn + h * (-1 * yn * g * m2 / (np.power(np.power(xn, 2) + np.power(yn, 2), 1.5)))
    xn = xn + h * vxn
    yn = yn + h * vyn
    x.append(xn)
    y.append(yn)

print(np.size(x), np.size(y))
plt.plot(x, y)
plt.show()
"""
h = 0.01
t = np.arange(0, 10 + h, h)
g, m2 = 6, 0.4

Vx = np.zeros(np.size(t))
Vx[0] = 0

Vy = np.zeros(np.size(t))
Vy[0] = -1

x = np.zeros(np.size(t))
x[0] = 2

y = np.zeros(np.size(t))
y[0] = 0

for i in range(1, np.size(t)):
    x[i] = x[i - 1] + h * Vx[i - 1]
    Vx[i] = Vx[i - 1] + h * (-1 * x[i - 1] * g * m2 / (np.power(np.power(x[i - 1], 2) + np.power(y[i - 1], 2), 1.5)))

    y[i] = y[i - 1] + h * Vy[i - 1]
    Vy[i] = Vy[i - 1] + h * (-1 * y[i - 1] * g * m2 / (np.power(np.power(x[i - 1], 2) + np.power(y[i - 1], 2), 1.5)))

print(np.size(x), np.size(y))
plt.plot(x, y)
plt.show()

