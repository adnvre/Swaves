import numpy as np
import matplotlib.pyplot as plt

a = -9.81
v0 = 20.
x0 = 0.

t_end = -2*v0/a
t = np.linspace(0,t_end,1e4)

v = v0 + a*t
x = x0 +v0*t + 0.5*a*t**2

plt.plot(t,x)
plt.show()
plt.plot(x,v)
plt.title("Phase plot of bouncy ball without loss")
plt.xlabel("position")
plt.ylabel("velocity")
plt.show()
plt.savefig("bouncyballphase.png")