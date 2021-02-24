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
plt.rcParams['axes.labelpad'] = -10



f = np.load('data/f.npy')




X,K=np.meshgrid(cst.xvec*10**9,cst.kvec/10**9)






##################################################################
#三次元plot
fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111, projection='3d')
surf = ax1.plot_surface(K, X, f, cmap='coolwarm')

#ax1.set_zlim(-0.1,0.4)
ax1.set_xlabel('k')
ax1.set_ylabel('x')
ax1.set_zlabel('f(x,k)')
plt.tight_layout()
plt.show()
##################################################################




##########################################################################################
#ヒートマップ
plt.pcolormesh(K, X, f, cmap='coolwarm', shading='gouraud')

pp=plt.colorbar (orientation="vertical") # カラーバーの表示 

pp.set_label('f (x,k)') #カラーバーのラベル
plt.xlabel('k (1/nm)')
plt.ylabel('x (nm)')
plt.show()
##########################################################################################







