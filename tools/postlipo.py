import numpy as np

def post(alphas,lbda,sto,u0):
    '''
    A partir des coefficients de la décomposition de l'intensité tourbillonnaire,
    on calcule les coefficients utiles CL, CD ainsi que le downwash wi et on les écrit dans un fichier 
    pour post-traitements additionnels
    Entrées:
        alphas:     array:              vecteur des incidences
        lbda:       float:              aspect ratio 
        sto:        list:               liste des vecteurs coefficients An
        u0:         float:              vitesse infini amont
    Sorties:
        res.out:    fichier texte:      CL et CD calculés
        wi.out:     fichier texte:      downwash
    '''
    f = open('res.out','a')
    f.truncate(0)
    f.write('alpha'+' '+'CL'+' '+'CD'+' '+'dummy'+'\n')
    j = 0
    for A in sto:
        alpha=alphas[j]
        CL = np.pi*lbda*A[0]
        CD = 0
        N=len(A)
        for i in range(0,N-1):
            CD = CD+np.pi*lbda*(i+1)*A[i]**2
        f.write(str(alpha)+'\t'+str(float(CL))+'\t'+str(float(CD))+'\t'+'0'+'\n')
        j += 1
    f.close()
    f = open('wi.out','a')
    f.truncate(0)
    f.write('alpha'+' '+'wi'+' '+'dummy'+'\n')
    theta=[]
    for i in range(1,N+1):
        theta.append((i - 0.5) * np.pi/N)
    k=0
    for A in sto:
        alpha=alphas[k]
        wadim=[]
        for i in range(0,N):
            wadimi=0
            for j in range(1,N):
                wadimi+=j*A[j-1]*np.sin(j*theta[i])/np.sin(theta[i])
            wadim.append(wadimi)
        f.write(str(alpha)+'\t'+str(-u0*np.array(wadim))+'\t'+'0'+'\n')
        k=0   
    f.close()