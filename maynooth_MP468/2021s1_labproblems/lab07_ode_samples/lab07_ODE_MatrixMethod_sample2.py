#!/usr/bin/env python3

"""

"""Solve the ordinary differential equation given in the question."""

"""Imports"""
import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

def solveODE(N):   
    """Range for x."""
    a = -1
    b = 1
    """Initial conditions."""
    ya = -3
    yb = 3
    """Spacing between points."""
    delta = (b-a)/N
    
    x = np.linspace(a,b,N+1) 
    
    """Create the matrix A where Ay = B. Solve for y. Using sparse matrices. Storing
    in coo format. So I am specifying the row and column of the matrix and the data 
    that is in that position."""
    row = []
    col = []
    data = []
    
    for i in range(N-1):
        row.append(i)
        col.append(i)
        data.append(10*(delta**2) - 4*x[i+1])
        if i != 0:
            row.append(i)
            col.append(i-1)
            data.append(2*x[i+1] + delta*(x[i+1]**2))
        if i != N-2:
            row.append(i)
            col.append(i+1)
            data.append(2*x[i+1] -delta*(x[i+1]**2))
    
    
    row = np.array(row)
    col = np.array(col)
    data = np.array(data)
    
    A = sparse.coo_matrix((data,(row,col)),(N-1,N-1))
    
    """Create B matrix in Ay = B"""
    B = np.zeros(N-1)
    for i in range(N-1):
        if i == 0:
            B[i] = 2*(delta**2)*(x[i+1]**2) - (2*x[i+1] + delta*(x[i+1]**2))*ya
        elif i == N-2:
            B[i] = 2*(delta**2)*(x[i+1]**2) - (2*x[i+1] - delta*(x[i+1]**2))*yb
        else:
            B[i] = 2*(delta**2)*(x[i+1]**2)
    
    """Solve Ay = B for y"""        
    y = sparse.linalg.spsolve(A,B)
    
    """Append initial conditions to y array."""
    y = np.append(np.array([ya]),y)
    y = np.append(y,np.array([yb]))
    
    return x,y




"""Plot solution for different values of N."""
N = np.array([10,50,100])

for i in range(len(N)):
    """In order to plot at x = 0 to 1. Halve the arrays."""
    start = int(N[i]/2)
    x,y = solveODE(N[i])
    plt.figure(i)
    plt.scatter(x[start:],y[start:])
    plt.title(r'Solution of $x(d^{2}y/dx^{2}) - x^{2}(dy/dx) + 5y = x^{2}$ for N = ' + str(N[i]))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('plot' + str(N[i]) + '.png')
    plt.show()
























    
