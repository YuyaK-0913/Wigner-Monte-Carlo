import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
sys.path.append('../../config')
import cst
import time_inf as tinf
import os


plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
plt.rcParams['axes.labelpad'] = -10



K,X=np.meshgrid(cst.kvec*10**9,cst.xvec/10**9)




##############################################
os.chdir('..')
os.chdir('time_evo')
time_evo_count_N = np.load('time_evo_count_N.npy')

'''#ここだけ変える
Nt_ex = pp.Nt_ex
print(Nt_ex)'''

Nt_ex = int( input('time step = ') )
print('time = ',tinf.delta_t * Nt_ex)

##############################################'''

print(time_evo_count_N.shape)
print(X.shape)
print(K.shape)
print(np.sum(time_evo_count_N[Nt_ex]))

##################################################################
#三次元plot
fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111, projection='3d')
surf = ax1.plot_surface(K, X, time_evo_count_N[Nt_ex], cmap='coolwarm')
#surf = ax1.plot_surface(K, X, count_N, cmap='coolwarm')
ax1.set_zlim(-2,2)

ax1.set_xlabel('k')
ax1.set_ylabel('x')
ax1.set_zlabel('count(x,k)')

plt.tight_layout()
plt.show()
##################################################################




