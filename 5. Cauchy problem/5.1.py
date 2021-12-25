# Программа5
# метод Эйлера
import math as mt
import matplotlib.pyplot as plt


def uu(j, t, y):
    return 2 + 2 * j * (1+j*mt.tan(j))/(mt.cos(j))**2 - 1/(mt.cos(j))**2 * y - 2 * mt.tan(j)/(mt.cos(j))**2 * t



def func(p):
    return p**2 + mt.exp(-mt.tan(p))



a = 0
b = 1
h = 0.05
v = []
x = [0]
u = []
#v.append(-1 + h * uu(0, 1, -1))
#u.append(1 + h * (-1))

u.insert(0, 1)
v.insert(0, -1)
for i in range(1, 21):

    v.append(v[i-1] + h * uu(x[i-1], u[i-1], v[i-1]))
    u.append(u[i-1] + h * v[i-1])
    x.append(i * h)

w = 0
xr = []
fr = []
while w < 101:
    xr.append(w/100)
    fr.append(func(xr[w]))
    w += 1

plt.figure(1)
plt.plot(x, u)
plt.plot(xr, fr, color='red')

plt.show()