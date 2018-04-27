#oppgave11

import matplotlib.pyplot as plt 
times = []
sunspots = []
fin = open('soldata.txt', 'r') 
for line in fin:
	cols = line.split() 
	times.append( float(cols[0]) ) 
	sunspots.append( float(cols[1]) )
fin.close()
plt.plot( times, sunspots, '-b')
plt.show()