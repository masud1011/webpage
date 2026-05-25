
'''
solving ODE Using matrix equation
x*y'' - x^2*y' + 5*y = x^2 on the interval [-1,1]
for varying N (10,50 and 100) and plotting y(x) for x in [0,1]

'''
import numpy as np
import matplotlib.pyplot as plt
#boundary conditions
a = -1
b = 1
Ya = -3
Yb = 3

#Solve ode for y(x) for varying N and plot solutions with labels
for N in [10,50,100]:
    #initialise variables
    dx = (b-a)/N
    x_array = np.linspace(a,b,N+1)
    
    #Set up Matrices
    A_mat = np.zeros([N-1,N-1])
    
    #using symmetric first derivative and 2nd derivative
    for i in range(N-1):
        for j in range(N-1):
            #diagonal
            if(i==j):
                A_mat[i][j] = (5*dx*dx- 2*x_array[i+1])
                
            #lower diagonal
            elif(j+1 == i):
                A_mat[i][j] = x_array[i+1]**2*dx/2 +x_array[i+1] 
                
            #upper diagonal
            elif(j-1 == i):
                A_mat[i][j] = x_array[i+1] - x_array[i+1]**2*dx/2
                
    #Setting up b vector
    b_vec = np.zeros([N-1]) # initial array of zeros
    b_vec[0] = (x_array[1]**2)*(dx**2) - Ya # first value of b (f_1 - y(-1))

    #Inermediary values f_1  to f_N-2
    for i in range(1,N-1):
        b_vec[i] = (x_array[i+1]**2)*(dx**2)
        
    # final valyue of b (f_N-1 - y(1))    
    b_vec[-1] = (x_array[N-1]**2)*(dx**2) - Yb
    
    #solving for y(x)
    ans = np.linalg.solve(A_mat,b_vec)
    
    #plotting solution for x \in [0,1]
    y_plt = []
    y_plt.append(ans[(N-1)//2]) # x == 0
    
    for i in range((N+1)//2,N-1):
        y_plt.append(ans[i])  # x = i*dx
    y_plt.append(Yb) # x == 1
    
    #plot graph of approximate solution for interval [0,1]
    title = 'Approximate Solution of y(x) for N'
    sol_N = 'N = ' + str(N)
    
    plt.plot(x_array[(N+1)//2:],y_plt,label = sol_N)
    plt.title(title)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.grid(True)
    







