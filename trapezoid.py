"""
Matt Russell
Program demonstrating trapezoidal rule on dataset representing velocity of a particle at discrete points in time
12/22/20
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("velocities.txt",float) # Column 0 is times (integers), Col 1 is velocities (floats)

N = data.shape[0] # both columns are same length, otherwise loadtxt does not work
a = data[0,0].astype(int) # t_{0} = 0
b = data[N-1,0].astype(int) # t_{f}, shape returns size so have to subtract 1 to properly index
h = (b-a)/N

x_t = np.zeros((N,1),dtype=float) # integral will be real-valued so represent w/float
x_t[a,0] = data[a,1]

for k in np.arange(N-1):
    x_t[k+1,0] = x_t[k,0] + data[a+(k+1),1] #velocities, h is absent because it is a float

x_t[N-1,0] = h*(x_t[N-2,0] + (0.5)*data[a,1] + (0.5)*data[b,1]) # final step

"""
Plotting
"""
resultsFig, axs = plt.subplots(2,1)

ax = axs[0]
ax.plot(data[:,0],data[:,1],'bo',label='velocity')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Velocity (units/s)')
ax.set_title('v(t)')

ax = axs[1]
ax.plot(data[:,0],x_t,'ro',label='position')
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Position (units)')
ax.set_title('Approximate x(t)')

resultsFig.suptitle('Trapezoidal integration of velocity data to approximate position')
plt.subplots_adjust(hspace = 0.5)

plt.show()
