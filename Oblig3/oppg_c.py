import numpy as np
import matplotlib.pyplot as mplt

def p_hat_V(T_hat, V_hat):
	return 8*T_hat/(3*V_hat - 1) - 3/(V_hat**2)

n = 1000
V_hat = np.linspace(0.4, 20, n)
T_hat = [1.15, 1.0, 0.85]

for T in T_hat:
	mplt.plot(V_hat, p_hat_V(T, V_hat), label='$\hat{T} =$ %.2f' %T)

mplt.legend()
mplt.xlabel('$\hat{V}$')
mplt.ylabel('$\hat{p}$')
mplt.savefig('oppg_c.png')
mplt.show()

#oppg e

def p_hat_rho(T_hat, rho_hat):
	return (8*T_hat*rho_hat/(3-rho_hat)) - 3*rho_hat*rho_hat

rho_hat = np.linspace(0, 2, n)
for T in T_hat:
	mplt.plot(rho_hat, p_hat_rho(T, rho_hat), label='$\hat{T} =$ %.2f' %T)
mplt.legend()
mplt.xlabel('$\hat{\\rho}$')
mplt.ylabel('$\hat{p}$')
mplt.savefig('oppg_e.png')
mplt.show()

for T in T_hat:
	mplt.plot(p_hat_rho(T, rho_hat), rho_hat, label='$\hat{T} =$ %.2f' %T)
mplt.legend()
mplt.show()

for T in T_hat:
	mplt.plot(p_hat_V(T, V_hat), V_hat, label='$\hat{T} =$ %.2f' %T)
mplt.legend()
mplt.show()





