import matplotlib.pyplot as plt
import math


n = int(input("Введите количество узлов: "))
h = 2 / n


# Функция
def func(y):
    return (1+ math.tanh(y + y**3))

# Теоретическая производная
def derivative(v):
    a = (1 + 3 * v**2)
    b = (math.cosh(v + v**3))**2
    return a / b


# Значения функции на отрезке [-1; 1]
f_true = []
x_true = []
m = -1
while m <= 1:
    f_true.append(func(m))
    x_true.append(m)
    m += 0.005

# Узлы равномерной сетки
x = []
f = []
m = -1
while m <= 1:
    x.append(m)
    f.append(func(m))
    m += h

# Правая разностная схема
df_r = []
df_r_x = []
delta_r = []
f1=0
for i in range(n - 1):
    f1 = f[i + 1] - f[i]
    f_r = f1 / h
    df_r.append(f_r)
    df_r_x.append(x[i])
    delta_r.append(derivative(x[i]) - f_r)
# i = n-1
f1 = f[n - 1] - f[n - 1 - 1]
f_r = f1 / h
df_r.append(f_r)
df_r_x.append(x[n - 1])
delta_r.append(derivative(x[n - 1]) - f_r)

# Центральная разностная схема
df_c = []
df_c_x = []
delta_c = []
# i = 0
f1 = -3 * f[0] + 4 * f[1] - f[2]
f_c = f1 / h / 2
df_c.append(f_c)
df_c_x.append(x[0])
delta_c.append(derivative(x[0]) - f_c)
for i in range(1, n - 2):
    f1 = f[i + 1] - f[i - 1]
    f_c = f1 / h / 2
    df_c.append(f_c)
    df_c_x.append(x[i])
    delta_c.append(derivative(x[i]) - f_c)
# i = n-1
f1 = 3 * f[n - 1] - 4 * f[n - 1 - 1] + f[n - 1 - 2]
f_c = f1 / h / 2
df_c.append(f_r)
df_c_x.append(x[n - 1])
delta_c.append(derivative(x[n - 1]) - f_c)

# Левая разностная схема
df_l = []
df_l_x = []
delta_l = []
# i = 0

for i in range(1, n):
    f1 = f[i] - f[i - 1]
    f_l = f1 / h
    df_l.append(f_l)
    df_l_x.append(x[i])
    delta_l.append(derivative(x[i]) - f_l)

# Вычисление второй производной со 2-ым порядком точности
d2f2 = []
d2f2_x = []
for i in range(1, n - 1):
    f1 = f[i + 1] - 2 * f[i] + f[i - 1]
    x1 = (x[i + 1] - x[i]) ** 2
    d2f2_f = f1 / x1
    d2f2.append(d2f2_f)
    d2f2_x.append(x[i])

# Вычисление второй производной с 4-ым порядком точности
d2f4 = []
d2f4_x = []
for i in range(2, n - 2):
    f1 = - f[i + 2] + 16 * f[i + 1] - 30 * f[i] + 16 * f[i - 1] - f[i - 2]
    x1 = 12 * (x[i + 1] - x[i]) ** 2
    d2f4_f = f1 / x1
    d2f4.append(d2f4_f)
    d2f4_x.append(x[i])
%matplotlib inline
# Графики
fig1 = plt.figure(1)

# Истинная функция
plt.subplot(331)
plt.plot(x_true, f_true, 'r')

# Значения в узлах интерполяции
plt.subplot(332)
plt.scatter(x, f, color='b', marker='.')

# Правые разности
plt.subplot(336)
plt.plot(df_r_x, df_r, 'g')

# Центральные разности
plt.subplot(335)
plt.plot(df_c_x, df_c, 'b')

# Левые разности
plt.subplot(334)
plt.plot(df_l_x, df_l, 'r')

# Вторая производная 2-го порядка точности
plt.subplot(337)
plt.plot(d2f2_x, d2f2, 'r')

# Вторая производная 4-го порядка точности
plt.subplot(338)
plt.plot(d2f4_x, d2f4, 'b')

fig2 = plt.figure(2)

# Ошибка правых разностей
plt.subplot(313)
plt.plot(df_r_x, delta_r, 'g')

# Ошибка центральных разностей
plt.subplot(312)
plt.plot(df_c_x, delta_c, 'b')

# Ошибка левых разностей
plt.subplot(311)
plt.plot(df_l_x, delta_l, 'r')

plt.show()
