################
# Circulations #
################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz as pltt
alpha = 3*np.pi/180
N = 25
b = 3
c0=1 
c=[]
theta=[]
for i in range(1,N+1):
    theta.append((i - 0.5) * np.pi/N)
    c.append(c0*np.sin(theta[i-1]))
c=np.array(c)
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
gammaNum=0
for i in range(0,N):
    gammaNum+=A[i]*np.sin((i+1)*theta)
theta2=np.linspace(0,np.pi,200)
A1=c0*np.pi*alpha/(4*b+c0*np.pi)
gamma=4*b*A1*np.sin(theta2)
# plt.plot(A,linestyle='',marker='+')
# plt.xlabel('$n$')
# plt.ylabel('Amplitude décomposition série de Fourier $A_n$')
# pltt.save('amp.tex')
# plt.figure()
plt.plot(theta2, gamma,label='théorique')
plt.plot(theta,4*b*gammaNum,label='numérique',marker='x')
plt.legend()
plt.xlabel('$\theta$ (rad)')
plt.ylabel('$\gamma$/$U_0$ (m$^{-1})$')
plt.title('Incidence '+str(180*alpha/np.pi)+' deg')
pltt.save('circ.tex')
