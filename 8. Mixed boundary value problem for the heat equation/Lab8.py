import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def real(xt, tt):
    return xt * tt + xt * np.arccos(xt * tt / 2)


def f(xt, tt):
    return xt + (8 * tt + xt ** 2 * (xt ** 2 * tt ** 2 - tt ** 3 - 4)) / (4 - xt ** 2 * tt ** 2) ** (3 / 2)


def fi(xt):
    return np.pi * xt / 2


def nu0():
    return 0


def mu0():
    return 1


def g0(tt):
    return tt + np.pi / 2


def nu1():
    return 1


def mu1():
    return 1


def g1(tt):
    return 2 * tt + 2 * np.arccos(tt / 2) - tt / np.sqrt(4 - tt ** 2)


h = 0.1
ta = 0.005
si = 0
aa = 1

N = int(1 / h)
M = int(1 / ta)

A = - (aa ** 2 * ta * si) / (h ** 2)
B = 1 + (2 * aa ** 2 * ta * si) / (h ** 2)
C = - (aa ** 2 * ta * si) / (h ** 2)

al = nu0() - mu0() / h
be = mu0() / h
ksi = - mu1() / h
psi = nu1() + mu1() / h

a = np.zeros((M + 1, N + 1))
b = np.zeros((M + 1, N + 1))
d = np.zeros((M + 1, N + 1))
x = np.linspace(0, 1, N + 1)
t = np.linspace(0, 1, M + 1)
u = np.zeros((M + 1, N + 1))
ur = np.zeros((M + 1, N + 1))

for j in range(M + 1):
    for i in range(N + 1):
        ur[j][i] = real(x[i], t[j])

for i in range(N + 1):
    u[0][i] = fi(x[i])

for j in range(1, M + 1):
    d[j][0] = g0(t[j])
    a[j][0] = - be / al
    b[j][0] = d[j][0] / al
    for i in range(1, N):
        d[j][i] = u[j - 1][i] + (1 - si) * (aa ** 2 * ta) / (h ** 2) * (
                    u[j - 1][i + 1] - 2 * u[j - 1][i] + u[j - 1][i - 1]) + ta * f(x[i], t[j - 1])
        a[j][i] = - C / (A * a[j][i - 1] + B)
        b[j][i] = (d[j][i] - A * b[j][i - 1]) / (A * a[j][i - 1] + B)
    d[j][N] = g1(t[j])
    u[j][N] = (d[j][N] / ksi - b[j][N - 1]) / (a[j][N - 1] + psi / ksi)
    for i in range(N - 1, - 1, - 1):
        u[j][i] = a[j][i] * u[j][i + 1] + b[j][i]

x3d, t3d = np.meshgrid(x, t)
fig = pylab.figure('Вычисленное')
axes = Axes3D(fig)
axes.plot_surface(x3d, t3d, u, cmap=cm.jet)
pylab.title('Вычисленное')
axes.set_xlabel('x')
axes.set_ylabel('t')
axes.set_zlabel('U(x,t)')
fig = pylab.figure('Точное')
axes = Axes3D(fig)
axes.plot_surface(x3d, t3d, ur, cmap=cm.jet)
pylab.title('Точное')
axes.set_xlabel('x')
axes.set_ylabel('t')
axes.set_zlabel('U(x,t)')
fig = pylab.figure('Ошибка')
axes = Axes3D(fig)
axes.plot_surface(x3d, t3d, abs(ur - u), cmap=cm.jet)
pylab.title('Ошибка')
axes.set_xlabel('x')
axes.set_ylabel('t')
axes.set_zlabel('Delta U(x,t)')
pylab.figure('Слой t = T')
pylab.plot(x, ur[M][:], linestyle='dashed', color='black', marker='.', label='Точная')
pylab.plot(x, u[M][:], linestyle='solid', color='red', marker='.', label='Вычисленная')
pylab.title('Слой t = T')
pylab.xlabel('x')
pylab.ylabel('u(x,t)')
pylab.grid()
pylab.figure('Ошибка на слое t = T')
pylab.plot(x, abs(u[M][:] - ur[M][:]), linestyle='solid', color='red', marker='.')
pylab.title('Ошибка на слое t = T')
pylab.xlabel('x')
pylab.ylabel('error u(x,t)')
pylab.grid()
pylab.show()
