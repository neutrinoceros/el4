#-*-coding:utf-8-*-

import numpy as np
from numpy.random import rand, randint, uniform, normal
from parameters import *


#fonction d'intégration bourine:

def integral(f,xmin,xmax,npt=1e4):
    dx = (xmax-xmin)/npt
    X = [xmin+n*dx for n in range(int(npt))]
    I = 0
    for i in range(int(npt)):
        x=X[i]
        I+=f(x)*dx
    return I

#----------------------------------
# fonctions définies dans l'énoncé
#----------------------------------

def sigma(R):
    """gas density by surface units"""
    return SIGMA0*np.exp(-R/RGAS)

def opticalDepth(R):
    return KAPPA*sigma(R)

def sourceDensity(R):
    return (1+(R/RCR)**2)**(-ALPHA)

def lambdaSpec(E):
    return LAMBDA0*E**BETA


#-------------------------
# fonctions normalisées
#-------------------------

NSD=integral(sourceDensity,0,1000*RCR)
def normalizedSourceDensity(R):
    return sourceDensity(R)/NSD


#-----------------------------------
# fonctions utiles au tirage random
#-----------------------------------

def gen_R():
    #methode du rejet
    passage = False
    while not passage :
        x1 = uniform(0,1000*RCR)
        x2 = uniform(0,1)
        if x2 < normalizedSourceDensity(x1):
            passage=True
    return x1




#-----------------------
# fonctions de plotting
#-----------------------

#...
