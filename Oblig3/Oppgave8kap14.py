"""Waveletanalysis.

Script that illustrates differences
between frequencyresolution and
timeresolution in waveletanalysis
"""

import numpy as np
import matplotlib.pyplot as plt

class FourierMorlet:
	#A Morelet-wave evaluated in the frequency domain

	def __init__(self,k):
		self.k = k

	def __call__(self, omega, omegaa):
		return 2 *(np.exp(-np.power(self.k * (omega - omegaa) / omegaa, 2))-
					np.exp(-np.power(self.k, 2)) *
					np.exp(-np.power(self.k * omega / omegaa, 2)))


def wavelet_transform(t, signal, omega_range, wavelet=FourierMorlet(6)):
	fft_signal = np.fft.fft(signal)
	fft_omegas = np.fft.fftfreq(len(signal), [1] -t[0]) *2 * np.pi
	transformed_signals = []
	for omega in omega_range:
		transformed_signals.append(
			np.fft.ifft(wavelet(fft_omegas, omega) * fft_signal))
		return np.asarray(transformed_signals)



if __name__ == "__main__":
	Fs = 10e3
	N = 8192
	T = N/Fs
	f1 = 1000
	f2 = 1600
	c1 = 1.0
	c2 = 1.7

	#___Exercise 8a___
	t = np.linspace(0, T, N)
	dt = t[1] - t[0]
	y = c1 *np.sin(2*np.pi * f1 *t) +c2 *np.sin(2*np.pi*f2*t)

	#___Exercise 8b___
	plt.figure()
	plt.subplot(121)
	plt.plot(t,y)
	

	FFT = np.fft.fft(y)/N
	freq = np.fft.fftfreq(N,dt)
	plt.subplot(122)
	plt.plot(freq[:int(N / 2)], np.absolute(FFT[:int(N / 2)]))
	plt.tight_layout()
	plt.savefig("ch14task8b.png")
	plt.show()

	#___Exercise 8c___
	omegas = np.logspace(np.log10(800), np.log10(2000), 100) *2*np.pi
	waveletDiagram24 = wavelet_transform(t, y, omegas, FourierMorlet(24))
	waveletDiagram200 = wavelet_transform(t, y, omegas, FourierMorlet(200))
	plt.figure()
	plt.subplot(121)
	plt.pcolormesh(t, omegas / 2.0 / np.pi, np.absolute(waveletDiagram24))
	plt.colorbar()
	plt.subplot(122)
	plt.pcolormesh(t, omegas / 2.0 / np.pi, np.absolute(waveletDiagram200))
	plt.colorbar()
	plt.tight_layout()
	plt.savefig("ch14task8c.png")
	plt.show()

	t1 = 0.15
	t2 = 0.5
	sigma1 = 0.01
	sigma2 = 0.1

	y = c1 * np.sin(2 *np.pi * f1 *t) * \
		np.exp(-np.power((t -t1) / sigma1, 2)) + \
		c2*np.sin(2*np.pi*f2*t) * \
		np.exp(-np.power((t-t2) / sigma2, 2))

	plt.figure()
	plt.subplot(121)
	plt.plot(t,y)
	

	#___Exercise 8d___
	FFT = np.fft.fft(y)/N
	freq = np.fft.fftfreq(N, dt)
	plt.subplot(122)
	plt.plot(freq[:int(N/2)],np.absolute(FFT[:int(N/2)]))
	plt.tight_layout()
	plt.savefig("ch14task8dfourier.png")
	plt.show()

	waveletDiagram24 = wavelet_transform(t,y,omegas,FourierMorlet(24))
	waveletDiagram200 = wavelet_transform(t,y,omegas, FourierMorlet(200))
	plt.figure()
	plt.subplot(121)
	plt.pcolormesh(t, omegas/2.0/np.pi,np.absolute(waveletDiagram24))
	plt.colorbar()
	plt.subplot(122)
	plt.pcolormesh(t, omegas/2.0/np.pi,np.absolute(waveletDiagram200))
	plt.colorbar()
	plt.tight_layout()
	plt.savefig("ch14task8dwavelet.png")
	plt.show()




