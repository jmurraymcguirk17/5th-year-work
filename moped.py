mopedtype = input("what type of moped would you like to rent? 50cc or 250cc")
day = input("are you planning to rent the moped on a weekend or weekday")
hour = int(input("how long are you going to rent the moped for (in hours)"))
price50 = 15
hourly50 = 2.50
price250 = 25
hourly20 = 3.50
we50 = 30
we250 = 35
wehour50 = 7.50
wehour250 = 8.50
if mopedtype == "50cc":
    if day == "weekday":
        if hour <=3:
            print ("it will cost €",price50," to rent the moped for your day")
        elif hour>3:
            print ("it will cost €",price50+(hourly50*hour)," to rent a moped for the day")
    if day == "weekend":
        if hour <=3:
            print ("it will cost €",we50," to rent the moped for your day")
        elif hour>3:
            print ("it will cost €",we50+(wehour50*hour)," to rent a moped for the day")
elif mopedtype == "250cc":
    if day == "weekday":
        if hour <=3:
                print ("it will cost €",price250," to rent the moped for your day")
        elif hour>3:
                print ("it will cost €",price250+(hourly20*hour)," to rent a moped for the day")
    if day == "weekend":
        if hour <=3:
            print ("it will cost €",we250," to rent the moped for your day")
        elif hour>3:
            print ("it will cost €",we250+(wehour250*hour)," to rent a moped for the day")
else:
    print("invalid option selected")