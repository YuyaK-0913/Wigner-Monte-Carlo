import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os
import sys
sys.path.append('../config')
import cst


plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
plt.rcParams['axes.labelpad'] = -10


psi = np.load('../1Qdot/data/psi_x.npy')




plt.plot(cst.xvec, np.real(psi))
plt.plot(cst.xvec, np.imag(psi))

plt.show()


####################################################################################################################################
#WFの計算
def getNearestIndex(array,num):
    #配列からある値にもっとも近い値のインデックスを返却する関数  
    #num=x+y or x-y
    array = np.abs(array-num)
    idx=array.argmin()
    return idx

IN1=np.zeros( ( len(cst.kvec) , len(cst.xvec) ) , dtype=complex )

for n,x in enumerate(cst.xvec):
    if n%5 == 0:
        print(n)
    for yi,y in enumerate(cst.yvec):

        plus_index=getNearestIndex(cst.xvec,x+y)
        minus_index=getNearestIndex(cst.xvec,x-y)
        
        #シンプソン則の処理
        for j,k in enumerate(cst.kvec):

            if y==cst.l or y==cst.r:
                IN1[j][n] += 1/3 * cst.delta_x * ( 2 * np.exp(-2*1j*k*y) * psi[ minus_index ] * psi[ plus_index ] ) 
            elif yi%2==1:
                IN1[j][n] += 4/3 * cst.delta_x * ( 2 * np.exp(-2*1j*k*y) * psi[ minus_index ] * psi[ plus_index ] ) 
            elif yi%2==0:
                IN1[j][n] += 2/3 * cst.delta_x * ( 2 * np.exp(-2*1j*k*y) * psi[ minus_index ] * psi[ plus_index ] ) 

IN1=np.real( (1/np.pi)*IN1 )
####################################################################################################################################




os.chdir('..')
os.chdir('2f')
os.chdir('data')
np.save('f',IN1)
