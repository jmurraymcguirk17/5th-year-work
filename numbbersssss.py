print("-"*20)
firstnum = float(input("enter a number"))
secnum = float(input("enter a second number"))
divide = secnum/firstnum
print (divide)
rem = secnum%firstnum
if (firstnum>secnum):
    print ("your first number is bigger than your second number")
else:
    print ("your first number is not bigger than your second number")
if (rem>=1):
    print ("your first number does not evenly divide into the second  number")
else:
    print ("your first number does evenly divide into your second number")
print("-"*20)