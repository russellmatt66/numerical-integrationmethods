"""
Matt Russell
Python program to evaluate error function using Trapezoidal and Simpson's Rule
12/22/20
"""
def f(t):
    return np.exp(-(t**2))

import numpy as np
import matplotlib.pyplot as plt

xi = -3
xf = 3
deltax = 0.1
Nx = int((xf - xi)/deltax) # total number of points I want to integrate

print(type(Nx))

x = np.empty((Nx,1),dtype=float)
erfx_trap = np.zeros((Nx,3),dtype=float) #  array to hold values from trapezoidal evaluation
erfx_simp = np.zeros((Nx,3),dtype=float) # array to hold values from simpson's rule evaluation

x = np.linspace(xi,xf,num=Nx)


print(x.shape)
print(type(x))
"""
print(erf_x.shape)
print(type(erf_x))
"""

#I_trap = 0.0
#I_simp = 0.0

Nslices = [10,100,1000]
j = 0
a = 0.0

for n in Nslices:
    for i in range(0,Nx): # for loop to calculate erf(x) for each x
        b = x[i] # get the current value of x that we want to calculate erf for
        h = float((b - a)/n) # x will change each loop so the step-size needs to reflect this
        #print(b)
        #print(h)
        for k_odd in range(0,n,2): # odd terms for Simpson's Rule
            #erfx_simp[i,j] = erfx_simp[i,j] + 4*f(a+k_odd*h)
            erfx_simp[i,j] = erfx_simp[i,j] + 4*np.exp(-(a+k_odd*h)**2)
        for k_even in range(1,n,2): # even terms for Simpson's Rule
            #erfx_simp[i,j] = erfx_simp[i,j] + 4*f(a+k_odd*h)
            erfx_simp[i,j] = erfx_simp[i,j] + 2*np.exp(-(a+k_even*h)**2)
        for k_trap in range(0,n):
            #erfx_simp[i,j] = erfx_simp[i,j] + 4*f(a+k_odd*h)
            erfx_trap[i,j] = erfx_trap[i,j] + np.exp(-(a+k_trap*h)**2)
        erfx_simp[i,j] = (2/np.sqrt(np.pi))*(1/3)*h*(f(a) + f(b) + erfx_simp[i,j])
        erfx_trap[i,j] = (2/np.sqrt(np.pi))*h*(0.5*f(a) + 0.5*f(b) + erfx_trap[i,j])
    j = j+1

"""
Plotting
"""
resultsFig, axs = plt.subplots(2,1)

simpax = axs[0]
for s in range(erfx_simp.shape[1]):
    simpax.plot(x,erfx_simp[:,s])

trapax = axs[1]
for t in range(erfx_trap.shape[1]):
    trapax.plot(x,erfx_trap[:,t])

plt.show()
