#Oppgave14
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


N = 512
T = 13*2*np.pi
X = np.zeros(N)
t = np.linspace(0,T, N)
x = np.sin(t)
fs = N/T
f = np.linspace(0, fs, N)



def FT(x, n, k):
	return x*np.exp(complex(0, -2*np.pi/N*k*n))


for k in range(N-1):
	Xk = 0
	for n in range(N-1):
		Xk += FT(x[n], n, k)   
	X[k] = 1./N *abs(Xk)

plt.figure()
plt.plot(f[0:N/2.], X[0:N/2.])
plt.xlabel('frekvens')
plt.ylabel('utslag')
plt.show()
