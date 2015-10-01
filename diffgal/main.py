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
    bench.walk0()#not well understood


#-------------------------
# plotting
#-------------------------

#...
