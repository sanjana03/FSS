from test import O
from dom import mainDom
from super import wrapper
import re, sys, random, math

# Test function
@O.k
def testing():
	print("\n For weatherLong.csv")
	wrapper('weatherLong.csv')
	print ("-------------------------------------------")
	print("\n For auto.csv")
	wrapper('auto.csv')
	print ("-------------------------------------------")