###########################
#  Géométrie Aile Réelle  #
###########################

import numpy as np
N=100
cord = np.linspace(1062.049, 404.76, N)
cord[0:(int(N*230/2500))] += np.linspace(-300,0,int(N*230/2500))
cord[0:(int(N*400/2500))] += np.linspace(-556,0,int(N*400/2500))
cord[int(N*2352/2500):] = -np.linspace(-440,0,len(cord[int(N*2352/2500):]))

cord=cord/1000
print(cord)

f=open('chord.mai','w')
f.truncate(0)
for x in cord:
    f.write(str(x)+'\n')
f.close()
