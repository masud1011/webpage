import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import pdb

def gaussbc(t,x0,t0,D):
    return np.sqrt(t0/t)*np.exp(-0.25*x0*x0/(D*t))


def ftcs_driver(dt,tmax):
    """
    Solve the 1+1-dimensional diffusion equation
    using the FTCS scheme, with time step dt up to time tmax
    """
    t0 = 0.1        # initial time
    D  = 1          # diffusion constant
    dx = 0.05       # grid spacing
    x1 = -5         # left boundary
    x2 = 5          # right boundary
    x  = np.arange(x1, x2, dx)   # set up vector of x-values
    t  = np.arange(t0, tmax, dt) # set up vector of y-values
    u0 = np.exp(-x*x/(4*t0))  # initial distribution
    bc1 = gaussbc  # boundary value function on left boundary
    bc2 = gaussbc  # boundary value function on right boundary    

    nt = len(t)
#    nx = len(x)
    u = 0*x         # initialise u to vector of zeros

    def update_plot(num):
        u[0] = bc1(t[num],x1,t0,D)  # apply boundary condition
        # the next line is the evolution equation
        u[1:-1] = u0[1:-1] + D*dt/(dx*dx)*(u0[:-2]-2*u0[1:-1]+u0[2:])
        u[-1] = bc2(t[num],x2,t0,D) # apply boundary condition
        u0[:] = u # save distribution for use in next step
        plt.cla()
        plt.title('t=' + str(t[num]))
        plt.plot(x,u)
        plt.ylim((0.0, 1.0))

    fig = plt.figure()    
    return animation.FuncAnimation(fig, update_plot, nt, interval=1, repeat=False)

# fill in sensible values here
my_animation = ftcs_driver(0.0015, 1)



