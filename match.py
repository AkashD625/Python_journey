# Match case statement is same as switch case i c programimng.
# sysntax - 
# match x:
#  case 0:
#   print("Hello")
#  case 1:
#   print("hello2")
#  case _:
#   #default case
#there may be maany defaoult in python we can run single using the if else statements

a = int(input("Enter the value of a :"))
match a:
      case 1:
            print("Thank you entered :"+a)
      case 2:
            print("Thankyou entered :",a)
      case _: 
              if(a>3):
                print("So you entered : ",a)
      