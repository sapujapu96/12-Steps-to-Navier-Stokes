import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D


nx = 41
ny = 41
dx = 2 / (nx -1)
dy = 2 / (ny -1)


x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,1,ny)
X, Y = numpy.meshgrid(x,y)

p = numpy.zeros((ny,nx))

p[:,0] = 0
p[:,-1] = 0
p[0,:] = 0
p[-1,:] = 0




def laplace2d (p,y,dx,dy,l1norm_target):
	l1norm=1
	pn = numpy.empty_like(p)

	while l1norm > l1norm_target:
		pn = p.copy()
		p[1:-1,1:-1] = (dy**2 * (p[1:-1,2:] + p[1:-1,0:-2]) + dx**2 * (p[2:,1:-1] + p[0:-2,1:-1]))/(2*(dx**2 + dy**2))

		p[:,0] = 0
		p[:,-1] = 0
		p[0,:] = 0
		p[-1,:] = 0
		p[20,20]=5
		l1norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pn[:])) / numpy.sum(numpy.abs(pn[:])))
	return p

p = laplace2d(p,y,dx,dy,1e-4)
print(p)



def plot2D(x, y, p):
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225) 
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    pyplot.show()

plot2D(x,y,p)

