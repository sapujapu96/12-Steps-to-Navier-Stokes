from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot, cm
import numpy

nx = 101
ny = 101
nt = 80
c  = 1
dx = 2 / (nx - 1)
dy = 2 / (nx - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)
X,Y = numpy.meshgrid(x,y)

u = numpy.ones((ny,nx))
v = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))

u[int(.5/dy):int(1/dy +1), int(.5/dx):int(1/dx+1)] = 2   #two coupled functions for 2D nonlinear convection
v[int(.5/dy):int(1/dy +1), int(.5/dx):int(1/dx+1)] = 2

fig = pyplot.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=2,cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$') 



for n in range(nt+1):
	un=u.copy()
	vn=v.copy()
	u[1:,1:] = (un[1:,1:] - (un[1:,1:] * c*dt/dx* (un[1:,1:] - un[1:,:-1]))-
							vn[1:,1:] * c*dt/dy* (un[1:,1:] - un[:-1,1:]))
	v[1:,1:] = (vn[1:,1:] - (un[1:,1:] * c*dt/dx* (vn[1:,1:] - vn[1:,:-1]))-
							vn[1:,1:] * c*dt/dy* (vn[1:,1:] - vn[:-1,1:]))

	u[0, :] = 1
	u[-1, :] = 1
	u[:, 0] = 1
	u[:, -1] = 1
	v[0, :] = 1
	v[-1, :] = 1
	v[:, 0] = 1
	v[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax2 = fig.gca(projection='3d')


surf2=ax2.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
pyplot.show()