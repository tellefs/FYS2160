import math as mt
import numpy as np
import matplotlib.pyplot as plt

def P(qa, q, Na, Nb):
	qb = q-qa
	N = Na + Nb
	omega_a = float(mt.factorial(qa+Na-1)/(mt.factorial(qa)*mt.factorial(Na-1)))
	omega_b = float(mt.factorial(qb+Na-1)/(mt.factorial(qb)*mt.factorial(Nb-1)))
	omega_tot = float(mt.factorial(q+N-1)/(mt.factorial(q)*mt.factorial(N-1)))	
	return (omega_a*omega_b)/omega_tot
	
q = 100
qa = np.linspace(0, 100, 101)
P_qa = np.zeros(101)

for i in range(101):
	P_qa[i] = P(qa[i], q=100, Na=50, Nb=50)

plt.plot(qa, P_qa)
plt.xlabel("q_a")
plt.ylabel("P(q_a)")
plt.show()

int_max_value = np.argmax(P_qa)

print 'The most probable state is q_a = %i with probability P(q_a) = %f' % (qa[int_max_value], P_qa[int_max_value])


