import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os
import sys
sys.path.append('../config')
import cst
from joblib import Parallel, delayed
import time



plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
plt.rcParams['axes.labelpad'] = -10



U = np.load('../1Qdot/data/U.npy')


###################################################################################################################
#非局所ポテンシャルを三次元配列に格納
V = np.zeros( (cst.Nk,cst.Nx,cst.Nk) , dtype=np.float ) #[奥行j2][行n][列j]


def U_xu(x):
    Uxu = 0
    for n in range(cst.Nx-1):
        if cst.xvec[n] <= x < cst.xvec[n+1]:
            Uxu = ( U[n]+U[n+1] ) / 2
    return Uxu


for n,x in enumerate(cst.xvec):
    print('#####')
    print('n',n)
    for i,u in enumerate(cst.uvec):

        xu_plus = x + u/2
        xu_minus = x - u/2
        Uxu_plus = 0 
        Uxu_minus = 0 

        if ( cst.l <= xu_plus <= cst.r ) and ( cst.l <= xu_minus <= cst.r ):
            Uxu_plus = U_xu(xu_plus)
            Uxu_minus = U_xu(xu_minus)

        
        for j1,k1 in enumerate(cst.kvec):
            for j2,k2 in enumerate(cst.kvec):

                V[j2][n][j1] += np.sin( u * ( k1 - k2 )  ) * ( Uxu_plus - Uxu_minus )

V = (2/cst.Nk) * V 

os.chdir('..')
os.chdir('3V')
np.save('V',V)
###################################################################################################################
