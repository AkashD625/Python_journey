#mapp - This method is used to iterate the give list based on some conditions.
def cude(x):
      return x*x
l = [2,3,6,2,4,5,6,8]
n = list(map(cude,l))  # Here , normal text will be converted to list form using the list keyword.
print(n)


#filter - This is only used to show the selected item based on the some condition
def filter_function(x):
      x>5
nel= list(filter(filter_function,l))
print(nel)


#Reduce - This is also priority function  , this should be imported from functionaltool librery
from functools import reduce
def sum(x,y):
      return x+y

nek = reduce(sum,l)
print(nek)