import numpy as np
import matplotlib.pyplot as mplt
import math as mt

"""
the first part of the program is a copy of task (m)
"""
M = 10000
N = 50

s = np.zeros(M)
number_of_cols = 0

for i in range(M):
	S_min = 0
	S_plus = 0
	for j in range(N):
		chooser_of_state = np.random.randint(2)
		if chooser_of_state == 1:
			S_min += 1
		else:
			S_plus += 1
	s_value = (S_plus - S_min)/2.
	if s_value not in s:
		number_of_cols += 1
	s[i] = s_value

energy = -2*s #times mu and B too, but i assume them to be equal to 1

"""
this is new for taks (q)
"""
def omega(N, s):
	return float(mt.factorial(N)/(mt.factorial(N/2 + s)*mt.factorial(N/2 - s)))


x_axis = np.linspace(-N/2, N/2, N)

analytic = omega(N,0)*np.exp((-2*(x_axis**2))/N)*M/(2**N)

mplt.hist(energy, number_of_cols+1, color='y')
mplt.xlabel('values of s ')
mplt.ylabel('probability of given s value')
mplt.hold('on')
mplt.plot(x_axis, analytic, 'b')
mplt.show()
