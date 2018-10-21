from test import O
from super import wrapper

# Test function
@O.k
def testing():
	print("\n For weatherLong.csv")
	wrapper('weatherLong.csv')
	print ("-------------------------------------------")
	print("\n For auto.csv")
	wrapper('auto.csv')
	print ("-------------------------------------------")