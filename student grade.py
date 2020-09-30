print ("*"*70)
age = int(input("how old is the student"))
grade = int(input("what grade did they get"))
print("*"*70)
if grade>=80:
    if age<16:
        print("excellent")
    elif age>=16:
        print("good")
else:
    print("please try harder next time")