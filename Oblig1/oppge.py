import math as mt
import matplotlib.pyplot as plt
import numpy as np


q = 6

def microstates(qa, Na, Nb):
	"""
	calculating # of possible microstates when q is known
	"""	
	qb = q-qa
	omega_a = mt.factorial(qa + Na - 1)/(mt.factorial(qa)*mt.factorial(Na-1))
	omega_b = mt.factorial(qb + Nb - 1)/(mt.factorial(qb)*mt.factorial(Nb-1))
	return omega_a*omega_b



def P(qa, q, Na, Nb):
	"""
	probability of macrostate given which state qa is in
	"""
	qb = q-qa
	N = Na + Nb
	omega_a = float(mt.factorial(qa+Na-1)/(mt.factorial(qa)*mt.factorial(Na-1)))
	omega_b = float(mt.factorial(qb+Na-1)/(mt.factorial(qb)*mt.factorial(Nb-1)))
	omega_tot = float(mt.factorial(q+N-1)/(mt.factorial(q)*mt.factorial(N-1)))
	print "# of microstates for qa = %i is %i" %(qa, omega_a*omega_b)
	return (omega_a*omega_b)/omega_tot, omega_tot

qa = np.linspace(0, 6, 7)
P_qa = np.zeros(7)
for i in range(7):
	P_qa[i] = P(qa[i], q=6, Na=2, Nb=2)[0]
print 'total # of microstates is %i' %P(qa[i], q=6, Na=2, Nb=2)[1]

plt.plot(qa, P_qa)
plt.xlabel("q_a")
plt.ylabel("P(q_a)")
plt.show()
