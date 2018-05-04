#imports
import numpy as np
import matplotlib.pyplot as plt
from RK4 import RK4
import seaborn


#declare constants
dt = 10.**-2		#some timestep [s]
m = 0.500		#mass of 500 g [kg]
k = 1. 			#stiffness constant [N/m]
x0 = 1. 			#start position [m]
v0 = 0. 			#start velocity [m/s]
T = 20. 			#total time [s]
N = int(T/dt) 	

#setting initialconditions
x = np.zeros(N); v = np.zeros(N); t = np.zeros(N)
x[0] = x0; v[0] = v0

"""
the function we have is 
mx''(t) + kx(t) = 0
x''(t) = kx(t)/m
"""
#making functions 

def diffEQ(xNow,vNow,tNow):
	aNow = -k*xNow/m
	return aNow

#running the loop 
for i in range(N-1):
	x1 = x[i]; v1 =v[i]
	x[i+1],v[i+1] = RK4(diffEQ,x1,v1,t,dt)
	t[i+1] = t[i] + dt



#plotting 

"""
#plotting the motion in x against time
plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("motion")
plt.show()
"""

#plotting the phaseplot
plt.plot(x,v, '#803CA2', linewidth=2.0)
plt.title('Plot i faserommet', fontsize=20)
plt.xlabel("Motion in x [m]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave1.png')
plt.show()


