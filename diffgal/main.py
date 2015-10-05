#-*-coding:utf-8-*-

from classes import *
from functions import *

import numpy as np
import pylab as pl

#-------------------------
# script
#-------------------------

bench = CRSet(int(1e5))
while bench.epoch < MAXEPOCH and not bench.isDead :
    bench.walk()


#-------------------------
# plotting
#-------------------------

#...
fig,ax=pl.subplots()
R=np.arange(-100,100,1e-2)
#ax.loglog(R,sigma(R))
#ax.loglog(R,opticalDepth(R))
#ax.semilogx(R,absorptionProb(R))
#ax.plot(R,sourceDensity(R))

ax.plot(R,np.arccos(R))
#bench.show(ax)

pl.show()
