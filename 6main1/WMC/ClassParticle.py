import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
import os
sys.path.append('../../config/')
import cst
import time_inf as tinf



U = np.load('../../1Qdot/data/U.npy')
f = np.load('../../2f/data/f.npy')
V = np.load('../../3V/V.npy')
Qfw = np.load('../../4Qfw/Qfw.npy') 



class Particle:
    
    def __init__(self,n,j):
        self.index_n = n
        self.index_j = j
        self.x = cst.xvec[n]
        self.k = cst.kvec[j]
        self.v = cst.hbar * self.k /cst.m1
        self.A = f[j][n]

    def time_evolution(self):        
        self.x += self.v * tinf.delta_t

    def xk_index(self):
        for j in range(cst.Nk):
            if ( cst.kvec[j]-0.5*cst.delta_k <= self.k < cst.kvec[j]+0.5*cst.delta_k ):
                self.index_j = j

        for n in range(cst.Nx):
            if ( cst.xvec[n]-0.5*cst.delta_x <= self.x < cst.xvec[n]+0.5*cst.delta_x ):
                self.index_n = n
                break
            else:
                self.index_n = None


    

        


