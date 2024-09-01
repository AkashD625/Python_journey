# Local variable - These are the variables that is going to store the valuess in only , whrer the is being used.
# Global variable are those where the decleared variable can be used in the entire programe.

# -------------------We can use the gloably decleared variables and functions in any function which is considered as local and be able to modify the globle variable.

x=5
print(f"Globle:{x}")
def localfunction():
      global x  #this will include global varible and it is editeble.   (Keyword=globle)
      x=10
      print(f"Local:{x}")
y=8
print(y)#Tthis is globaly decleared and used globaly.NO error found
print(x)
localfunction()