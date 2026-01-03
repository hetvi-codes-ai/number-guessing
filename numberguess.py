#number guessing program 
import random
cn=random.randrange(1,101)
ui=int(input("enter your number:-"))
if(cn>ui):
    print("computer number is",cn)
    print("your number is low")
elif(ui>cn):
    print("computer number is",cn)
    print("your number is high")
else:
    print("computer number is",cn)
    print("your number is equal")
