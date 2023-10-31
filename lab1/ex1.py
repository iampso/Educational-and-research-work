import math

print('Введите x, y, z')

x = int(input())
y = int(input())
z = int(input())
a = (((abs(x - 1))   ** (1 / 2)) - (abs(y)) ** (1 / 2)) / (1 + ((x ** 2) / 2) + (y ** 2) / 4)
print('a = ', a)

b = x * (math.atan(z) + 5)
print('b = ', b)
