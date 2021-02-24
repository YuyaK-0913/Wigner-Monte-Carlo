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



V = np.load('../3V/V.npy') 
f = np.load('../2f/data/f.npy') 


def calc_Qfw(n,j):
    Qfw_nj = 0
    for j2 in range(cst.Nk):
        Qfw_nj += V[j2][n][j] * f[j2][n]
    return Qfw_nj
    







########################################################################################################
#量子補正項　[n][j]
start = time.time()

parallelize = Parallel(n_jobs=10, verbose=10)
calc_Qfw = delayed(calc_Qfw)
result = parallelize( [ calc_Qfw(n,j) for n in range(cst.Nx) for j in range(cst.Nk) ] )

result = np.array(result)
Qfw = result.reshape(cst.Nx,cst.Nk)
Qfw = -(1/cst.hbar) *  Qfw

end = time.time()
print(end - start)


np.save('Qfw',Qfw)
########################################################################################################
    


