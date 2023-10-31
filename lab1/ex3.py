import math
import numpy

m = 1
n = 3
h = 0.1

for x in numpy.arange(m, n + h, h):
    print('x = ', x)
    f = ((math.sin(x) + math.cos(x)) / (math.cos(x) - math.sin(x))) * math.tan(x)
    print('f = ', f)


