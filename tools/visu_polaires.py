import numpy as np
import matplotlib.pyplot as plt
import matplotlib2tikz as pltt
'''
Ce code permet d'afficher facilement les polaires CL=f(alpha), CD=f(alpha)
Il enregistre aussi les graphes en sortie retracés par Tikz pour intégration
dans un rapport LaTeX.
Entrées:
    res.out: fichier txt:   fichier de sortie de postlipo
Sorties:
    graph1.tex:     fichier .tex:   figure TikZ du premier graphique
    graph2.tex:     fichier .tex:   figure TikZ du deuxième graphique
'''
f=open('res.out','r')
alpha=[]
fx=[]
fy=[]
a=f.readline().split(' ')
xlabel=a[0]
y1label=a[1]
y2label=a[2]
for line in f.readlines():
	line=line.split('\t')
	alpha.append(float(line[0]))
	fx.append(float(line[1]))
	fy.append(float(line[2]))
plt.plot(alpha,np.array(fx),marker='+')
plt.xlabel(xlabel)
plt.ylabel(y1label)
pltt.save('graph1.tex')
plt.figure()
plt.plot(alpha,np.array(fy),marker='+')
plt.xlabel(xlabel)
plt.ylabel(y2label)
pltt.save('graph2.tex')
plt.show()
