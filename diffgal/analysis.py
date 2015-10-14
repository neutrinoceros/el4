#-*-coding:utf-8-*-

from classes import *
from functions import *

from time import time
import numpy as np
import pylab as pl

t0=time()
print "loading data..."
bench = CRSet(SAMPLESIZE,rdpos=False)
bench.load('run1444850897.dat')

print "took {}s".format(round(time()-t0,1))

#-------------------------------
#answers to original questions :
#-------------------------------

pl.ion()
Q1(bench)
Q2(bench)
Q3(bench)

pl.ioff()
close=raw_input('press enter to end the program')
