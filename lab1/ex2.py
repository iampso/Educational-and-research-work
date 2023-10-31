import numpy
a = 2
b = 2
c = - 5
h = 0.3

for x in numpy.arange(0, 3 + h, h):
    print(x)
    f = x ** a + ((b * x) ** (1 / 3)) / (c * x + a)
    print('f = ', f)
