import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys 
sys.path.append('../../config')
import cst
import time_inf as tinf
import os

plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
#plt.rcParams['axes.labelpad'] = -10


##############################################
time_evo_f = np.load('../time_evo/time_evo_f.npy')
##############################################


X,K=np.meshgrid(cst.xvec*10**9,cst.kvec/10**9)


fig = plt.figure()
ax = fig.add_subplot(111)

ims = []

tmax = 2400
for ti in range(tmax):
    if ti%100 ==0:

        print(ti)    
        img = ax.imshow( time_evo_f[ti], extent=( cst.xvec[0]*10**9, cst.xvec[-1]*10**9, cst.kvec[0]/10**9,cst.kvec[-1]/10**9,  ), vmin=-0.2, vmax=0.6 )
        plt.ylabel('k (1/nm)')
        plt.xlabel('x (nm)')

        ims.append([img])


fig.colorbar(img)
ani = animation.ArtistAnimation(fig, ims, interval=200)
plt.show()

ani.save("f.gif", writer="imagemagick")
