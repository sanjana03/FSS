import math
from num import Num
from sym import Sym
from test import O
import re, sys
import pandas as pd

class Rows:
    def __init__(self):
        '''Initializing all the variables'''
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []
        
    def indep(self,c):
        '''Checking if the column is independent'''
        return not c in self.w and self._class!=c

    def dep(self,c):
        '''For checking if the column is dependent'''
        return not indep(self,c)

    def header(self,cells):
        '''Checks for certain symbols at the beginning of the column name and structure then into sym and num objects'''
        self = self or Rows()
        self.indep = []
        for c0,x in enumerate(cells):
            if not "?" in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
                # Col names beginning with $,<,> are set as numeric columns
                if "$" in x or "<" in x or ">" in x:
                    self.nums[c] = Num([])
                else:
                    self.syms[c] = Sym([])
                if "<" in x:
                    self.w[c] = -1
                elif ">" in x:
                    self.w[c] = 1
                elif "!" in x:
                    self._class = c
                else:
                    self.indeps.append(c)
        return self

    def row(self, cells):
        '''Reading data and adding to the headers extracted in the previous function'''
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x!="?":
                if c in self.nums:
                    x = round(float(x),2)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)
        return self


def rows1(stream):
    '''After reading data, this function processes the various matrix needed'''
    first = True
    line = Rows()
    for line1 in stream:
        line1 = re.sub(r'([\n\r\t]|#.*)', "", line1)
        cells = line1.split(",")
        if len(cells)>0 :
            if first :
                line.header(cells)
            else :
                line.row(cells)
            first=False
    
    df_idx = list()
    df_name = list()
    df_n = list()
    df_mode = list()
    df_freq = list()

    for k, v in line.syms.items():
        #Getting n,mode and frequency from syms
        df_idx.append(k+1)
        df_name.append(line.name[k])
        df_n.append(v.n)
        df_mode.append(v.mode)
        df_freq.append(v.most)

    #print(pd.DataFrame({" ":df_idx, " ":df_name, "n":df_n, "Mode":df_mode, "Freq":df_freq}))
    
    df_idx = list()
    df_name = list()
    df_n = list()
    df_mu = list()
    df_sd = list()

    #print('\n')
    for k, v in line.nums.items():
        # Getting n, mu, standard deviation from nums
        df_idx.append(k+1)
        df_name.append(line.name[k])
        df_n.append(v.n)
        df_mu.append(round(v.mu,2))
        df_sd.append(round(v.sd,2))
        
    #print(pd.DataFrame({" ":df_idx, " ":df_name, "n":df_n, "mu":df_mu, "sd":df_sd}))
    return line

def getlines(srcfile=None):
    '''Getting each line and sending it to rows1'''
    if srcfile == None:
        for line in sys.stdin:
            yield line
    elif srcfile[-3:] in ["csv"]:
        with open(srcfile) as file:
            for line in file:
                yield line
    else:
        for line in srcfile.splitlines():
            yield line

def rows(s):
    '''Reading the whole data and generating relevant matrix'''
    return(rows1(getlines(s)))

#Calling test cases for various datasets
# @O.k
# def test():
#     print("\nweather.csv\n")
#     rows("weather.csv")
#     print("\nweatherLong.csv\n")
#     rows("weatherLong.csv")
#     print("\nauto.csv\n")
#     rows("auto.csv")