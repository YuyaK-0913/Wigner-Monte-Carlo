import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
sys.path.append('../config')
import cst
import os

plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
#plt.rcParams['axes.labelpad'] = -10


Qfw_start = np.load('Qfw.npy')

K,X=np.meshgrid(cst.kvec/10**9,cst.xvec*10**9)





##################################################################
#三次元plot

fig = plt.figure(figsize=(5,4))

ax1 = fig.add_subplot(111, projection='3d')
surf = ax1.plot_surface(K, X, Qfw_start, cmap=plt.cm.seismic , linewidth=0 , antialiased=False)

#ax1.set_zlim(-4*10**14,4*10**14)
ax1.set_xlabel(r'$k(1/nm)$')
ax1.set_ylabel(r'$x(nm)$')
ax1.set_zlabel(r'$Qfw(x,k)$')

plt.tick_params(labelsize=13)
plt.tight_layout()

# カラーバーの表示
#fig.colorbar(surf, shrink=0.5, aspect=10)
plt.tight_layout()
plt.show()
##################################################################






#############################################
#ヒートマップ
plt.pcolormesh(K, X, Qfw_start, cmap='coolwarm', shading='gouraud')
#plt.pcolormesh(K, X, Qfw_start, cmap='coolwarm', vmin=-4*10**14, vmax=4*10**14, shading='gouraud')
pp=plt.colorbar (orientation="vertical") # カラーバーの表示 

pp.set_label(r'$Qfw (x,k)$') #カラーバーのラベル
plt.xlabel(r'$k (1/nm)$')
plt.ylabel(r'$x (nm)$')
plt.show()
#############################################
