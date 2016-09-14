import numpy as np
import matplotlib.pyplot as mplt
import math as mt

"""
the first part of the program is a copy of task (m)
"""
M = 10000
N = 50

macrostates = np.zeros((N, M));

for i in range(N):
	for j in range(M):
		chooser_of_state = np.random.randint(2)
		if chooser_of_state == 1:
			macrostates[i,j] = -1.
		else:
			macrostates[i,j] = 1.

thesum = sum(macrostates)

"""
this is new for taks (q)
"""
def omega(N, s):
	return float(mt.factorial(N)/(mt.factorial(N/2 + s)*mt.factorial(N/2 - s)))


x_axis = np.linspace(-N/2, N/2, N)

analytic = omega(N,0)*np.exp((-2*(x_axis**2))/N)

print omega(N,0)



mplt.hist(thesum, 30)
mplt.xlabel(' ')
mplt.ylabel(" ")
mplt.hold('on')
mplt.plot(x_axis, analytic)
#mplt.show()
