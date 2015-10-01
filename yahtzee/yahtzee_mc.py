#-*- coding : utf-8 -*-

from random import randint
import numpy as np
import pylab as pl


diedict={1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
FANCYPRINTING=False

class Dice :
    def __init__(self,n):
        self._facenumber=n
        self._faceup=0#this value can not be reached otherwise. A null dice is a dice that was never rolled or reseted.
        self._islocked=False

    def roll(self):
        if not self._islocked :
            self._faceup=randint(1,self._facenumber)
        #return self._faceup
        
    def lock(self):
        self._islocked=True
    
    def unlock(self):
        self._islocked=False

    def __repr__(self):
        return str(self._faceup)


class Set :
    """a set of dices"""

    def __init__(self,m,n):
        self._diceNumber=m
        self._faceNumber=n
        self._dices=[Dice(n) for i in range(m)]
        self._facesup=[d._faceup for d in self._dices]
        self._state=1
        self._target=0
        self._rollcount=0

    def roll(self):        
        for d in self._dices:
            d.roll()
        self._facesup=[d._faceup for d in self._dices]
        self._rollcount+=1
        

    def updatelocking(self,target):
        for d in self._dices :
            if d._faceup == target :
                d.lock()
            else :
                d.unlock()


    def updatestate(self):
        L=[]
        for val in range(1,self._faceNumber+1):
            L.append(self._facesup.count(val))
        L1=[n for n in L]#copy
        L1.sort()
        self._state=L1[-1]#get the population of the largest group of identical dices
        self._target=L.index(self._state)+1


    def reset(self):
        for d in self._dices:
            d.unlock()
        self._target=0
        self._state=1
        self._rollcount=0


    def __repr__(self):
        if FANCYPRINTING :
            string=' '.join([diedict[f] for f in self._facesup])
        else :
            string=' '.join([str(f) for f in self._facesup])
        return string

            
    def play(self,maxroll):
        while self._rollcount<maxroll :
            self.roll()
            self.updatestate()
            if self._state == self._diceNumber :
                break            
            self.updatelocking(self._target)
                    


#--------------------------------------------------
#                     SCRIPT
#--------------------------------------------------

yset=Set(5,6)#5 6-faced dices

GAMENUMBER=int(1000)
e=[]
VICTORIES=[]
V=0

for t in range(GAMENUMBER):
    yset.play(3)
    if yset._state==5:
        print yset, "yahtzee !"
    else:
        print yset

    if yset._state==yset._diceNumber:
        VICTORIES.append(1)
        V+=1 
    else :
        VICTORIES.append(0)

    vrate=float(V)/float(t+1)*100
    e.append(vrate)
    yset.reset()

    if t>0 and t%int(1e5)==0 :
        print t,"games played, won",vrate,"%"


#V=VICTORIES.count(1) 
vrate=float(V)/float(GAMENUMBER)*100

print "------------------------------------------------------------------------------"
print "Final results, for",GAMENUMBER,"games played, ",V, "victories were reached."
print "Estimated probability of victory :",vrate,"%"
print "------------------------------------------------------------------------------"

x=np.arange(GAMENUMBER)
with open("results.dat",'w') as fi:
    for i in range(GAMENUMBER):
        fi.write(str(x[i])+"    "+str(e[i])+"\n")

fig,ax=pl.subplots()
ax.semilogx(x,e)
ax.set_xlim(100,GAMENUMBER)
ax.set_ylim(0,7)
ax.set_xlabel("games played",size=20)
ax.set_ylabel("yahtzee rate (%)",size=20)
pl.savefig("yahtzee_mc.pdf")
