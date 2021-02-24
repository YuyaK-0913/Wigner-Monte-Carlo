import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import sys 
sys.path.append('../config/')
import cst
import time_inf as tinf
import os

plt.rcParams['font.family']='Times New Roman'
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=15
plt.rcParams['axes.labelpad'] = -10

psi1 = np.load('data/psi1_x.npy')
psi2 = np.load('data/psi2_x.npy')
psi = np.load('data/psi_x.npy')
E1 = np.load('data/E1.npy')
E2 = np.load('data/E2.npy')
print( (E2-E1)/cst.eV )



#位相
t = tinf.delta_t /3
t = t *10**3
t = t*2

omega1 = E1 / cst.hbar
delta_theta1 = omega1 * t

omega2 = E2 / cst.hbar
delta_theta2 = omega2 * t

delta_E = (2*np.pi) * cst.hbar / t
print( delta_E/cst.eV )



