#                                             Программа 6
import math as mt
import matplotlib.pyplot as plt


def func(j):
    return j ** 2 + mt.exp(-mt.tan(j))


def p(xj):
    return 1 / (mt.cos(xj)) ** 2


def q(xj):
    return 2 * mt.tan(xj) / (mt.cos(xj)) ** 2


a = 0
b = 1
h = 0.005
x = []
Real = []
for i in range(int((b - a) / h)):
    x.append(i * h)
    Real.append(func(x[i]))
x.append(1)
Real.append(func(x[-1]))
A = [1]
B = [0]
C = [0]
d = [1]
for m in range(1, int((b - a) / h)):
    A.append(1 / h ** 2 - p(x[m]) / (2 * h))
    B.append(-2 / h ** 2 + q(x[m]))
    C.append(1 / h ** 2 + p(x[m]) / (2 * h))
    d.append(2 + 2 * x[m] * (1 + x[m] * mt.tan(x[m])) / (mt.cos(x[m])) ** 2)
A.append(0)
B.append(1 / h)
C.append(1 - 1 / h)
d.append(-0.0676)

a = [-B[0] / A[0]]
b = [d[0] / A[0]]
for m in range(1, int(1 / h) + 1):
    a.append(- C[m] / (A[m] * a[m - 1] + B[m]))  # a1
    b.append((d[m] - A[m] * b[m - 1]) / (A[m] * a[m - 1] + B[m]))  # b1

# U = []
# Ur = []  # ошибка
# U.insert(0, (d[int(1 / h)] / B[int(1 / h)] - b[int(1 / h) - 1]) / (
#        a[int(1 / h) - 1] + C[int(1 / h)] / B[int(1 / h)]))
# Ur.insert(0, abs(Real[int(1 / h)] - U[0]))
# U.insert(0, a[m] * U[0] + b[m])
# Ur.insert(0, abs(Real[int(1 / h)-1] - U[0]))
# for m in range(int(1 / h) - 1, 0, - 1):
#    U.insert(0, a[m] * U[1] + b[m])
#    Ur.insert(0, abs(Real[m-1] - U[0]))

U = []
Ur = []
Ui = (d[int(1 / h)] / B[int(1 / h)] - b[int(1 / h) - 1]) / (a[int(1 / h) - 1] + C[int(1 / h)] / B[int(1 / h)])
U.insert(0, Ui)
Ur.append(abs(Real[int(1 / h)] - Ui))
for m in range(int(1 / h) - 1, - 1, - 1):
    Ui = a[m] * U[0] + b[m]
    U.insert(0, Ui)
    Ur.insert(0, abs(Real[m] - Ui))



plt.figure(1)
plt.title('Графики функции')
plt.xlabel('X')
plt.ylabel('U')
plt.plot(x, Real, color='blue', label='Теоритическая')
plt.plot(x, U, color='red', label='Вычисленная')
plt.legend()
plt.figure(2)
plt.title('График ошибки')
plt.xlabel('X')
plt.ylabel('Ur')
plt.plot(x, Ur, color='yellow')

plt.show()
