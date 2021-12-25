# Программа №3 (3.2)
import math as mt
import matplotlib.pyplot as plt
def func(j):
    return 1 / (j ** 3 + j + 10)


ir = 0.20179100954186575465595019741395596694301378
n = input('Максимальное число узлов - ')
n = int(n)
a = -1
b = 1
err5 = []
il = 0
irr = 0
cr = 0
trap = 0
v = -1
h = []
hs = []
z = 0
# Метод левых прямоугольников

for d in range(2, n, 2):
    h.append(2 / d)
    hs.append(4 / d)
    x = []
    v = -1
    while v < 1:
        x.append(v)
        v += h[z]
    x.append(1)
    s = 0
    # s0 = 0
    # s0 = h[z] * (func(x[0]) + func(x[d])) / 2

    for k in range(0, len(x) - 2, 2):
        # s += h[z] * func(x[k])
        s += h[z] / 3 * (func(x[k]) + 4 * func(x[k + 1]) + func(x[k + 2]))
    # s = s + s0
    err5.append(abs(s - ir))
    z += 1
print("Методом Симпсона: I = " + str(s))
print("Теоритическое значение I = " + str(ir))
plt.figure(2)
plt.plot(hs, err5, 'g')
plt.show()
