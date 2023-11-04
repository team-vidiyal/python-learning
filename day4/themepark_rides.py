# 55 inch and above -> High thrill rides
# 48 inch and below -> medium thrill rides
# 40 inch and below -> Mild thrill rides
# 24 inch and below -> Kids rides

# height 55 and above plus age >=60, you are allowed to get 10% discount in your ticket rate.
height = int(input("Enter your height: "))
age = int(input("Enter your age: "))

if height >= 55 or age >= 60:
    print("You are eligible for high thrill rides")
    print("You are eligible for 10% discount on ticket rates")

elif height >= 48:
    print("You are eligible for medium thrill rides")
elif height >= 40:
    print("You are eligible for mild thrill rides")
else:
    print("You are allowed to do kids rides")
