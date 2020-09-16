'''pi = 3.14
x = float(4)
y = float(3)
radius = float(input("What would you like the radius to be?"))

print(4/3*pi*radius**3)
#print(4/3*3.14*7**3)'''

'''pi = 3.14
x = float(4)
y = float(3)
radius = float(input("What would you like the radius to be?"))
height = float(input("What would you like the height to be?"))
answer = (pi*radius**2*height/3)
#print ((round)answer)
print(pi*radius**2*height/3)
#print(4/3*3.14*7**3)'''
dec1 = 6.9
dec2 = 4.2
print ("average is",(dec1+dec2)/2)
print ("remainder is",(dec1//dec2))
print ("\n6.9 to the power of 4.2 is",dec1**dec2)
print ("87 degrees in fahrenheit is", (5/9)*(87-32))
singapore = 6962*1.60935
print ("\nmy school is 6962 miles from Singapore, this is",singapore,"km")
print("it would cost €",round(singapore*900,2),"euros to travel to singapore")

radius = float(input("n\What would you like the radius to be?"))
height = float(input("What would you like the height to be?"))
pi = 3.14
volume = pi*radius**2*height
print("Your cylinder's volume is", volume)
totalLiquid = float(input("Input a value greater than the volume of the cylinder"))
if totalLiquid<=volume:
    print("Liquid must be greater than volume")
else:
    print(totalLiquid/volume)
    
moonweight = float(input("Input your weight in kg"))
print(moonweight*0.165)