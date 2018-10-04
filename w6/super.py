from test_engine import O
from num import Num
from rows import rows
from sym import Sym
from dom import doms
import math, random

def super(data, goal=None, enough=None):
    rows = data.rows
    if goal is None:
        goal = len(rows[0])-1
    if enough is None:
        enough = len(rows)**param_enough

    def band(c, lo, hi):
        if lo == 1:
            return ".."+str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c])+".."
        else:
            return str(rows[lo][c])+".."+str(rows[hi][c])