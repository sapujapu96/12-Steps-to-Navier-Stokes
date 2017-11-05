import numpy
from matplotlib import pyplot
import time, sys

nx = 41
dx = 2 / (nx-1)
nt = 25
dt = 0.025
c  = 1

u = numpy.ones(nx)
u[int(0.5/dx):int(1/dx+1)] = 2 # setting u = 2 between 0.5 and 1, initial conditions




#initialize temporary array for the n+1 timestep
un = numpy.ones(nx)

for n in range (nt):
	un = u.copy() #copy existing array u into temporary array un
	for i in range(1,nx):
	#for i in range(nx):
		u[i] = un[i] - c * dt /dx * (un[i] - un[i-1])

print(u)
pyplot.plot(numpy.linspace(0,2,nx),u)
pyplot.show()