#imports
import numpy as np
import matplotlib.pyplot as plt
from RK4 import RK4
import seaborn


#declare constants
dt = 10.**-4		#some timestep [s]
m0 = 0.00001		#mass of waterdrop [kg]
k = 0.475 			#stiffness constant [N/m]
x0 = 0.001 			#start position [m]
v0 = 0.001 			#start velocity [m/s]
T = 3. 			#total time [s]
N = int(T/dt) 		#number of things
b = 0.001 			#[kg/s]
#omega0 = k/m 		#Svingefrekvens for HO
#F_D = 0.7 			#[N]
#omega_D = 13./(8*omega0)
#omega_D = 2./((np.sqrt(5)-1)*omega0)
g = 9.81 			#gravitational acceleration [m/s^2]
psi = 0.00055 		#m'(t) [kg/s]
dpsi =3*psi/N

#setting initialconditions
x = np.zeros(N); v = np.zeros(N); t = np.zeros(N)
x[0] = x0; v[0] = v0
m = np.zeros(N)
m[0] = m0

#F = np.zeros(N)
#F[0] = F_D



"""
the functions we have are 
m(t)x''(t)+(b+psi)x'(t)+kx(t)=m(t)g
x''(t) = (m(t)g - (b+psi)x'(t) - kx(t))/m(t)
"""
#making functions 

def diffEQ(xNow,vNow,tNow):
	aNow = (m[i]*g-(b+psi)*vNow-k*xNow)/m[i]
	return aNow

#running the loop
for i in range(N-1):
	x1 = x[i]; v1 =v[i]
	x[i+1],v[i+1] = RK4(diffEQ,x1,v1,t,dt)
	t[i+1] = t[i] + dt
	m[i+1] = m[i] + dpsi


#plotting

#plotting the motion in x against time
plt.plot(t,x, '#803CA2', linewidth=2.0)
plt.title('Plot av utslag', fontsize=20)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Motion in x [m]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
plt.show()

#plotting the phaseplot
plt.plot(x,v, '#803CA2', linewidth=2.0)
plt.title('Plot i faserommet', fontsize=20)
plt.xlabel("Motion in x [m]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave5del1.png')
plt.show()


