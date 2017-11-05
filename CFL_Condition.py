import numpy
from matplotlib import pyplot

def linearconv(nx):
	dx = 2 / (nx-1)
	nt = 20
	dt = 0.025
	c  = 1

	u = numpy.ones(nx)
	u[int(.5/dx):int(1/dx + 1)] = 2

	un=numpy.ones(nx)

	for n in range(nt): #iterates through time
		un = u.copy()
		for i in range(1,nx): #iterates through array
			u[i] = un[i] - c * dt/dx * (un[i]-un[i-1])

	pyplot.figure(1)
	pyplot.plot(numpy.linspace(0,2,nx),u);
	

linearconv(41)


#at 85 gridpoints, the hat function breaks
#reason: gridpoints became so small, that wave traveled a greater distance than dx in timestep dt
#this leads to a wrong estimate of the speed of the wave

#solution: implementation of a Courant number which adjusts the size of the time step dt depending on the grid length dx

def linearconv_fixed(nx):
	dx = 2 / (nx-1)
	nt = 20
	c  = 1
	sigma = 0.5 #Courant number

	dt = sigma * dx #time step size is now dependent on size of dx

	u = numpy.ones(nx)
	u[int(.5 /dx):int(1 /dx +1)] =2

	un = numpy.ones(nx)

	for n in range(nt):
		un=u.copy()
		for i in range(1,nx):
			u[i] = un[i] - c * dt/dx * (un[i]-un[i-1])

	pyplot.figure(2)
	pyplot.plot(numpy.linspace(0,2,nx),u)
	pyplot.show()

linearconv_fixed(1001)