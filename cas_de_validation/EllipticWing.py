###########################
#Géométrie Aile Elliptique#
###########################

import numpy as np
N=25
c=[]
c0=1
theta=[]
for i in range(1,N+1):
    theta.append((i - 0.5) * np.pi/N)
    c.append(c0*np.sin(theta[i-1]))
c=np.array(c)
theta=np.array(theta)

f=open('chord.mai','w')
f.truncate(0)
for x in c:
    f.write(str(x)+'\n')
f.close()
