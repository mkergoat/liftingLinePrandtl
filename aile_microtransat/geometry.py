def getChord():
    '''
    Lit le fichier de points de l'aile
    Entrées:
        Aucune
    Sorties:
        chord: liste
        len(chord): entier, nombre de points de discrétisation du profil
    '''
    r=(open('chord.mai','r').readlines())
    chord=[]
    for x in r:
        chord.append(float(x.strip('\n')))
    return(chord,len(chord))

def getAlpha0():
    '''
    Lit le fichier des incidences locales
    Entrées:
        Aucune
    Sorties:
        alphao: liste
    '''
    r=(open('Alpha0.data','r').readlines())
    alpha0=[]
    for x in r:
        alpha0.append(float(x.strip('\n')))
    return(alpha0)
