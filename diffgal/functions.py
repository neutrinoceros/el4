#-*-coding:utf-8-*-

import numpy as np
import pylab as pl
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


def fQ3(R):
    return sourceDensity(R)*sigma(R)

NQ3=integral(fQ3,0,1000*RCR)
def normalizedfQ3(R):
    return fQ3(R)/NQ3


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



#------------------------------------
# fonctions de reponse aux questions
#------------------------------------

def Q1(myCRSet) :
    myCRSet.udStatus()
    Eabs=[r.E for r in myCRSet.abs_rays]
    
    fig,ax=pl.subplots()
    ax.hist(Eabs,alpha=ALPHA/1.5,color='r',histtype=STYLE)
    #manque barres d'erreur
    ax.set_xlabel("Energy (GeV)")
    ax.set_ylabel("# of rays absorbed")
    ax.set_xscale("log")
    ax.set_title("Q1")

def Q2(myCRSet) :
    Etot = 0.
    Eabs = 0.
    for r in myCRSet.rays :
        Etot += r.E
    for r in myCRSet.abs_rays :
        Eabs += r.E
    
    print "Q2 : Total fraction of absorbed energy estimated to : %.2e" % (Eabs/Etot)
    #manque estimation de l'incertitude

def Q3(myCRSet) :
    rabs = [ray.r for ray in myCRSet.abs_rays]
    fig,ax=pl.subplots()
    bins0=[10**n for n in np.linspace(0,1,10)]
    bins=[]
    for n in range(0,7):
        bins+=[10**(n-3)*b for b in bins0]
    #print bins

    ax.hist(rabs,bins=bins,color='r',alpha=ALPHA/1.5,histtype='bar')
    R = np.arange(0,1e3*RCR,1e-3)
    ax.plot(R,normalizedfQ3(R),c='b',lw=3,alpha=ALPHA,label=r'$\propto \Sigma(R)\times (1+(R/R_{CR})^{-\alpha}$')
    ax.set_xlabel("galactic radius (kpc)")
    ax.set_ylabel("# of rays absorbed")
    ax.legend()
    ax.set_xscale("log")
    ax.set_title("Q3")
