# Программа5
# метод Рунге-Кутта
import math as mt
import matplotlib.pyplot as plt


def uu(j, t, y):
    return 2 + 2 * j * (1 + j * mt.tan(j)) / (mt.cos(j)) ** 2 - 1 / (mt.cos(j)) ** 2 * y - 2 * mt.tan(j) / (
        mt.cos(j)) ** 2 * t


def func(p):
    return p ** 2 + mt.exp(-mt.tan(p))


b = 1
a = 0
h = 0.05
v = []
x = [0]
u = []
u.insert(0, 1)
v.insert(0, -1)
for i in range(int(1/h)):
    k1u = v[i]
    k1v = uu(x[i], u[i], v[i])
    k2u = v[i] + h / 2 * k1v
    k2v = uu(x[i] + h / 2, u[i] + h / 2 * k1u, k2u)
    k3u = v[i] + h / 2 * k2v
    k3v = uu(x[i] + h / 2, u[i] + h / 2 * k2u, k3u)
    k4u = v[i] + h * k3v
    k4v = uu(x[i] + h, u[i] + h * k3u, k4u)
    v.append(v[i] + h / 6 * (k1v + 2 * k2v + 2 * k3v + k4v))
    u.append(u[i] + h / 6 * (k1u + 2 * k2u + 2 * k3u + k4u))
    x.append(x[i] + h)
w = 0
xf = []
fr = []
while w < 101:
    xf.append(w / 100)
    fr.append(func(xf[w]))
    w += 1

h2 = 0.1
vr = []
xr = [0]
ur = []
ur.insert(0, 1)
vr.insert(0, -1)
for i in range(int(1/h2)):
    k1u = v[i]
    k1v = uu(xr[i], ur[i], vr[i])
    k2u = vr[i] + h2 / 2 * k1v
    k2v = uu(xr[i] + h2 / 2, ur[i] + h2 / 2 * k1u, k2u)
    k3u = vr[i] + h2 / 2 * k2v
    k3v = uu(xr[i] + h2 / 2, ur[i] + h2 / 2 * k2u, k3u)
    k4u = vr[i] + h2 * k3v
    k4v = uu(xr[i] + h2, ur[i] + h2 * k3u, k4u)
    vr.append(vr[i] + h2 / 6 * (k1v + 2 * k2v + 2 * k3v + k4v))
    ur.append(ur[i] + h2 / 6 * (k1u + 2 * k2u + 2 * k3u + k4u))
    xr.append(xr[i] + h2)

z = 0
sr = []
for q in range(int(1/h2) + 1):
    sr.append(abs(ur[q] - u[q+z])/(2**4-1))
    z += 1

plt.figure(1)
plt.plot(x, u)
plt.plot(xf, fr, color='yellow', linestyle='--')

plt.figure(2)
plt.plot(xr, sr)

plt.show()