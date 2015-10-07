#-*-coding:utf-8-*-

from parameters import *
from functions import *
import numpy as np
from numpy.random import rand, randint, uniform
import pylab as pl

#-------------------------
# def classes
#-------------------------

class CosmicRay :

    def __init__(self) :
        """constructeur d'une particule aléatoire dans le plan galactique"""
        self.r = uniform(0,RGAS)#TEMPORARY
        self.h = 0.
        self.E = uniform(EMIN,EMAX)#TEMPORARY

        #mu, phi : propagation direction in spherical coords
        self.mu = uniform(-1.,1.)#mu=cos(theta) is uniformly distributed
        self.phi = uniform(0.,2*np.pi)
        self.theta = 0.#python declaration...
        self.udtheta()

        #initialy the particle is neither absorbed nor away from the galaxy or its halo
        self.absorbed = False
        self.escaped = False

        #if rand() < absorptionProb(self.r)/2 :#une "demie traversée" à la naissance
        #    self.absorbed = True


    def udtheta(self) :
        self.theta=(-1)**randint(2)*np.arccos(self.mu)


    def getnextpos(self,ts=TIMESTEP):
        #NB : acutal radial and vertical velocities need to be adjusted to take azimutal vel into account
        nextr = self.r + LIGHTC * np.sin(self.theta) * ts#radial projection of the velocity aplied
        nexth = self.h + LIGHTC * np.cos(self.theta) * ts
        return nextr,nexth


    def udpos(self,ts=TIMESTEP) :
        """update postion"""
        self.r,self.h = self.getnextpos()


    def uddir(self) :
        """update propagation direction as a new random vector (theta,phi) in spherical coords"""
        self.mu = uniform(-1.,1.)
        self.phi = uniform(0.,2*np.pi)
        self.udtheta()
        

    def scatteringProb(self,ts=TIMESTEP):
        d=LIGHTC*ts
        mfp=LAMBDA0*self.E**BETA
        return d/mfp*np.exp(-d/mfp)


    def absorptionProb(self):
        return np.exp(opticalDepth(self.r))


    def propag(self,ts=TIMESTEP) :
        """in the galactic halo"""

        nr,nh=self.getnextpos()
        if self.h*nh < 0 :#traversée du plan galactique, possibilité d'absorption
            if rand() < self.absorptionProb() :
                self.absorbed=True

        if rand() < self.scatteringProb() :
            self.uddir()
        
        self.udpos(ts)
    
        if abs(self.h) > H0 :
            self.escaped = True
        

            
class CRSet :

    def __init__(self,N):
        self.rays = [CosmicRay() for n in range(N)]
        self.epoch = 0.
        self.isDead = False


    def udIsDead(self):
        dead = True
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped):
                dead = False
                break
        self.isDead = dead
            

    def walk(self,ts=TIMESTEP):
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped) :
                ray.propag(ts)
        self.udIsDead()
        self.epoch+=1

    def show(self) :
        r_alive=[]
        h_alive=[]
        r_esc=[]
        h_esc=[]
        r_abs=[]
        h_abs=[]
        for ray in self.rays :
            if ray.absorbed :
                r_abs.append(ray.r)
                h_abs.append(ray.h)
            elif ray.escaped :
                r_esc.append(ray.r)
                h_esc.append(ray.h)
            else :
                r_alive.append(ray.r) 
                h_alive.append(ray.h)
        pl.scatter(r_alive,h_alive,color="blue",alpha=0.8,s=.5)
        pl.scatter(r_abs,h_abs,color="red",alpha=0.8,s=.5)
        pl.scatter(r_esc,h_esc,color="green",alpha=0.8,s=.5)

        #rmin,rmax=ax.get_xlim()
        rrr=np.linspace(0,1e3,100)
        lim=H0*np.ones(100)
        pl.plot(rrr,-lim,color='k')
        pl.plot(rrr,+lim,color='k')
        #ax.fillbetween()...

