#imports
import time
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
T = 20. 			#total time [s]
N = int(T/dt) 		#number of things
b = 0.001 			#[kg/s]
g = 9.81 			#gravitational acceleration [m/s^2]
M = 100 			#numer of steps
psi_list = np.linspace(0.00055, 0.00075, M) 		#m'(t) [kg/s]
#dpsi =T*psi/N 		#mass gain step
x_c = 0.0025 		#critical distant for drop fall
beta = 50 			# [s/m]
rho = 1000 			# density of water [kg/m^3]


#setting initialconditions
x = np.zeros(N); v = np.zeros(N); t = np.zeros(N)
x[0] = x0; v[0] = v0
m = np.zeros(N)
m[0] = m0

runtime0 = time.clock()
print("runtime0 =", runtime0)
"""
the functions we have are 
m(t)x''(t)+(b+psi)x'(t)+kx(t)=m(t)g
x''(t) = (m(t)g - (b+psi)x'(t) - kx(t))/m(t)
"""
#making functions 

def diffEQ(xNow,vNow,tNow):
	aNow = (m[i]*g-(b+psi)*vNow-k*xNow)/m[i]
	return aNow


#t_drop = np.zeros(M)

t_c =0

runtime1 = time.clock()
print("runtime1 =", runtime1)

#psiruntime = np.zeros(M)
forlooptimer = np.zeros(N-1)

#running the loop
for psi in psi_list:
	print(psi)
	psi_plot_list = [psi]*50
	t_diff = []
	#dpsi =(T*psi[j])/N
	psiruntime = time.clock()
	print("PSI loop = ", psiruntime)

	for i in range(N-1):
		x1 = x[i]; v1 =v[i]
		oldmass = m[i]
		dm = beta*oldmass*v[i]
		A = (3*dm**4)
		B = (4*np.pi*rho*oldmass**3)
		dx =  (A/B)**(1./3) 

		if x[i] > x_c:
			t_c_old = t_c
			t_c = t[i] 
			#print (i)
			#print ('xi=',x[i])
			#print ('dx =',dx)
			
			m[i+1] = oldmass - dm + psi*dt
 			
			if m[i+1] <= 0:
				print ("mass cannot be 0 or negative")
				m[i+1]=0.00001

			x1 = x[i] - dx
			t_diff.append(t_c - t_c_old)

		else:
			m[i+1] = m[i] + psi*dt

		x[i+1],v[i+1] = RK4(diffEQ,x1,v1,t,dt)
		t[i+1] = t[i] + dt
		forlooptimer[i] = time.clock()
	print("For loop timer =", forlooptimer[::100])
	t_diff_plot = t_diff[-50:]
	plt.plot(psi_plot_list, t_diff_plot)
#plt.savefig("Oppgave8.png")
plt.show()



#plotting

"""
#plotting the motion in x against time
plt.figure(figsize=(8,5))
plt.plot(t,x, '#803CA2', linewidth=2.0)
plt.title('Plot av utslag', fontsize=20)
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Motion in x [m]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave8utslag_psi55.png')
plt.show()

#plotting the phaseplot
plt.figure(figsize=(8,5))
plt.plot(x,v, '#803CA2', linewidth=2.0)
plt.title('Plot i faserommet', fontsize=20)
plt.xlabel("Motion in x [m]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
#plt.savefig('Oppgave8faseplott_psi55.png')
plt.show()
"""

final_runtime = time.clock()
print("Final runtime =", final_runtime)

