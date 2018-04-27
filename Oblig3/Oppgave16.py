#Oppgave16
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


N = 1024
T = 16*2*np.pi
X = np.zeros(N)
t = np.linspace(0,T, N)
fs = N/T
f = np.linspace(0, fs, N)

x = 0
for j in range(3000):
	n = 2*j+1
	x += 1./n*np.sin(n*t)


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
