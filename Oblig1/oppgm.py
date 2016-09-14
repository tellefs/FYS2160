import numpy as np
import matplotlib.pyplot as mplt

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

mplt.hist(energy, number_of_cols+1)
mplt.xlabel('value of s')
mplt.ylabel('probability of s')
mplt.show()
