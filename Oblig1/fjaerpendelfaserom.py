import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 1e4)

omega = 2*np.pi

z = np.sin(omega*t)
v = omega*np.cos(omega*t)  # dz/dt

plt.plot(z,v)
plt.title("Phase plot of harmonic oscilation")
plt.xlabel("position")
plt.ylabel("velocity") 
plt.show()
plt.savefig("phaseplot.png")

