print("*"*100)
print("Murray Airlines")
print("*"*100)
membertype = int(input("What is being added,\nPress 1) for Passenger.\nPress 2) for Crew Member.\nPress 3) for a Piece of Cargo.\nSelect: "))#asks the user to select what type of crew member they are
print("*"*100)
#stores values of maximum average hours a certain job title can work
maxhrspilot = 8
maxhrscopilot = 10
maxhrsstew = 12
#stores the current year
currentyear = 2020

if membertype == 3:
    #asks for details about the cargo
    cargodetails = input("Please enter details about your cargo (colour, size, etc.)")
    #asks user about cargo weight
    cargoweight = int(input("How much does the cargo weigh (in kilograms)?"))
    #prints a receipt of information about the cargo
    if cargoweight <=15:
        print("You have successfully logged your piece of cargo")
        print("Successful, here is your receipt")
        print("*"*100)
        print("RECEIPT\nDetails: ",cargodetails,"\nWeight: ",cargoweight)
        print("*"*100)
    else:
        print("Weight must be under 15 kg, please try again")
elif membertype == 2:
    crewtype = int(input("What type of crew member are you?\nPress 1) for Pilot.\nPress 2) for Co-Pilot.\nPress 3) for Steward."))#gives user options of crew members to select
    hrswrkd1 = int(input("How many hours did you work 2 days ago?"))#asks user how many hours they worked 2 days ago
    hrswrkd2 = int(input("How many hours did you work yesterday?"))#asks user how many hours they worked yesterday
    flightlen = int(input("How long will this flight be?"))
    #adds up the total hours worked over the past 2 days
    totalhrswrkd = hrswrkd1+hrswrkd2
    #calculates the average hours worked over the past 2 days
    averagehrs = totalhrswrkd/2
    #calculates the total average hours IF the worker boards the flight
    totalavhrs = (totalhrswrkd+flightlen)/3
    if averagehrs>maxhrspilot and crewtype == 1:
        print("Maximum average hours worked over the past 2 days must be 8 hours.")#tells the user that the maximum average hours must be 8 hours
    elif averagehrs>maxhrscopilot and crewtype == 2:
        print("Maximum average hours worked over the past 2 days must be 10 hours.")
    elif averagehrs>maxhrsstew and crewtype == 3:
        print("Maximum average hours worked over the past 2 days must be 12 hours.")
    elif averagehrs<=maxhrspilot and crewtype == 1:
        print("Your average hours worked currently is",averagehrs)
        if totalavhrs>maxhrspilot:
            print("you cannot board this flight as your total hours worked will be too long after this.",round(totalavhrs,1),"hours")#tells the user that if they board the flight, they will go over the maximum average hours to work
        else:
            print("You can board this flight, your total hours worked after this flight will be",totalhrswrkd+flightlen)#tells the user they can board the flight as they will not exceed the maximum average working hours
    elif averagehrs<=maxhrscopilot and crewtype == 2:
        print("Your average hours worked currently is",averagehrs)
        if totalavhrs>maxhrscopilot:
            print("you cannot board this flight as your total hours worked will be too long after this.",round(totalavhrs,1),"hours")
        else:
            print("You can board this flight, your total hours worked after this flight will be",totalhrswrkd+flightlen)
    elif averagehrs<=maxhrsstew and crewtype == 3:
        print("Your average hours worked currently is",averagehrs)
        if totalavhrs>maxhrspilot:
            print("you cannot board this flight as your total hours worked will be too long after this.",round(totalavhrs,1),"hours")
        else:
            print("You can board this flight, your total hours worked after this flight will be",totalhrswrkd+flightlen)
elif membertype == 1:
    name = input("What is your name?")
    yearborn = int(input("What year were you born in?"))#asks the user what year they were born in
    age = currentyear-yearborn
    if age<18:
        print("You must be an adult to book a flight.")#tells user that they must be an adult to board the flight
        print("*"*100)
    else:
        childrenboard = int(input("How many children are you boarding with? (If none press 0)"))
        print("*"*100)
        print("Name: ",name,"\nAge: ",age,"\nNo. of Children: ",childrenboard)#prints a receipt of information to the user for their boarding
        print("*"*100)
else:
    print("Invalid Option selected, please try again.")#tells the user that they picked an option that wasnt available to be selected