import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
sys.path.append('../config/')
import cst
import os




H1 = -2 * np.eye(cst.Nx) 
H2 = np.eye(cst.Nx,k=1)
H3 = np.eye(cst.Nx,k=-1)
H = -cst.hbar**2 / (2*cst.m1*cst.delta_x**2) * ( H1+H2+H3 )

V = 10 * cst.eV * np.eye(cst.Nx)
for i in range(290,295):
    V[i][i] = 0
for i in range(305,310):
    V[i][i] = 0


U = np.diag(V)

plt.plot(cst.xvec*10**9, U/cst.eV)
plt.show()

H = H+V

val,vec = np.linalg.eigh(H)

E1 = val[0]
E2 = val[1]
E3 = val[2]

psi1 = vec.T[0]
psi2 = vec.T[1]
psi3 = vec.T[2]

print('E1',E1/cst.eV)
print('E2',E2/cst.eV)
print('delta_E', (E2-E1)/cst.eV)


I1 = integrate.simps(psi1**2, cst.xvec)
I2 = integrate.simps(psi2**2, cst.xvec)
I3 = integrate.simps(psi3**2, cst.xvec)

psi1 = psi1 / np.sqrt(I1)
psi2 = psi2 / np.sqrt(I2)
psi3 = psi3 / np.sqrt(I3)

print( integrate.simps(psi1**2, cst.xvec) )
print( integrate.simps(psi2**2, cst.xvec) )
print( integrate.simps(psi3**2, cst.xvec) )


plt.plot(cst.xvec,psi1)
plt.plot(cst.xvec,psi2)
plt.plot(cst.xvec,psi1+psi2)
#plt.plot(cst.xvec,psi2-psi1+psi3)

plt.show()




os.chdir('data')
np.save('psi1_x',psi1)
np.save('psi2_x',psi2)
np.save('psi_x',psi2+psi1)
np.save('U',U)
np.save('E1',E1)
np.save('E2',E2)