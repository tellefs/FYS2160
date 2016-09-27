import matplotlib.pyplot as mplt
import numpy as np


T_over_theta = [1.e3, 1e-5]

n = 100
j = np.linspace(0, n, n+1) #j is integers from 0 up to n

def z(j, T_over_theta):
	return np.exp(-j*(j+1)/T_over_theta)


for i in range(len(T_over_theta)):
	mplt.plot(j, z(j, T_over_theta[i]))
	mplt.show()


