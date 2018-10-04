import re, sys, random, math
from num import Num
from sym import Sym
from rows import Rows, rows
from test import O

n = 100

def another(r, rows):
    range_max = int(0.5 + random.random() * len(rows)) - 1
    val = max(0, range_max) 
    if r == val:
    	return another(r, rows)
    else:
    	return rows[val]

def dump(rows):
    for row in rows:
        x = len(row) - 1
        row[x] = str("%.2f"%row[x])
        for r in row:
        	print("\t" + str(r), end = '')
        print()

def dom(t, row1, row2):
    s1 = 0
    s2 = 0
    n = len(t.w)
    for c, w in t.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = t.nums[c].numNorm(a0)
        b = t.nums[c].numNorm(b0)
        s1 -= math.pow(10, (w*(a-b)/n))
        s2 -= math.pow(10, (w*(b-a)/n))
    return (s1/n < s2/n)
        
def doms(t):
    c = len(t.name)
    print("\t"+ str(t.name) +"\t"+">dom")
    for r1, row1 in enumerate(t.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, t.rows)
            s = dom(t, row1, row2) and 1/n or 0
            row1[c] = row1[c] + s
    dump(t.rows)

def mainDom(file):
    doms(rows(file))
