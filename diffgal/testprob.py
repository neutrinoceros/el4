from classes import *
from parameters import *
from functions import *

M = 1./(EMAX-EMIN)
def gen_E(E1=EMIN,E2=EMAX):

    passage=False
    while not passage :
        x1 = uniform(E1,E2)
        x2 = uniform(0,M)
        if x2 < np.log(x1) :
            passage = True
    return x1

# ens = [gen_E() for n in range(int(1e7))] 
# pl.figure()
# pl.xlim(EMIN,EMAX)
# pl.hist(ens,bins = 100, normed = 1)

# x=np.arange(EMIN,EMAX,10)
# #pl.plot(x,np.log(x)*M)


def gauss(x,sigma=1.,loc=0.):
    N=np.sqrt(2*np.pi*sigma**2)
    return np.exp(-(x-loc)**2/sigma**2)/N


#M = integral(normalizedSourceDensity,0,1000*RCR)
#print M
R=np.arange(0.1,10*RCR,1e-2)
Z=np.exp(-opticalDepth(R))
print Z
pl.plot(R,Z)
#pl.plot(R,gauss(R,sigma=15.))
#pl.plot(R,np.exp(-R))


#rs = [gen_R() for n in range(int(1e3))] 
#pl.hist(rs,bins = 100, normed = 1)


pl.show()
