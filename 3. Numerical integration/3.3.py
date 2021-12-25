# Программа №3 (3.1)
import math as mt
import matplotlib.pyplot as plt


def func(j):
    return 1 / (j ** 3 + j + 10)


ir = 0.20179100954186575465595019741395596694301378
n = input('Максимальное число узлов - ')
n = int(n)
a = -1
b = 1
err1 = []
err2 = []
err3 = []
err4 = []
il = 0
irr = 0
cr = 0
trap = 0
v = -1
h = []
z = 0
# Метод левых прямоугольников

for d in range(2, n):
    h.append(2 / d)
    x = []
    v = -1
    while v < 1:
        x.append(v)
        v += h[z]
    x.append(1)
    il = 0
    irr = 0
    cr = 0
    trap = 0
    s = 0
    #s0 = 0
    for k in range(d):
        il += h[z] * func(x[k])
        irr += h[z] * func(x[k + 1])
        trap += (func(x[k + 1]) + func(x[k])) * h[z] / 2
        cr += func(x[k] + h[z] / 2) * h[z]
    err1.append(abs(il - ir))
    err2.append(abs(irr - ir))
    err3.append(abs(cr - ir))
    err4.append(abs(trap - ir))
    #s0 = h[z] * (func(x[0]) + func(x[d])) / 2

    #for k in range(0, len(x) - 2, 2):
        #s += h[z] * func(x[k])
        #s += h[z] / 3 * (func(x[k-1]) + 4 * func(x[k]) + func(x[k + 1]))
    #s = s + s0
    #err5.append(abs(s - ir))
    z += 1

print("Методом левых прямоугольников: " + str(il))
print("Правых: I = " + str(irr))
print("Средних: I = " + str(cr))
print("Трапеций: I = " + str(trap))
print("Теоритическое значение I = "+ str(ir))

plt.figure(1)

plt.subplot(411)
plt.plot(h, err1, 'b')

plt.subplot(412)
plt.plot(h, err2, 'r')

plt.subplot(413)
plt.plot(h, err3, 'y')

plt.subplot(414)
plt.plot(h, err4, 'g')
plt.show()
