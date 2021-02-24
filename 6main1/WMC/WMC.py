import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
sys.path.append('../../config')
import cst
import time_inf as tinf
import os
import ClassParticle
from joblib import Parallel, delayed


plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
#plt.rcParams['axes.labelpad'] = -10


U = np.load('../../1Qdot/data/U.npy')
f = np.load('../../2f/data/f.npy')
V = np.load('../../3V/V.npy')
Qfw = np.load('../../4Qfw/Qfw.npy') 



time_evo_f = np.zeros((10000,cst.Nk,cst.Nx))
time_evo_f[0] = f

time_evo_Qfw = np.zeros((10000,cst.Nx,cst.Nk))
time_evo_Qfw[0] = Qfw

time_evo_count_N = np.zeros((10000,cst.Nx,cst.Nk))
time_evo_count_N[0] = 1


os.chdir('../time_evo')



def renew_p(P):
    P.time_evolution()
    P.xk_index()
    return P

P_list = [ ClassParticle.Particle(n,j) for n in range(cst.Nx) for j in range(cst.Nk) ]

parallelize = Parallel(n_jobs=10, verbose=10)
renew_p = delayed(renew_p)

N = cst.N
for i in range(10009):

    print('######')
    print('time',i)
    print('N',N)

    P_list = parallelize( [ renew_p(P) for P in P_list ] ) 
    
    P_list = [ P for P in P_list if P.index_n is not None ]
    N = len(P_list)

    count_N = np.zeros( (cst.Nx,cst.Nk) )
    for P in P_list:
        n = P.index_n
        j = P.index_j
        count_N[n][j] += 1

    

    print('affinity_start')
    ##########################################################################
    #affinityの計算
    for p,P in enumerate(P_list):
        p_n = P.index_n
        p_j = P.index_j

        if count_N[p_n][p_j]!=0:
            P.A += Qfw[p_n][p_j] * tinf.delta_t / count_N[p_n][p_j]
        else:
            P.A += Qfw[p_n][p_j] * tinf.delta_t
    ##########################################################################
    print('affinity_end')



    print('addparticle_start')
    ##########################################################################
    #count_Nで格子点セルの範囲に粒子が存在しない場所の格子点をリストにする
    count_N_zero_list = list( zip( *np.where( count_N==0 ) ) )
    
    for index,lp in enumerate(count_N_zero_list):
        #粒子の存在しない場所の格子点を取得
        zero_n = lp[0]
        zero_j = lp[1]

        #追加で以下の条件を満たした場合のみ粒子を注入する
        if ( np.abs( Qfw[zero_n][zero_j] ) > (0.01/tinf.delta_t) ):
            add_P = ClassParticle.Particle(zero_n,zero_j)
            add_P.A = 0
            P_list.append(add_P)
            count_N[zero_n][zero_j] += 1
            N += 1 
    ##########################################################################
    time_evo_count_N[i+1] = count_N
    print('addparticle_end')



    print('f_start')
    #################################################################################
    #ウィグナー関数の値の更新
    f[:,:]=0
    for p,P in enumerate(P_list):
        p_n = P.index_n
        p_j = P.index_j

        f[p_j][p_n] += P.A
    #################################################################################
    time_evo_f[i+1] = f
    print('f_end')




    print('Qfw_start')
    #################################################################################
    #Qfw更新はΔtの間に全粒子のxkaの更新が終わった後に行う
    Qfw[:,:]=0
    for n in range(cst.Nx):
        for j in range(cst.Nk):
            for j2 in range(cst.Nk):
                    
                Qfw[n][j] += V[j2][n][j] * f[j2][n] 
    Qfw = -(1/cst.hbar) *  Qfw
    #################################################################################
    time_evo_Qfw[i+1] = Qfw
    print('Qfw_end')





    if i%50 == 0:
        np.save('time_evo_f',time_evo_f)
        np.save('time_evo_Qfw',time_evo_Qfw)
        np.save('time_evo_count_N',time_evo_count_N)