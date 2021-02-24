import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os
import sys
sys.path.append('../')
import cst


plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
plt.rcParams['axes.labelpad'] = -10

V = np.load('V.npy')

X,K=np.meshgrid(cst.xvec*10**9,cst.kvec/10**9)

#######################################################################
#三次元plot
fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111, projection='3d')

surf = ax1.plot_surface(K, X, V[:,:,300], cmap='coolwarm')

ax1.set_xlabel('k')
ax1.set_ylabel('x')
ax1.set_zlabel('f(x,k)')

plt.tight_layout()
plt.show()
#######################################################################
