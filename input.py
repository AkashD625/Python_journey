# ****************User input in python**************

# To take the user input we use input fuction in python 
#   syntax - variable = input()
#              or       input("Text that should be printed while taking the input")


print("Welcome")
a = input("Enter the number 1 :")
b = input("Enter the number two:")
# By default the user input is considered as string , if he or she enters number fromthe keyboard that will be considered as string , we should typ cast it to the integ2er type

print("The sum of number",a,"And number",b,"is",int(a)+int(b))
print("THNKYOU")