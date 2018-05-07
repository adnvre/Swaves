#imports
import numpy as np
import matplotlib.pyplot as plt
from RK4 import RK4
import seaborn



#declare constants
dt = 10.**-2		#some timestep [s]
m = 0.500			#mass of 500 g [kg]
k = 1. 				#stiffness constant [N/m]
x0 = 2. 			#start position [m]
v0 = 0. 			#start velocity [m/s]
T = 200. 			#total time [s]
N = int(T/dt) 		#number of things
omega0 = np.sqrt(k/m) 		#Svingefrekvens for HO
F_D = 0.7 			#[N]
#omega_D = (13./8)*omega0
omega_D = (2./((np.sqrt(5)-1)))*omega0


#setting initialconditions
x = np.zeros(N); v = np.zeros(N); t = np.zeros(N)
x[0] = x0; v[0] = v0
F = np.zeros(N)
F[0] = F_D



"""
the function we have is 
mx''(t) + kx(t) = F(t)
x''(t) = F(t)/m -kx(t)/m
"""
#making functions 

def diffEQ(xNow,vNow,tNow):
	aNow = (F[i]-k*xNow)/m
	return aNow

#running the loop
for i in range(N-1):
	x1 = x[i]; v1 =v[i]
	F[i] = F_D *np.cos(omega_D*t[i]) 
	x[i+1],v[i+1] = RK4(diffEQ,x1,v1,t,dt)
	t[i+1] = t[i] + dt


#The analytic solution

def anal_x_solution(t):
	return 2*np.cos(np.sqrt(k/m)*t) + F_D/(k-m*omega_D**2)*(np.cos(omega_D*t)-np.cos(np.sqrt(k/m)*t))


#plotting

#plotting the motion in x against time
plt.figure(figsize=(8,5))
plt.plot(t,x, '#803CA2', linewidth=2.0)
plt.title('Plot av utslag $\omega_D = (2/(\sqrt{5}-1))\omega_0$', fontsize=20)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Motion in x [m]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('oppgave4utslagdel2.png')
plt.show()

#plotting the phaseplot
plt.figure(figsize=(8,5))
plt.plot(x,v, '#803CA2', linewidth=2.0)
plt.title('Plot i faserommet, $\omega_D = (2/(\sqrt{5}-1))\omega_0$', fontsize=20)
plt.xlabel("Motion in x [m]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave4fasedel2.png')
plt.show()


#plotting the difference between the numerical and analytical result
plt.figure(figsize=(8,5))
plt.plot(t, x-anal_x_solution(t), '#803CA2', linewidth=2.0)
plt.xlabel('t [s]', fontsize=14)
plt.ylabel('Differanse utslag [m]',fontsize=14)
plt.title('Differanse mellom analytisk og numerisk utslag', fontsize=16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave4_differanse.png')
plt.show()
