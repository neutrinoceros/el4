#-*-coding:utf-8-*-

from classes import *
from functions import *

from time import time
import numpy as np
import pylab as pl


#-------------------------
# script
#-------------------------
pl.ion()
fig=pl.figure()

print "sourcing %.1e particles..." % (SAMPLESIZE)
t1=time()
bench = CRSet(int(SAMPLESIZE))
print "took {}s".format(round(time()-t1,1))
print "entering main loop"

while bench.epoch < MAXEPOCH and not bench.isDead :
    bench.walk()
    if bench.epoch%1e1==0 :
        fig.clf()
        pl.xlim(0,2*RCR)
        pl.ylim(-H0-1,H0+1)
        bench.show()
        pl.draw()


# pl.figure(2)
# bench.hist()


if bench.epoch == MAXEPOCH :
    print "MAXEPOCH reached"
else :
    print "every particle was either absorbed or escaped"

svgname = 'run{}.dat'.format(int(time())) 
with open(svgname,'w') as svgf:
    svgf.write(bench.__repr__())
print 'results saved under {} !'.format(svgname)

#-------------------------------
#answers to original questions :
#-------------------------------
#Q1(bench)
#Q2(bench)
#Q3(bench)

pl.ioff()
close=raw_input('press enter to end the program')
