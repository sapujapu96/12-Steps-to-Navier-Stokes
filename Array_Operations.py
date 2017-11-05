import numpy

u = numpy.array((0,1,2,3,4,5))

for i in range(1,len(u)):
	print(u[i]-u[i-1])

a = u[1:] - u[0:-1] #subtract 0th,1th,2nd... element from 1st,2nd,3rd... element


nx = 81
ny = 81
nt = 100
c  = 1
dx = 2 / (nx-1)
dy = 2 / (ny-1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))

u[int(.5/dy):int(1 / dy +1), int(.5/dx):int(1 / dx +1)] = 2

for n in range (nt+1):
	un=u.copy()
	row, col = u.shape #returns dimnesions of array u
	for j in range(1,row):
		for i in range(1,col):
			u[j,i] = (un[j,i] - (c*dt/dx *un[j,i]-un[j,i-1])) - 