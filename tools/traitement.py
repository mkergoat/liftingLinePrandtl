import numpy as np
import matplotlib.pyplot as plt

f=open('conv_maillage.txt','r')
alpha=[]
fx=[]
fy=[]
a=f.readline().split(' ')
xlabel=a[0]
y1label=a[1]
y2label=a[2]
for line in f.readlines():
	line=line.split(' ')
	alpha.append(float(line[0]))
	fx.append(float(line[1]))
	fy.append(float(line[2]))
plt.plot(alpha,(np.array(fx)-fx[-1])/fx[-1])
plt.xlabel(xlabel)
plt.ylabel(y1label)
plt.figure()
plt.plot(alpha,(np.array(fy)-fy[-1])/fy[-1])
plt.xlabel(xlabel)
plt.ylabel(y2label)
plt.show()
