# Assignment 6 -----
# get 2 values from user(3digit) check if the values between the 2 entered value is divisible by 7

import sys

value1=int((input("Enter a value with length 3 digit: ")))
value2=int((input("Enter a value with length 3 digit: ")))

if len(str(value1)) == 3 and len(str(value2)) == 3 :
    print(f"User Input \n\t value 1 = {value1} \n\t value 2 ={value2}")
    result = []
    for number in range(value1, value2+1):
        if (number % 7) == 0:
            result.append(number)
    print(f" Numbers divisible by 7 between {value1} and {value2} = {result}")
else:
    print("*****Enter the values  with 3 digit***********")
    sys.exit()



