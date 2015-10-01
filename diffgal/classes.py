#-*-coding:utf-8-*-

from parameters import *
import numpy as np
from numpy.random import rand, uniform
import pylab as pl

#-------------------------
# def classes
#-------------------------

class CosmicRay :

    def __init__(self) :
        """constructeur d'une particule aléatoire dans le plan galactique"""
        self.r = rand()#...  
        self.h = 0.
        self.E = rand()#...

        #mu, phi : propagation direction in spherical coords
        self.mu = uniform(-1.,1.)#mu=cos(theta) is uniformly distributed
        self.phi = uniform(0.,2*np.pi)
        self.theta = 0.#python declaration...
        self.udtheta()

        #initialy the particle is neither absorbed nor away from the galaxy or its halo
        self.absorbed = False
        self.escaped = False


    def udtheta(self) :
        self.theta=np.arccos(self.mu)


    def udpos(self) :
        self.r = self.r + LIGHTC * np.sin(self.theta) * ts#radial projection of the velocity aplied
        self.h = self.h + LIGHTC * self.mu * ts#...


    def uddir(self) :
        self.mu = uniform(-1.,1.)
        self.phi = uniform(0.,2*np.pi)
        self.udtheta()
        

    def diffuse(self,ts=TIMESTEP) :
        """diffusion through the galactic plan, used for first stage of the simulation"""
        absorption_criterion=False
        #...
        #evaluate probability of being absorbed 
        #...
        if absorption_criterion :
            self.absorbed=True
        else :
            self.udpos()

        
    def propag(self,ts=TIMESTEP) :
        """propagation in the galactic halo, used for second stage of the simulation"""
        newmu = self.mu
        newphi = self.phi#default values
        newr = LIGHTC*ts#...
        newh = LIGHTC*ts#...
        #...

        if self.h*newh < 0 :#passage dans le plan galactique, possibilité d'absorption
            #...
            scattering_criterion = False
            #evaluate probability of being scattered (elastic scattering)
            #...
            if scattering_criterion :
                self.uddir(np.uniform(-1.,1.),np.uniform(0.,2*np.pi))
            
        if abs(newh) > H0 :
            ray.escaped = True

        self.udpos(newr,newh)
        self.uddir(newmu,newphi)
        

            
class CRSet :
    def __init__(self,N):
        self.rays = [CosmicRay() for n in range N]
        self.epoch = 0.
        self.isDead = False


    def.udIsDead(self):
        dead = True
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped):
                dead = False
                break
        self.isDead = dead
        print "He's dead Jim"

            
    def walk0(ts=TIMESTEP):
        #need caractèrisation de "traverser la moitié du plan gal"
        dead = True
        for ray in self.rays :
            if not ray.absorded :
                ray.diffuse(ts)
        self.udIsDead()
        

    def walk(ts=TIMESTEP):
        #utile à la deuxième phase du code, où les rayons peuvent quitter le plan gal
        for ray in self.rays :
            if not (ray.absorded or ray.escaped) :
                ray.propag(ts)
        self.udIsDead()
