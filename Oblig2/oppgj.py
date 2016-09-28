import numpy as np
import matplotlib.pyplot as mplt


# -- Problem (j) --
def Z(T_over_theta_r, epsilon=1e-14):
	"""
	Z(T) = sum_i (from 0 to infinity): exp(-i(i+1)/T_over_theta_r)
	function to calculate a reasonable approximation to the partition function Z(T,V,N)
	epsilon tells hos how low the lowest entry to the function should be
	since the first part of the function is 1, we start here and add elements until one element is smaller than epsilon
	this function takes T_over_theta_r as an array of different values
	"""
	z = np.zeros(len(T_over_theta_r))
	for j in range(len(T_over_theta_r)):
		element = 1. 
		i = 1
		while (2*i + 1)*np.exp(-i*(i+1)/T_over_theta_r[j]) > epsilon:
			element += (2*i + 1)*np.exp(-i*(i+1)/T_over_theta_r[j])
			i += 1
		z[j] = element
	return z

# -- Problem (k) --
T_over_theta_r = np.linspace(1e-6, 5, 100)
mplt.plot(T_over_theta_r, Z(T_over_theta_r), label='Z(T)')
mplt.plot(T_over_theta_r, 1+np.exp(-2/T_over_theta_r), 'r', label='approximation of Z(T) for high T') # -- Problem (l) --
mplt.axis([0,4,0,5])
mplt.legend()
mplt.xlabel('$T/\Theta_R$')
mplt.ylabel('Z(t)')
mplt.show()		



