import math
class Sym:
    def __init__(self, l, f=lambda x: x):
        self.counts = dict()
        self.mode = None
        self.most = 0
        self.n = 0
        self.ent = None
        for i in l:
            self.symInc(f(i))

    def symInc(self, x):
        if x == "?":
            return x
        self.ent = None
        self.n += 1
        old = self.counts.get(x)
        new = old + 1 if old else 1
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x
        return x

    def symDec(self, x):
        self.ent = None
        if self.n > 0:
            self.n -= 1
            self.counts[x] -= 1
        return x

    def symEnt(self):
        if self.ent==None:
            self.ent = 0
            p=0
            for i in self.counts.values():
                p = i / self.n
                self.ent = self.ent - p*math.log(p,2)
        return self.ent