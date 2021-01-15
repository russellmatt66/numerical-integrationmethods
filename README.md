INTRODUCTION:
Hobby project as part of a larger effort on my part to learn more about numerical methods. This repository focuses on techniques for performing integration. As with all numerical routines, one of the main challenges is the error introduced by the discretization process. Real numbers are continuous and "stored mathematically" with infinite precision. To represent one digitally it must be truncated at some point in order for it to fit inside the appropriate container, like a float data type for instance. This discarded information introduces an inherent source of error into the calculation. 

FILE DESCRIPTIONS:
-"errorfunc.py": Numpy script that implements the techniques of Trapezoidal Integration and Simpson's Rule in order to calculate the value of the error function, erf(x), for a range of particular x.

-"trapezoid.py": Numpy script that implements Trapezoidal Integration to calculate the position of an object whose velocity, as a function of time, is given by the 'velocities.txt' file
-"velocities.txt": Velocity vs. Time data for "trapezoid.py" to process
