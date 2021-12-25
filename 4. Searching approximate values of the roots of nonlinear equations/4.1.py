# Программма4
# метод дихотомии
import math as mt


def func(t):
    return mt.tan(t / 4 - 1) + t ** 2 - 5 * t - 3


eps = 1E-3
a = float(0)
b = float(10)
x = (a + b) / 2
i = 1
while abs(func(x)) > eps:
    x = (a + b) / 2
    if func(a) * func(x) < 0:
        b = x
    elif func(x) * func(b) < 0:
        a = x
    i+=1
print("Корень при eps = 10^-3 - " + str(x))
print("Количество итерация - " + str(i))

eps = 1E-6
a = float(0)
b = float(10)
x = (a + b) / 2
i = 1
while abs(func(x)) > eps:
    x = (a + b) / 2
    if func(a) * func(x) < 0:
        b = x
    elif func(x) * func(b) < 0:
        a = x
    i+=1
print("Корень при eps = 10^-6 - " + str(x))
print("Количество итерация - " + str(i))

eps = 1E-9
a = float(0)
b = float(10)
x = (a + b) / 2
i = 1
while abs(func(x)) > eps:
    x = (a + b) / 2
    if func(a) * func(x) < 0:
        b = x
    elif func(x) * func(b) < 0:
        a = x
    i+=1
print("Корень при eps = 10^-9 - " + str(x))
print("Количество итерация - " + str(i))