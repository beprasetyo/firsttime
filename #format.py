#print("The value of 2/3 to four decimal places is {:.4f}.".format(2/3))
#print("The radius is {}, the area is {:.3f}".format(4,3.14*4**2))
'''import math
print(math.e)
print(math.e**3)
print(math.exp(3))'''

import numpy
#print(numpy.exp(3))
#print table of trig values
print("angle |{:>5} |{:>5} |{:>5} |{:>5} |{:>5} |".format(\
    '0','\u03C0/6','\u03C0/4','\u03C0/3','\u03C0/2'))
print("------------------------------------------")
print("Cos(x)|{:.4f}|{:.4f}|{:.4f}|{:.4f}|{:.4f}|".format(\
    numpy.cos(0),numpy.cos(numpy.pi/6),numpy.cos(numpy.pi/4),\
    numpy.cos(numpy.pi/3),numpy.cos(numpy.pi/2)))
print("Sin(x)|{:.4f}|{:.4f}|{:.4f}|{:.4f}|{:.4f}|".format(\
    numpy.sin(0),numpy.sin(numpy.pi/6),numpy.sin(numpy.pi/4),\
    numpy.sin(numpy.pi/3),numpy.sin(numpy.pi/2)))