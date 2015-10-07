#-*-coding:utf-8-*-

from classes import *
from functions import *

import numpy as np
import pylab as pl

#-------------------------
# script
#-------------------------
#fig,ax=pl.subplots()
fig=pl.figure(1)
ax=fig.add_subplot(111)
pl.ion()
pl.draw()
bench = CRSet(int(1e4))
while bench.epoch < MAXEPOCH and not bench.isDead :
    bench.walk()
    if bench.epoch % 10 == 0 :
        #fig.clf()
        print 'hey'
        bench.show(ax)
        pl.draw()

if bench.epoch == MAXEPOCH :
    print "MAXEPOCH reached"
else :
    print "every particle was rather absorbed or escaped"


#bench.show(ax);pl.show()


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
