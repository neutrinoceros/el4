#-*-coding:utf-8-*-

import numpy as np
from parameters import *


#----------------------------------
# fonctions définies dans l'énoncé
#----------------------------------

def sigma(R):
    """gas density by surface units"""
    return SIGMA0*np.exp(-R/RGAS)

def opticalDepth(R):
    return KAPPA*sigma(R)

def absorptionProb(R):
    return np.exp(opticalDepth(R))

def sourceDensity(R):
    return (1+(R/RCR)**2)**(-ALPHA)

def lambdaSpec(E):
    return LAMBDA0*E**BETA


#-----------------------------------
# fonctions utiles au tirage random
#-----------------------------------

#...



#-----------------------
# fonctions de plotting
#-----------------------

#...