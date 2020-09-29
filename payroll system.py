'''rate = float(input("How much are you paid per hour"))
hours = int(input("How many hours do you work per week?"))
print ("You should be paid €",round(rate*hours,2))'''
hour = int(input("How many hours do you work per week?"))
basewage = 5
overtime = 10
othour = hour-39
otpay = othour*overtime
bwagecap = 39
ypayot = (bwagecap*basewage)+otpay
ypay = hour*basewage
tax = ypay
yearlypayot = ypayot*52
yearlypay = ypay*52
lowtax = yearlypay*0.01
tax3 = yearlypay*0.03
tax55 = yearlypay*0.055
lowtaxb = yearlypayot*0.01
tax3b = yearlypayot*0.03
tax55b = yearlypayot*0.055
taxb8 = yearlypayot*0.08
if hour<30:
    print ("you should be paid €",hour*basewage,"per week")
    print ("your yearly pay is €",yearlypay)
    if yearlypay <= 12012:
        print("your yearly tax is", lowtax)
    elif yearlypay 12011< 18667:
        print("your yearly tax is", tax3)
else:
    print ("you should be paid €",(bwagecap*basewage)+otpay,"per week")
    print ("your yearly pay is €", yearlypayot)