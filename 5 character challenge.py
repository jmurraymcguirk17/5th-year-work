char = input("enter 5 random characters")
print (char[0])
print (char[1])
print (char[2])
print (char[3])
print (char[4])
print ("the ascii of your first value is", ord(char[0]))
print ("the ascii of your second value is", ord(char[1]))
print ("the ascii of your third value is", ord(char[2]))
print ("the ascii of your fourth value is", ord(char[3]))
print ("the ascii of your fifth value is", ord(char[4]))

unit = int(input("\n how many units of electricity would you like to use?"))
btax = round(unit*0.19,2)
print("it will cost €",btax,"to use ", unit,"units of electricity before a standing charge")
print("it will cost €",btax+26.2," to use ",unit,"units of electricity in total")