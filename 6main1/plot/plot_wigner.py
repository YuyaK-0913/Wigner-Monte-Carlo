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




X,K=np.meshgrid(cst.xvec*10**9,cst.kvec/10**9)




##############################################
os.chdir('..')
os.chdir('time_evo')
time_evo_f = np.load('time_evo_f.npy')

'''#ここだけ変える
Nt_ex = pp.Nt_ex
print(Nt_ex)'''

Nt_ex = int( input('time step = ') )
print('time = ',tinf.delta_t * Nt_ex)
##############################################'''


##################################################################
#三次元plot
fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111, projection='3d')
surf = ax1.plot_surface(K, X, time_evo_f[Nt_ex], cmap='coolwarm')
#surf = ax1.plot_surface(K, X, time_evo_f[N_ex] -time_evo_f[0] , cmap='coolwarm')
#ax1.set_zlim(-0.1,0.4)

ax1.set_xlabel('k')
ax1.set_ylabel('x')
ax1.set_zlabel('f(x,k)')

ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_zticks([])
#ax1.set_xticklabels([])
#ax1.set_yticklabels([])
#ax1.set_zticklabels([])

plt.tight_layout()
plt.show()
##################################################################




##########################################################################################
#ヒートマップ
plt.pcolormesh(K, X, time_evo_f[0], cmap='coolwarm', vmin=-0.1, vmax=0.6, shading='gouraud')
#plt.pcolormesh(K, X, time_evo_f[0], cmap='coolwarm', shading='gouraud')
pp=plt.colorbar (orientation="vertical") # カラーバーの表示 

pp.set_label('f (x,k)') #カラーバーのラベル
plt.xlabel('k (1/nm)')
plt.ylabel('x (nm)')
plt.show()
##########################################################################################

##########################################################################################
#ヒートマップ
plt.pcolormesh(K, X, time_evo_f[Nt_ex], cmap='coolwarm', vmin=-0.1, vmax=0.6, shading='gouraud')
#plt.pcolormesh(K, X, time_evo_f[Nt_ex], cmap='coolwarm', shading='gouraud')
pp=plt.colorbar (orientation="vertical") # カラーバーの表示 

pp.set_label('f (x,k)') #カラーバーのラベル
plt.xlabel('k (1/nm)')
plt.ylabel('x (nm)')
plt.show()
##########################################################################################



##########################################################################################
#ヒートマップ
#plt.pcolormesh(K, X, time_evo_f[N_ex], cmap='coolwarm', vmin=-0.1, vmax=0.4, shading='gouraud')
#plt.pcolormesh(K, X, time_evo_f[N_ex], cmap='coolwarm', shading='gouraud')
#plt.pcolormesh(K, X, time_evo_f[Nt_ex]-time_evo_f[0], cmap='coolwarm', vmin=-0.1, vmax=0.1, shading='gouraud')
plt.pcolormesh(K, X, time_evo_f[Nt_ex]-time_evo_f[0], cmap='coolwarm', vmin=-0.5, vmax=0.5, shading='gouraud')

pp=plt.colorbar (orientation="vertical") # カラーバーの表示 

pp.set_label('f (x,k)') #カラーバーのラベル
plt.xlabel('k (1/nm)')
plt.ylabel('x (nm)')
plt.show()
##########################################################################################