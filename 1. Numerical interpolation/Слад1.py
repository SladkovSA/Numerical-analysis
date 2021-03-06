import matplotlib.pyplot as plt
import math as mh

n = int(input("Введите количество узлов: "))
h = 10 / n
""" задание функции
   из варианта"""
def func(y):
    return 2**(mh.cos(y) - mh.sin(y)) * mh.cos(1+mh.log(1+y))
""" Вычисление функции 
   в узлах функции """
x_gr = []
f_gr = []
for i in range(n):
    t = 10 * i / (n - 1)
    x_gr.append(t)
    f_gr.append(func(t))
"""Задание интерполяционного 
   полинома Лагранжа"""
def lagrange(r):
    lagr= 0
    for m in range(len(f_gr)):
        l1 = 1
        l2 = 1
        for j in range(len(x_gr)):
            if j != m:
                l1 *= r - x_gr[j]
                l2 *= x_gr[m] - x_gr[j]
        lagr += f_gr[m] * l1 / l2
    return lagr


x1 = []
x2 = []
f_a = []      # Объявление динамических масссивов
L_a = []
f_err_a1 = []
f_err_a2 = []
""" Построение функции """
for i in range(1000):
    t = 10 * i / 999
    y1 = func(t)
    x1.append(t)
    f_a.append(y1)

    la1 = lagrange(t)
    L_a.append(la1)

    f_err_a2.append(abs(y1 - la1))

for x in x_gr:
    yt = func(x)
    yi = lagrange(x)
    f_err_a1.append(abs(yt - yi))

print('Максимум ошибки: ', max(f_err_a2))

plt.figure(1)
plt.plot(x_gr, f_gr, color='black', linestyle='none', marker='x')
plt.plot(x1, f_a, color='blue', linestyle='solid', label='Функция')
plt.plot(x1, L_a, color='red', linestyle='dashed', label='Интерполяция')
plt.legend()
plt.axis(xmin=0, xmax=10)
plt.axis(ymin=min(L_a) - 0.25, ymax=max(f_a) + 0.25)
plt.title('Равномерная интерполяционная сетка')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.figure(2)
plt.plot(x_gr, f_err_a1, color='black', linestyle='none', marker='x')
plt.plot(x1, f_err_a2, color='red', linestyle='solid')
plt.axis(xmin=0, xmax=10)
plt.axis(ymin=min(f_err_a2), ymax=max(f_err_a2))
plt.title('Значение ошибки при равномерной интер. сетке')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.show()
