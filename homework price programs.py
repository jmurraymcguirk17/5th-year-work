cost = float(input("how much does the item cost?"))
quote = 499<cost<10001
tender = cost>10000
if quote:
    print("you must get a quote as your item is between 500 and 10000 euro")
elif tender:
    print("you must go to a tender as it costs more than 10000 euros")
else:
    print("you can now confirm your order")
    
option = input("\nplease choose option A, B or C")
option1 = option.upper()
if option1 == ("A"):
    print ("you have won a ticket to Dundrum")
elif option == ("B"):
    print ("you have won the best prize, a trip to Tallaght")
elif option == ("C"):
    print ("you can go to Broombridge")
else:
    print ("invalid character entered")
    
grade = int(input("enter your percentage on your computer science lc exam"))
h1 = 90<=grade<=100
h2 = 80<=grade<=89
h3 = 70<=grade<=79
h4 = 60<=grade<=69
h5 = 50<=grade<=59
h6 = 40<=grade<=49
h7 = 30<=grade<=39
h8 = 0<=grade<=29
if h1:
    print ("you will get a h1")
elif h2:
    print ("you will get a h2")
elif h3:
    print ("you will get a h3")
elif h4:
    print ("you will get a h4")
elif h5:
    print ("you will get a h5")
elif h6:
    print ("you will get a h6")
elif h7:
    print ("you will get a h7")
elif h8:
    print ("you will get a h8")
else:
    print("you have not entered a valid percentage in numbers")