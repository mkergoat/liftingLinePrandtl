import numpy as np

def solveAlpha(c,alpha0,b,N,alpha):
    '''
    Calcule les coefficients An de la décomposition de l'intensité tourbilonnaire
    Entrées:
        c: array : loi de corde 
        alpha0 : array : loi de vrillage
        b : float : demi-envergure
        N : integer : nombre de points de discrétisation géométrique
        alpha: float: incidence de calcul
    Sorties:
        A: array : matrice des coefficients An
    '''
    alpha = np.pi/180*alpha
    theta=[]
    for i in range(1,N+1):
        theta.append((i - 0.5) * np.pi/N)
    theta=np.array(theta)
    M = []
    for i in range(0,N):
        M.append([])
        for j in range(1,N+1):
            M[i].append((4*b+np.pi*c[i]*j/np.sin(theta[i]))*np.sin(theta[i]*j))
    B=[]
    for i in range(0,N):
        B.append(np.pi*c[i]*alpha)
    A = np.linalg.solve(np.array(M),np.array(B))
    return(A)