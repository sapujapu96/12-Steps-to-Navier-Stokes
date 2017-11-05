import numpy
from matplotlib import pyplot

nx = 321
dx = 2 / (nx-1)
nt=100
dt=0.003125

u = numpy.ones(nx)
u[int(0.5/dx):int(1/dx + 1)] = 2

un = numpy.ones(nx)

for n in range (nt):  #iterate through time
	un=u.copy()
	for i in range(1,nx): #iterate through array

		u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

pyplot.plot(numpy.linspace(0,2,nx),u)
pyplot.show()