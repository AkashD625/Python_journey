# a = input("Enter the number for table : ")
# try:
#   i = 1
#   for i in range(11):
#         print(f"{a} X {i}={int(a)*i}")
# except :
#     print("Invalid input")        

# n = input("Enter the number: ")
# a = [2,3]
# try:
#  print(f"{a[n]}")
# except IndexError: 
#       print("Invalid input")  


#Finaly  =  This key word will run any how , irrespectivie of the condications
# try:
#  finally:
#   print("This will run any how")    
# except:
#   print("Invalid input")




#--------------------------Custom error---------------
a = int(input("Enter the number"))
if(a<10 or a>20):
      raise ValueError("Value must btw 10 and 20")  #custom error
else:
      print(f"You entered : {a}")

#ther are more custom error class in python goto python docs for that.      