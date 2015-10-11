#-*-coding:utf-8-*-

from classes import *
from functions import *

from time import time
import numpy as np
import pylab as pl


#-------------------------
# script
#-------------------------
#fig,ax=pl.subplots()
pl.ion()
fig=pl.figure()

print "sourcing %.1e particles..." % (SAMPLESIZE)
t1=time()
bench = CRSet(int(SAMPLESIZE))
print "took {}s".format(round(time()-t1,1))
print "entering main loop"

while bench.epoch < MAXEPOCH and not bench.isDead :
    bench.walk()
    if bench.epoch%10==0 :
        fig.clf()
        pl.xlim(0,10*RCR)
        pl.ylim(-H0-1,H0+1)
        bench.show()
        pl.draw()

pl.figure(2)
bench.hist()
pl.ioff()

if bench.epoch == MAXEPOCH :
    print "MAXEPOCH reached"
else :
    print "every particle was either absorbed or escaped"

close=raw_input('press enter to end the program')
