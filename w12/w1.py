import re,traceback
import re as regex
from collections import defaultdict
from collections import Counter
import random
from functools import partial

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f

def square(x):
  return x*x


@O.k
def testing_whitespace():
	long_winded_computation=(1+2
	+3+4)
	assert long_winded_computation==10

@O.k
def testing_regularexp():
	result=re.findall('x','abx') is not None 
	assert result

@O.k
def testing_integerdivision():
	assert (5//2==2)

@O.k
def testing_square():
	assert square(4)==16

@O.k
def testing_string():
	assert(len('Sanjana')==7)

@O.k
def testing_exceptionhandling():
  flag = False
  try:
    0/0
  except ZeroDivisionError:
    flag = True

  assert flag == True

@O.k
def testing_list():
	integers=[1,2,3]
	assert (len(integers)==3)

@O.k
def testing_extendinglist():
	integers=[1,2,3]
	integers.extend([4, 5, 6])
	assert(len(integers)==6)

def product(x, y):
	return (x * y)

@O.k
def testing_tupleproduct():
	assert(product(3,4)==12)

@O.k
def testing_dictionary1():
	grades = { "Sanjana" : 80, "Shruti" : 95 }
	assert("Sanjana" in grades)

@O.k
def testing_addelement():
	inventory={"pen":15,"pencil":8}
	inventory["notebook"]=10
	assert (len(inventory)==3)

@O.k
def testing_dictionaryvalue():
  words = "Foundation of Software Science".split(" ")
  wordcount = defaultdict(int)
  for w in words:
    wordcount[w]=wordcount[w]+1
  assert (wordcount["Software"]==1)

@O.k
def testing_counter():
	c = Counter([0, 1, 2, 0])
 	assert(c.get(0)==2)

@O.k
def testing_set():
	list1=[1,2,1,1,3,1]
	set1=set(list1)
	assert(len(set1)==3)

@O.k
def testing_ifelse():
	x=10
	two_digit=True if x>9 else False
	assert two_digit

@O.k
def testing_all():
  x = all([True, 1, { 3 }]) 
  assert x == True

@O.k
def testing_sorting():
	x=[4,5,1,2]
	x.sort()
	assert x[0]==1

@O.k
def testing_listcomprehensions():
	square_list = [x*x for x in range(10)]
	assert(square_list[2]==4)

def even_numbers(limit):
	n = 1
	while n%2==0:
		yield n
		n += 1
		if(n==limit):
			break

def createGenerator():
  for i in [5,10]:
    yield i*i

@O.k
def testing_generators():
  gen = createGenerator()
  sum = 0
  for i  in  gen:
    sum = sum + i  
  assert sum == 125

@O.k
def testing_random():
  x = random.randrange(5, 10)
  assert x >=5 and x <10

@O.k
def testing_searchregex():
   ans = regex.search("a", "Sanjana")
  
   assert ans is not None

def exp(base, power):
	return base ** power

@O.k
def testing_partialfn():
	two_to_the = partial(exp, 2)
	assert (two_to_the(3)==8)

def is_even(x):
	return x % 2 == 0

@O.k
def testing_filter():
	xs=[1,2,3,4]
	x_even = filter(is_even, xs)
	assert(len(x_even)==2)

@O.k
def testing_enumerate():
	documents="sanjana"
	count=0
	for i in enumerate(documents):
		count=count+1
	assert(count==7)

@O.k
def testing_zip():
	pairs = [('a', 1), ('b', 2), ('c', 3)]
	letters, numbers = zip(*pairs)
	assert(len(letters)==3)

def doubler(f):    
  def g(x):        
    return 2 * f(x)    
  return g
def f1(x):    
  return x + 1

@O.k
def testing_fnasparameter():
  g = doubler(f1) 
  a = g(-1)
  assert a == 0

@O.k
def testing_args():
	def add(x, y, z):
		return x + y + z
	x_y_list = [1, 2]
	z_dict = { "z" : 3 }
	assert (add(*x_y_list, **z_dict)==6)


if __name__== "__main__":
  O.report()