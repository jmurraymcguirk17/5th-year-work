price = 57.23
golddis = 0.035
hundreddis = 0.10
quarterdis = 0.05
numitems = int(input("how many products did you buy"))
gold = input("are you a gold member Y/N?")
priceb4tax = numitems*price
golddiscount = priceb4tax*golddis
goldmem = gold.upper()
if goldmem == "Y":
    if numitems<25:
        print("your total cost is €", round(priceb4tax-(priceb4tax*golddis),2),",gold discount only")
    elif numitems>=25:
        if numitems<100:
            print("your total cost is €", round(priceb4tax-(priceb4tax*golddis)-(priceb4tax*quarterdis),2),",gold and 25 products discount")
        else:
            print ("your total cost is €", round(priceb4tax-(priceb4tax*golddis)-(priceb4tax*hundreddis),2), ",discount for spending 100 or more euros and being a gold member")
else:
    if numitems<25:
        print("your total cost is €", round(priceb4tax,2),", no discount added")
    elif numitems>=25:
        if numitems<100:
            print("your total cost is €", round(priceb4tax-(priceb4tax*quarterdis),2),", 25 products discount")
        else:
            print ("your total cost is €", round((priceb4tax)-(priceb4tax*hundreddis),2), ", discount for spending €100 or more")