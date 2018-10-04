from test import O
from num import Num
from sym import Sym
from dom import dom
from rows import Rows, rows
import re, sys, math, random

x = 0.5
y = 1.05

def ksort(k, t):
	t = sorted(t, key=lambda x: str(x[k]))
	return t

def dump(row):
	for data in row:
		for char in data:
			print("\t" + str(char), end = '')
		print()

def unsuper(data):
	rows = data.rows
	enough = math.pow(len(rows), x)

	def band(c, lo, hi):
		if lo == 1:
			return ".." + str(rows[hi][c])
		elif hi == most:
			return str(rows[lo][c]) + ".."
		else:
			return str(rows[lo][c]) + ".." + str(rows[hi][c])

	def argmin(c, lo, hi):
		cut = None
		if ((hi - lo) > 2*enough):
			l = Num([])
			r = Num([])
			for i in range(lo, hi+1):
				r.numInc(rows[i][c])
			best = r.sd
			for i in range(lo, hi+1):
				x = rows[i][c]
				l.numInc(x)
				r.numDec(x)

				if l.n >= enough:
					if r.n >= enough:
						tmp = Num.numXpect(data, l, r) * y
						if tmp < best:
							cut = i
							best = tmp
		return cut


	def cuts(c, lo, hi, pre):
		txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
		cut = argmin(c ,lo, hi)
		if (cut):
			print(txt)
			cuts(c, lo, cut, pre + "|..")
			cuts(c, cut+1, hi, pre + "|..")
		else:
			b = band(c, lo, hi)
			print(txt + " (" + b + ")")
			for r in range(lo, hi+1):
				rows[r][c] = b

	def stop(c, t):
		for i in range(len(t) - 1, 1, -1):
			if not t[i][c] == "?":
				return i
		return 0

	for c in data.indeps:
		if c in data.nums:
			ksort(c, rows)
			most = stop(c, rows)
			print("\n---" + str(data.name[c]) + str(most) + "---")
			cuts(c, 1, most, "|..")

	print(", ".join(data.name).replace("$",""))
	dump(rows)

def main(data):
	unsuper(rows(data))

