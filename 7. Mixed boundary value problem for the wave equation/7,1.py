import pylab
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def real(xt, tt):
    return 1 / 2 * np.sinh(1 + tt - xt)


def f(xt, tt):
    return 1 / 4 * np.sinh(1 + tt - xt)


def fi(xt):
    return 1 / 2 * np.sinh(1 - xt)


def psi(xt):
    return 1 / 2 * np.cosh(1 - xt)


def g0(tt):
    return 1 / 4 * (np.exp(1 + tt) - 3 * np.exp(-1 - tt))


def gl(tt):
    return 1 / 2 * np.exp(tt)


h = 0.05
ta = 0.05

kur = ta / (h * np.sqrt(2))
N = int(1 / h)
L = int(1 / ta)

x = np.linspace(0, 1, N + 1)
t = np.linspace(0, 1, L + 1)
u = np.zeros((L + 1, N + 1))
ur = np.zeros((L + 1, N + 1))

for j in range(L + 1):
    for i in range(N + 1):
        ur[j][i] = real(x[i], t[j])

for i in range(1, N):
    u[0][i] = fi(x[i])
    u[1][i] = u[0][i] + ta * psi(x[i])
u[0][0] = (g0(t[0]) - 1 / h * u[0][1]) / (2 - 1 / h)
u[0][N] = (gl(t[0]) - 1 / h * u[0][N - 1]) / (1 - 1 / h)
u[1][0] = (g0(t[1]) - 1 / h * u[1][1]) / (2 - 1 / h)
u[1][N] = (gl(t[1]) - 1 / h * u[1][N - 1]) / (1 - 1 / h)

for j in range(1, L):
    for i in range(1, N):
        u[j + 1][i] = 2 * u[j][i] - u[j - 1][i] + kur ** 2 * (u[j][i + 1] - 2 * u[j][i] + u[j][i - 1]) + ta ** 2 * f(
            x[i], t[j])
    u[j + 1][0] = (g0(t[j + 1]) - 1 / h * u[j + 1][1]) / (2 - 1 / h)
    u[j + 1][N] = (gl(t[j + 1]) + 1 / h * u[j + 1][N - 1]) / (1 - 1 / h)

# print(u, end='\n\n')
# print(ur)


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
pylab.plot(x, ur[L][:], linestyle='dashed', color='black', marker='.', label='Точная')
pylab.plot(x, u[L][:], linestyle='solid', color='red', marker='.', label='Вычисленная')
pylab.title('Слой t = T')
pylab.xlabel('t')
pylab.ylabel('u(x,t)')
pylab.legend()
pylab.grid()
pylab.figure('Ошибка на слое t = T')
pylab.plot(x, abs(u[L][:] - ur[L][:]), linestyle='solid', color='red', marker='.')
pylab.title('Ошибка на слое t = T')
pylab.xlabel('t')
pylab.ylabel('error u(x,t)')
pylab.grid()
pylab.show()
