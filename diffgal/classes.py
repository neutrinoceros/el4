#-*-coding:utf-8-*-

from parameters import *
from functions import *
import numpy as np
import pylab as pl

#-------------------------
# def classes
#-------------------------

class CosmicRay :

    def __init__(self) :
        """constructeur d'une particule aléatoire dans le plan galactique"""
        self.r = gen_R()
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

        if rand() < self.absorptionProb()/2 :#une "demie traversée" à la naissance
            self.absorbed = True


    def udtheta(self) :
        self.theta=(-1)**randint(2)*np.arccos(self.mu)


    def getnextpos(self,ts=TIMESTEP):
        #NB : acutal radial and vertical velocities need to be adjusted to take azimutal vel into account
        azimutal_v = LIGHTC * np.sin(self.phi) 
        radial_v   = LIGHTC * np.cos(self.phi) * np.sin(self.theta)
        vertical_v = LIGHTC * np.cos(self.phi) * np.cos(self.theta)
        nextr = np.abs(self.r + radial_v * ts)
        nexth = self.h + vertical_v * ts
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
        return 1.-np.exp(-opticalDepth(self.r))


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
        self.alive_rays = []
        self.esc_rays = []
        self.abs_rays = []
        self.udStatus()

        
    def udIsDead(self):
        dead = True
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped):
                dead = False
                break
        self.isDead = dead
            

    def udStatus(self):
        self.abs_rays = []
        self.esc_rays = []
        self.alive_rays = []
        for ray in self.rays :
            if ray.absorbed :
                self.abs_rays.append(ray)
            elif ray.escaped :
                self.esc_rays.append(ray)
            else :
                self.alive_rays.append(ray)


    def walk(self,ts=TIMESTEP):
        for ray in self.rays :
            if not (ray.absorbed or ray.escaped) :
                ray.propag(ts)
        self.udIsDead()
        self.epoch+=1


    def show(self) :
        self.udStatus()
        r1 = [ray.r for ray in self.alive_rays]
        r2 = [ray.r for ray in self.abs_rays]
        r3 = [ray.r for ray in self.esc_rays]
        h1 = [ray.h for ray in self.alive_rays]
        h2 = [ray.h for ray in self.abs_rays]
        h3 = [ray.h for ray in self.esc_rays]
        pl.scatter(r1,h1,color="blue",alpha=ALPHA,s=SIZE)
        pl.scatter(r2,h2,color="red",alpha=ALPHA,s=SIZE)
        pl.scatter(r3,h3,color="green",alpha=ALPHA,s=SIZE)

        #rmin,rmax=ax.get_xlim()
        rrr=np.linspace(0,1000*RCR,3)
        lim=H0*np.ones(len(rrr))
        pl.plot(rrr,-lim,color='k')
        pl.plot(rrr,+lim,color='k')
        #ax.fillbetween()...


    def hist(self) :
        self.udStatus()
        r_alive = [ray.r for ray in self.alive_rays]
        r_abs   = [ray.r for ray in self.abs_rays]
        r_esc   = [ray.r for ray in self.esc_rays]
        pl.hist([r_abs,r_esc,r_alive],bins=100,range=(0,10*RCR),color=['r','g','b'],alpha=ALPHA/1.5,histtype=STYLE,stacked=True)
