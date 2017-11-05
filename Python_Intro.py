import numpy
from matplotlib import pyplot

myarray = numpy.linspace(0,5,10)
print(myarray)

a=5
b='five'
c=5.0

type(a)
type(b)
type(c)
print(type(a))
print(type(b))
print(type(c))

for i in range(5):
	print("Hi \n")

for i in range(3):
	for j in range(3):
		print(i,j)


myvals = numpy.array([1,2,3,4,5])
print(myvals)
print(myvals[0])

print(myvals[0:3])

a = numpy.linspace(1,5,5)

b=a


a[2]=17

c=a.copy()

a[2]=3

print(a)
print(c)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show() 