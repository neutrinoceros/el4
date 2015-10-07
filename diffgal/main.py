#-*-coding:utf-8-*-

from classes import *
from functions import *

import numpy as np
import pylab as pl

#-------------------------
# script
#-------------------------
#fig,ax=pl.subplots()
pl.ion()
fig=pl.figure()

bench = CRSet(int(1e4))
while bench.epoch < MAXEPOCH and not bench.isDead :
    bench.walk()
    if bench.epoch in [1,MAXEPOCH] or bench.epoch % 5 == 0 :
        fig.clf()
        pl.xlim(0,5e1)
        pl.ylim(-H0-1,H0+1)
        bench.show()
        pl.draw()


pl.ioff()

if bench.epoch == MAXEPOCH :
    print "MAXEPOCH reached"
else :
    print "every particle was rather absorbed or escaped"

close=raw_input('press enter to end the program')


#-------------------------
# plotting
#-------------------------
# fig,ax=pl.subplots()
# R=np.arange(-100,100,1e-2)

# #...
# #ax.loglog(R,sigma(R))
# #ax.loglog(R,opticalDepth(R))
# #ax.semilogx(R,absorptionProb(R))
# #ax.plot(R,sourceDensity(R))

# #ax.plot(R,np.arccos(R))
# bench.show(ax)

#pl.show()
