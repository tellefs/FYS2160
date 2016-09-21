import numpy as np
import matplotlib.pyplot as mplt

epsilon = 1e-20
k = 1.38064852e-23
T = np.linspace(1, 1000, 1000)
beta = 1/(k*T)

def heat_capacity(T):
	return (3*epsilon**2*np.exp(epsilon*beta))/(k*T**2*(np.exp(epsilon*beta)+3)**2)

mplt.plot(T, heat_capacity(T))
mplt.show()

