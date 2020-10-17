##################################
#### Code Ligne Portante LiPo ####
#### Mathieu Kergoat, AS 2020 ####
##################################

import ligneportante as lp
import geometry as geo
from tools.postlipo import post
import numpy as np
import matplotlib.pyplot as plt
'''
Fichier principal du code. Interpétation des entrées, 
calculs élémentaires et bouclage sur les différentes incidences. 
Appel des autres routines auxiliaires (ligneportante.py, geometry.py, postlipo.py)
'''
f = open('setup.in', 'r') 
b = float(f.readline())
S = float(f.readline())
u0 = float(f.readline())
rho = float(f.readline())
lbda = 4*b**2/S
Nalpha = f.readline()
alphas = np.linspace(float(f.readline()), float(f.readline()), Nalpha)
f.close()
c,N = geo.getChord()
alpha0 = geo.getAlpha0()
sto = []
for alpha in(alphas):
    A = lp.solveAlpha(c, alpha0, b, N, alpha)
    sto.append(A)
post(alphas,lbda,sto,u0)
