# Программма4
# метод Ньютона
import math as mt
def func(t):
    return mt.tan(t / 4 - 1) + t ** 2 - 5 * t - 3
def derivative(y):
    return 1/(4*mt.tan(y/4-1))+2*y-5
eps = 1E-3
a = float(0)
b = float(10)
x0 = b
x1 = 0
x = x0
i = 1
while abs(func(x)) > eps:
    x1 = x0 - func(x0)/derivative(x0)
    x0=x1
    x = x0
    i+=1
print("Корень при eps = 10^-3 - " + str(x))
print("Количество итерация - " + str(i))


def func(t):
    return mt.tan(t / 4 - 1) + t ** 2 - 5 * t - 3
def derivative(y):
    return 1/(4*mt.tan(y/4-1))+2*y-5
eps = 1E-6
a = float(0)
b = float(10)
x0 = b
x1 = 0
x = x0
i = 1
while abs(func(x)) > eps:
    x1 = x0 - func(x0)/derivative(x0)
    x0=x1
    x = x0
    i+=1
print("Корень при eps = 10^-6 - " + str(x))
print("Количество итерация - " + str(i))

def func(t):
    return mt.tan(t / 4 - 1) + t ** 2 - 5 * t - 3
def derivative(y):
    return 1/(4*mt.tan(y/4-1))+2*y-5
eps = 1E-9
a = float(0)
b = float(10)
x0 = b
x1 = 0
x = x0
i = 1
while abs(func(x)) > eps:
    x1 = x0 - func(x0)/derivative(x0)
    x0=x1
    x = x0
    i+=1
print("Корень при eps = 10^-9 - " + str(x))
print("Количество итерация - " + str(i))