import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz as pltt

f = open('setup.in','r') 
b = float(f.readline())
S = float(f.readline())
lbda = 4*b**2/S
f.close()

f=open('res.out','r')
alpha=[]
fx=[]
fy=[]
a=f.readline().split(' ')
xlabel=a[0]
for line in f.readlines():
    line=line.split('\t')
    alpha.append(float(line[0]))
    fx.append(float(line[2]))
    fy.append(float(line[1]))
CL2D = 2*np.pi*np.array(alpha)*np.pi/180
CL3DP = CL2D * lbda/(lbda+2) #prandtl correction
CL3DH = CL2D * (lbda/(2+np.sqrt(lbda**2+4))) #hembold
CD3DP = CL3DP**2/(np.pi*lbda)
CD3DH = CL3DH**2/(np.pi*lbda)
plt.plot(alpha,np.array(fy),marker='+',label='Ligne Portante')
plt.plot(alpha,CL3DH, marker='.', label='Helmbold')
plt.plot(alpha,CL3DP, marker='x', label='Prandtl')
plt.xlabel(xlabel)
plt.ylabel('$C_L$')
plt.legend()
pltt.save('comp_CL.tex')
plt.figure()
plt.plot(alpha,np.array(fx),marker='+',label='Ligne Portante')
plt.plot(alpha,CD3DH, marker='.', label='Helmbold')
plt.plot(alpha,CD3DP, marker='x', label='Prandtl')
plt.xlabel(xlabel)
plt.ylabel('$C_D$')
plt.legend()
pltt.save('comp_CDi.tex')
plt.show()
print('Erreur relative max entre CL_LignePortante et CL_Prandtl: '+str(max(abs(np.array(fy)[1:]-CL3DP[1:])/np.array(fy)[1:])))
print('Erreur relative max entre CL_LignePortante et CL_Helmbold: '+str(max(abs(np.array(fy)[1:]-CL3DH[1:])/np.array(fy)[1:])))
print('Erreur relative max entre CD_LignePortante et CD_Prandtl: '+str(max(abs(np.array(fx)[1:]-CD3DP[1:])/np.array(fx)[1:])))
print('Erreur relative max entre CD_LignePortante et CD_Helmbold: '+str(max(abs(np.array(fx)[1:]-CD3DH[1:])/np.array(fx)[1:])))