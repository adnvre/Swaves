import time
import numpy as np
import matplotlib.pyplot as plt
#import scipy.integrate.RK45 as RK45
from RK4 import RK4 



#Declaring variables
N = 4000				#number of timesteps
t_end = 100				#amount of time for simulation
dt = t_end/N 			#timestep

b = 0.04				#[kg/s] friction
m = 0.1					#[kg] mass
k = 10 					#[N/m] spring constant
#omega_F = np.sqrt(k/m)*0.9	#force frequency
F = 0.1					#external force [N]

#some calculations
omega_0 = np.sqrt(k/m)	#own frequency
#gamma = b/(2*m)
#omega_hat = np.sqrt(omega_0**2-gamma**2)
#phi = np.arctan(-gamma/omega_hat)
#A = 0.1/np.cos(phi)


#arrays
t = np.linspace(0,t_end,N)	#time array
z = np.zeros(N)
v = np.zeros(N)

#initial conditions
z[0] = 0.1
v[0] = 0

def diffEQ(z,v,t):
	return F/m*np.cos(omega_F*t) -b/m*v - k/m*z



"""
#integration loop with scipy module
for i in range(N-1):
	#SOMETHING WITH THE RK45 MOTHERFUCKER


#standard integration loop
for i in range(N-1):
	z[i+1], v[i+1] = RK4(diffEQ,z[i],v[i],t[i],dt)
	
"""
#analytical solution, z(t)=e^(-gamma*t)*A*np.cos(omega_hat*T+phi)
#analytical_z = np.exp(-gamma*t)*A*np.cos(omega_hat*t + phi)



#checking frequency response
nr_freqs = 801 			#nr of frequencies (omega_F) to test
energies = np.zeros(nr_freqs)

omega_F_array = np.linspace(0.5, 1.5, nr_freqs)*omega_0 	




#Tj_loop = np.zeros(nr_freqs)



#integration loop
for j in range(nr_freqs):
	omega_F = omega_F_array[j]
	for i in range(N-1):
		z[i+1], v[i+1] = RK4(diffEQ,z[i],v[i],t[i],dt)



	energies[j] = 0.5*k*np.max(z[9*nr_freqs//10:])**2 #Energy is set to 0.5*x*A**2
	#where A is the max amplitude after 9/10th of the time has passed.
	#Tj_loop[j] = time.clock()
	#every10steps = Tj_loop[::10]
	#print("10steps = ", Tj_loop[::10])
	#print("jloop_time = ", Tj_loop[j])

#every15steps = Tj_loop[::15]




max_energy = np.max(energies)
above_half_energy = np.where(energies>(max_energy/2))[0] #indexes of elements above Emax/2
#width of peak is equal to difference between first and last frequency above Emax/2:
delta_f = omega_F_array[above_half_energy[-1]] - omega_F_array[above_half_energy[0]]
Q = omega_0/delta_f # estimated Q

print("Calculated Q =", Q, "Actual Q = ", np.sqrt(m*k/b**2))

#plotting
plt.plot(omega_F_array, energies)#t, z) t, analytical_z)
plt.show()

T_final = time.clock()

print("Computation took =", T_final, "seconds")







