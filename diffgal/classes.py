#-*-coding:utf-8-*-

from parameters import *
import numpy as np
from numpy.random import rand
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
        self.mu = # ??? ...
        self.phi = 0#diffusion purement radiale initialement
        self.absorbed = False
        self.escaped = False

    def udpos(self,newr,newh) :
        self.r=newr
        self.h=newh


    def uddir(self,newmu,newphi) :
        self.mu = newmu
        self.phi = newphi

        
    def diffuse(self,ts=TIMESTEP) :
        #ts : timestep
        """diffusion through the galactic plan"""
        newmu = self.mu
        newphi = self.phi#default values
        newr = LIGHTC*ts#...
        newh = LIGHTC*ts#...
        #...


    def propag(self,ts=TIMESTEP) :
        """propagation in the galactic halo"""
        newmu = self.mu
        newphi = self.phi#default values
        newr = LIGHTC*ts#...
        newh = LIGHTC*ts#...
        #...

        if self.h*newh < 0 :#passage dans le plan galactique, possibilité d'absorption
            #...
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

            
    def walk0(ts=TIMESTEP):
        #need caractèrisation de "traverser la moitié du plan gal
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
