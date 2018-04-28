#imports
import numpy as np
import matplotlib.pyplot as plt

#declare constants
dt = 10.**-2		#some shit timestep [s]
m = 0.500		#mass of 500 g [kg]
k = 1. 			#stiffness constant [N/m]
x0 = 1. 			#start position [m]
v0 = 0. 			#start velocity [m/s]
T = 20. 			#total time [s]
N = int(T/dt) 	

#setting initialconditions
x = np.zeros(N); v = np.zeros(N); t = np.zeros(N)
x[0] = x0; v[0] = v0



#making functions for this bitch
"""
the function we have is 
mx''(t) + kx(t) = 0
x''(t) = kx(t)/m

"""

def f(x,v,t):
	a = -k*x/m 
	return a

def diffEQ(xNow,vNow,tNow):
	aNow = f(xNow,vNow,tNow)
	return aNow

# The Runge Kutta method
def RK4(xStart,vStart,tStart):
	a1 = diffEQ(xStart,vStart,tStart)
	v1 = vStart

	xHalf1 = xStart + v1 * dt/2.0
	vHalf1 = vStart + a1 * dt/2.0

	a2 = diffEQ(xHalf1,vHalf1,tStart+dt/2.0)
	v2 = vHalf1

	xHalf2 = xStart + v2 * dt/2.0
	vHalf2 = vStart + a2 * dt/2.0

	a3 = diffEQ(xHalf2,vHalf2,tStart+dt)
	v3 = vHalf2

	xEnd = xStart + v3 * dt
	vEnd = vStart + a3 * dt

	a4 = diffEQ(xEnd,vEnd,tStart+dt)
	v4 = vEnd

	aMiddle = 1.0/6.0 * (a1+2*a2+2*a3+a4)
	vMiddle = 1.0/6.0 * (v1+2*v2+2*v3+v4)

	xEnd = xStart + vMiddle*dt
	vEnd = vStart + aMiddle*dt

	return xEnd, vEnd

#running the loop for shit
for i in range(N-1):
	x1 = x[i]; v1 =v[i]
	x[i+1],v[i+1] = RK4(x1,v1,t)
	t[i+1] = t[i] + dt




#plotting shit
"""
#plotting the motion in x against time
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("utslag, whatever that is in english")
plt.show()
"""

#plotting the 
plt.plot(x,v)
plt.xlabel("motion in x [m]")
plt.ylabel("velocity [m/s]")
plt.show()


