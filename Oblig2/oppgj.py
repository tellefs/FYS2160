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
n = 100
T_over_theta_r = np.linspace(1e-6, 5, n)
mplt.plot(T_over_theta_r, Z(T_over_theta_r), label='Z(T)')
mplt.plot(T_over_theta_r, T_over_theta_r, 'r', label='approximation of Z(T) for high T') # -- Problem (l) --
mplt.axis([0,4,0,5])
mplt.legend()
mplt.xlabel('$T/\Theta_R$')
mplt.ylabel('Z(t)')
mplt.show()		


# -- Problem (m) --

E = np.zeros(n)
for k in range(n-1):
	E[k] = - ( (np.log(Z(T_over_theta_r)[k+1]) - np.log(Z(T_over_theta_r)[k])) / (T_over_theta_r[k] - T_over_theta_r[k+1]) )

C_v = np.zeros(n)
for k in range(n-1):
	C_v[k] = (E[k+1] - E[k]) / (T_over_theta_r[k+1] - T_over_theta_r[k])

Cv_anal_low = (np.exp(-2./T_over_theta_r))/((1+3*np.exp(-2./T_over_theta_r))**2)
Cv_anal_high = T_over_theta_r
E_anal_low = (6*np.exp(-2./T_over_theta_r))/(1 + 3*np.exp(-2./T_over_theta_r))
E_anal_high = T_over_theta_r


mplt.plot(T_over_theta_r, C_v, label='$C_v(T)$')
mplt.plot(T_over_theta_r, Cv_anal_low, label='$C_V(T)$ analytical, low T')
mplt.plot(T_over_theta_r, Cv_anal_high, label='$C_V(T)$ analytical, high T')
mplt.xlabel('$T/\Theta_R$')
mplt.legend()
mplt.show()

mplt.plot(T_over_theta_r, E, label='$E(T)$')
mplt.plot(T_over_theta_r, E_anal_low, label='$E(T)$ analytical, low T')
mplt.plot(T_over_theta_r, E_anal_high, label='$E(T)$ analytical, high T')
mplt.xlabel('$T/\Theta_R$')
mplt.legend()
mplt.show()



