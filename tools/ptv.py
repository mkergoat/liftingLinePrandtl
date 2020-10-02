import numpy as np

def portance(alphas,u0,rho,S):
    CL=[]
    f=open('res.out','r')
    a=f.readlines()
    for k in a:
        l=k.split('\t')[:-1]
        CL.append(float(l[1]))
    CL=np.array(CL)
    L=1/2*rho*S*u0**2*CL
    f.close()
    return(alphas,L)
    
def trainee(alphas,u0,rho,S):
    CD=[]
    f=open('res.out','r')
    a=f.readlines()
    for k in a:
        l=k.split('\t')[:-1]
        CD.append(float(l[1]))
    CD=np.array(CD)
    D=1/2*rho*S*u0**2*CD
    f.close()
    return(alphas,D)
    
def downwash(alphas,sto,u0,N):
    '''
    Calcule les vitesses induites w_i
    Entrées:
        alphas: array, incidences de calcul
        sto: list, vecteurs de décomposition (Ai)1<i<N pour chaque incidence
        u0: float, vitesse de l'écoulement infini amont
    Sorties:
        liste contenant les vecteurs w_i(theta_i)
    '''
    theta=[]
    for i in range(1,N+1):
        theta.append((i - 0.5) * np.pi/N)
    wadim=[]
    for A in sto:
        wadimInc=[]
        for i in range(0,N):
            wadimi=0
            for j in range(1,N):
                wadimi+=j*A[j-1]*np.sin(j*theta[i])/np.sin(theta[i])
            wadimInc.append(-u0*wadimi)
        wadim.append(wadimInc)
    return(wadim)