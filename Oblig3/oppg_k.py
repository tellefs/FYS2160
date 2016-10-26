import numpy as np
import matplotlib.pyplot as mplt

T_hat = 0.9
n = 1000

rho_hat = np.linspace(0.2, 2.0, n)

def g_hat(rho_hat, T_hat, p_hat):
	return -3*rho_hat -(8./3)*T_hat*np.log(3./rho_hat - 1) + p_hat/rho_hat

def p_hat(rho_hat, T_hat):
	return(8.*rho_hat*T_hat)/(3. - rho_hat) - 3*rho_hat*rho_hat

def V_hat(rho_hat):
	return 1./rho_hat



mplt.subplot(3, 1, 1)
mplt.plot(rho_hat, p_hat(rho_hat, T_hat), label='$\hat{p}(\hat{\\rho})$')
mplt.legend(loc='upper left')
mplt.xlabel('$\hat{\\rho}$')
mplt.ylabel('$\hat{p}$')
mplt.tight_layout()

mplt.subplot(3, 1, 2)
mplt.plot(p_hat(rho_hat, T_hat), V_hat(rho_hat), label='$\hat{V}(\hat{\\rho})$')
mplt.legend(loc='upper right')
mplt.xlabel('$\hat{p}$')
mplt.ylabel('$\hat{V}$')
mplt.tight_layout()

mplt.subplot(3, 1, 3)
mplt.plot(p_hat(rho_hat, T_hat), g_hat(rho_hat, T_hat, p_hat(rho_hat, T_hat)), label='$\hat{g}(\hat{p})$')
mplt.legend(loc='lower right')
mplt.xlabel('$\hat{p}$')
mplt.ylabel('$\hat{g}$')
mplt.tight_layout()

mplt.savefig('oppg_k.png')
mplt.show()


#oppgm -selfintersect-
"""
def selfintersect(x, y):
	n = len(x)
	xpoints = []
	ypoints = []
	tol = 1e-14
	for i in range(n):
		for j in range(n):
			if abs(x[i] - x[j]) < tol and abs(y[i] - y[j]) < tol:
				xpoints.append(x[i])
				ypoints.append(y[i])
	return xpoints, ypoints


xpoints, ypoints = selfintersect(p_hat(rho_hat, T_hat), g_hat(rho_hat, T_hat, p_hat(rho_hat, T_hat)))
print xpoints
print ypoints
"""

			
			




