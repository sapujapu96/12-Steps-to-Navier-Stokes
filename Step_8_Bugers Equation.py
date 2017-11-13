import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

nx = 41
ny = 41
nt = 3000
c  = 1
dx = 2 / (nx -1)
dy = 2 / (ny -1)
sigma = 0.0009
nu = 0.01
dt = sigma * dx * dy / nu

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)
X, Y = numpy.meshgrid(x,y)

u = numpy.zeros((ny,nx))
v = numpy.zeros((ny,nx))
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))

u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 3 
v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 1


fig1 = pyplot.figure(figsize=(11,7),dpi=100)
ax1 = fig1.gca(projection='3d')
surf = ax1.plot_surface(X, Y, u[:], cmap=cm.viridis, rstride=1, cstride=1)
surf = ax1.plot_surface(X, Y, v[:], cmap=cm.viridis, rstride=1, cstride=1)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')



for n in range(nt+1):
	un = u.copy()
	vn = v.copy()

	u[1:-1,1:-1] = 	(un[1:-1,1:-1] - 
					dt/dx * un[1:-1,1:-1] * (un[1:-1,1:-1] - un[1:-1,0:-2]) - 
					dt/dy * vn[1:-1,1:-1] * (un[1:-1,1:-1] - un[0:-2,1:-1]) + 
	 				nu*dt/dx**2 * (un[1:-1,2:] - 2*un[1:-1,1:-1] + un[1:-1,0:-2]) + 
	 				nu*dt/dy**2 * (un[2:,1:-1] - 2*un[1:-1,1:-1] + un[0:-2,1:-1]))

	v[1:-1,1:-1] = 	(vn[1:-1,1:-1] - dt/dx * un[1:-1,1:-1] * (vn[1:-1,1:-1] - vn[1:-1,0:-2]) - dt/dx * vn[1:-1,1:-1] * (vn[1:-1,1:-1] - vn[0:-2,1:-1]) + 
					nu*dt/dx**2 * (vn[1:-1,2:] - 2*vn[1:-1,1:-1] + vn[1:-1,0:-2]) + nu*dt/dy**2 * (vn[2:,1:-1] - 2*vn[1:-1,1:-1] + vn[0:-2,1:-1]))


u[0,:] = 0
u[-1,:] = 0
u[:,0] = 0
u[:,-1] =0

v[0,:] = 0
v[-1,:] = 0
v[:,0] = 0
v[:,-1] = 0

fig2 = pyplot.figure(figsize=(11,7),dpi=100)
ax2 = fig2.gca(projection='3d')
surf = ax2.plot_surface(X, Y, u[:], cmap=cm.viridis, rstride=1, cstride=1)
surf = ax2.plot_surface(X, Y, v[:], cmap=cm.viridis, rstride=1, cstride=1)
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
pyplot.show()
