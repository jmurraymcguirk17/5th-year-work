firstname = input("Enter your first name")
surname = input ("What is your surname")
year = int(input("What year is it"))
if year > 2000:
    print(firstname,surname,year-2000)
elif year < 2000 >1900:
    print(firstname,surname,year-1900)