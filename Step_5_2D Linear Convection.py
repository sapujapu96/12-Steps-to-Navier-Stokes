from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import pyplot, cm

nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx-1)
dy = 2 / (ny - 1)
sigma = .2
dt = sigma * dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u1 = numpy.ones((ny,nx))
un1 = numpy.ones ((ny,nx))

u1[int(.5/dy):int(1 / dy +1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt+1):
	un1 = u1.copy()
	row,col = u1.shape
	for j in range(1,row):
		for i in range(1,col):
			u1[i,j] = (un1[j,i] - (c * dt/dx * (un1[j,i] - un1[j,i-1])) -
								(c * dt/dx * (un1[j,i] - un1[j-1,i])))

			u1[0,:] = 1
			u1[-1,:] = 1  #-1 means last element
			u1[:,0] = 1
			u1[:,-1] = 1




fig = pyplot.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(X,Y,u1[:],cmap=cm.viridis)


u2 = numpy.ones((ny,nx))
un2 = numpy.ones ((ny,nx))
u2[int(.5/dy):int(1 / dy +1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt+1):
	un2=u2.copy()
	u2[1:,1:] = (un2[1:,1:]- (c*dt/dx* (un2[1:,1:] - un2[1:,:-1]))-
						   (c*dt/dx* (un2[1:,1:] - un2[:-1,1:])))

	u2[0,:] = 1
	u2[-1,:] = 1
	u2[:,0] = 1
	u2[:,-1] = 1	


fig = pyplot.figure(figsize=(11,7),dpi = 100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(X,Y,u2[:], cmap=cm.viridis)
#pyplot.show()

