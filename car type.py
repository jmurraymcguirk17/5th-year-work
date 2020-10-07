currentyear = 2020
caryear = int(input("what year was your car made?"))
cartype = input("is your car petrol, diesel, electric or other (if other please specify)?")
carage = currentyear-caryear
if carage>=10 or cartype == "petrol":
    print ("your car is a high pollution car")
else:
    print ("your car is a low pollution car")