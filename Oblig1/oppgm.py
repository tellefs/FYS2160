import numpy as np
import matplotlib.pyplot as mplt

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

mplt.hist(thesum, 30)
mplt.xlabel(' ')
mplt.ylabel('Energy (assuming mu*B=1)')
mplt.show()
