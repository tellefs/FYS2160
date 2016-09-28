import matplotlib.pyplot as mplt
import numpy as np


T_over_theta = [10**i for i in xrange(-3, 6)]

n = 1000
j = np.linspace(0, n, n+1) #j is integers from 0 up to n

def z(j, T_over_theta):
	return (2*j + 1)*np.exp(-j*(j+1)/T_over_theta)


for i in range(len(T_over_theta)):
	mplt.plot(j, z(j, T_over_theta[i]), label='$T/\Theta_R$ = %e' %T_over_theta[i])
mplt.legend()
mplt.xlabel('j')
mplt.ylabel('z(j)')	
mplt.show()


