#-*-coding:utf-8-*-

from parameters import *
from functions import *
import numpy as np
from numpy.random import rand, uniform
import pylab as pl

#-------------------------
# def classes
#-------------------------

class CosmicRay :

    def __init__(self) :
        """constructeur d'une particule aléatoire dans le plan galactique"""
        self.r = uniform(-RGAS,RGAS)#(rand()-rand())*RGAS#TEMP  
        self.h = 0.
        self.E = uniform(EMIN,EMAX)#EMIN + (rand()-rand())*(EMAX-EMIN)#TEMP

        #mu, phi : propagation direction in spherical coords
        self.mu = uniform(-1.,1.)#mu=cos(theta) is uniformly distributed
        self.phi = uniform(0.,2*np.pi)
        self.theta = 0.#python declaration...
        self.udtheta()

        #initialy the particle is neither absorbed nor away from the galaxy or its halo
        self.absorbed = False
        self.escaped = False

        if rand() < absorptionProb(self.r)/2 :#une "demie traversée" à la naissance
            self.absorbed = True


    def udtheta(self) :
        self.theta=np.arccos(self.mu)


    def getnextpos(self,ts=TIMESTEP):
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
        

    def propag(self,ts=TIMESTEP) :
        """in the galactic halo"""

        nr,nh=self.getnextpos()
        if self.h*nh < 0 :#traversée du plan galactique, possibilité d'absorption
            absorption_criterion=False
            #...
            #evaluate probability of being absorbed
            #...
            if absorption_criterion :
                self.absorbed=True


        scattering_criterion = False
        #...
        #evaluate probability of being scattered (elastic scattering)
        #...
        if scattering_criterion :
            self.uddir()

            
        if abs(nh) > H0 :
            self.escaped = True

        else :
            self.udpos(ts)


            
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
        print "He's dead Jim"

            
    # def walk0(ts=TIMESTEP):
    #     #need caractèrisation de "traverser la moitié du plan gal"
    #     for ray in self.rays :
    #         if not ray.absorded :
    #             ray.diffuse(ts)
    #     self.udIsDead()
    #     self.epoch+=1
        

    def walk(self,ts=TIMESTEP):
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped) :
                ray.propag(ts)
        self.udIsDead()
        self.epoch+=1

    def show(self,ax) :
        radii = [ray.r for ray in self.rays]
        heights = [ray.h for ray in self.rays]
        ax.scatter(radii,heights)

        rmin,rmax=ax.get_xlim()
        ax.plot(np.linspace(rmin,rmax,100),-H0*np.ones(100),color='k')
        ax.plot(np.linspace(rmin,rmax,100),+H0*np.ones(100),color='k')

