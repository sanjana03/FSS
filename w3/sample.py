import random
import math

class Sample:
    def __init__(self, maximum):
        self.maximum=maximum
        self.rank=1
        self.n=0
        self.sorted=False
        self.some=[]
    
    def sampleInc(self,x):
        self.n += 1
        now=len(self.some)
        if now < self.maximum:
            self.sorted = False
            self.some.append(x)
        elif random.uniform(0,1) < now / (self.n) :
            self.sorted = False
            self.some[int(random.uniform(0,1)*now)]=x
        return x
    
    def sampleSorted(self):
        if self.sorted == False:
            self.sorted = True
            self.some.sort()

        return self.some
    
    def nth(self, n):
        s = self.sampleSorted()
        return s[min(len(s), max(1, int(math.floor(0.5+(n*len(s))))))]
                
    def nths(self, ns,out):
        if ns is None:
            ns = [0.1,0.3,0.5,0.7,0.9]
        out = []
        for _,n in enumerate(ns):
            out.append(self.nth(n))
        
        return out
    def sampleLt(self, s1, s2):
            return self.nth(s1, 0.5) < self.nth(s2, 0.5)

    