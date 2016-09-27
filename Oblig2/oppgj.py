import numpy as np
import matplotlib.pyplot as mplt



def Z(T_over_theta_r, epsilon=1e-3):
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
		while np.exp(-i*(i+1)/T_over_theta_r[j]) > epsilon:
			element += np.exp(-i*(i+1)/T_over_theta_r[j])
			i += 1
		z[j] = element
	return z





T_over_theta_r = np.linspace(1e-6, 1e6, 100)

mplt.plot(T_over_theta_r, Z(T_over_theta_r))
mplt.xlabel('T_over_theta_r')
mplt.ylabel('Z(t)')
mplt.show()		



