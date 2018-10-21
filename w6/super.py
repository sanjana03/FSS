from num import Num
from sym import Sym
from dom import dom, doms
from rows import Rows, rows
import re, sys, math, random

#Taking values declared from config.lua and initialising
super_enough = 0.5
super_margin = 1.05

def split(Data):
	sum_elements = 0
	result = 0
	Items = Data.items()
	for i,(n,sd) in Items:
		sum_elements += n
	for i,(n,sd) in Items:
		result += n/(sum_elements+(10**(-32)))*sd
	return result

def ksort(k, sort_k):
	sort_k = sorted(sort_k, key=lambda x: str(x[k]))
	return sort_k

def dump(row):
	# Getting the rows from data
	for data in row:
		print("\t".join(str(char) for char in data))

def super(data, goal=None, enough=None):
	# Initialising all variables needed for super.py
	Data = {}
	rows = data.rows
	if goal == None:
		goal = len(rows[0]) - 1
	if enough == None:
		enough = math.pow(len(rows),super_enough)

	def band(c, lo, hi):
		# Function generates a print string from low to high
		if lo==1:
			return ".." + str(rows[hi][c])
		elif hi==most:
			return str(rows[lo][c]) + ".."
		else:
			return str(rows[lo][c])+".."+str(rows[hi][c])


	def argmin(c, lo, hi):
		# Function is use to find the best cut by creating two counters on left and right
		xl = Num([])
		xr = Num([])
		yl = Num([])
		yr = Num([])
		cut = None
		for i in range(lo, hi+1):
			xr.numInc(rows[i][c])
			yr.numInc(rows[i][goal])
		bestx = xr.sd
		besty = yr.sd
		mu = yr.mu
		n = yr.n
		if (hi-lo)>2*enough:
			for i in range(lo, hi+1):
				xl.numInc(rows[i][c])
				xr.numDec(rows[i][c])
				yl.numInc(rows[i][goal])
				yr.numDec(rows[i][goal])

				if xl.n >= enough and xr.n >= enough:
					tmpx = Num.numXpect(data,xl,xr)*super_margin
					tmpy = Num.numXpect(data,yl,yr)*super_margin
					if tmpx < bestx:
						if tmpy < besty:
							cut,bestx,besty = i, tmpx, tmpy 
		return (cut, mu, n, besty)

	def cuts(c, lo, hi, pre):
		# Function finds good cuts
		txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
		cut, mu, n, sd = argmin(c, lo, hi)
		if cut:
			print(txt)
			cuts(c, lo,	cut, pre+"|.. ")
			cuts(c, cut+1, hi, pre+"|.. ")
		else:
			s = band(c, lo, hi)
			print(txt + "==>" + str(math.floor(100*mu)))
			Data[c] = {}
			Data[c][s] = (n, sd)			
			for r in range(lo, hi+1):
				rows[r][c] = s

	def stop(c, sort_k):
		# Function to tell where to stop so that we don't get stuck with unknown values
		for i in range(len(sort_k)-1, -1, -1):
			if sort_k[i][c] != '?':
				return i
		return 0

	for c in data.indeps:
		if c in data.nums:
			rows = ksort(c, rows)
			most = stop(c, rows)
			print("\n--" + data.name[c] + "-------")
			cuts(c, 1, most, "|.. ")
	print(" ".join(str("%10s" %name) for name in data.name).replace(",",""))
	dump(rows)

	splitter = None
	sd_min = sys.maxsize
	for index in data.indeps:
		if index in data.nums:
			sd_current = split(Data[index])
			if sd_current < sd_min:
				sd_min = sd_current
				splitter = data.name[index]
	print("Splitter attribute : ", splitter)
	print("Expected Standard Deviation(SD) : ", sd_min,"\n")


def wrapper(s):
	# Wrapper class for super
	super(doms(rows(s)))

