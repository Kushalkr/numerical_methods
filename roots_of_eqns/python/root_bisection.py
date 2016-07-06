from math import tan
from bisect import *
from rootsearch import *


f = lambda x: x - tan(x)

a, b, dx = (0, 20, 0.01)

print 'The roots are:'

while True:
    x1, x2 = rootsearch(f, a, b, dx)

    if x1 != None:
        a = x2
        root = bisect(f, x1, x2, 1)
        if root != None: print root
    else:
        print '\ndone!'
        break
raw_input('Press return to exit')
