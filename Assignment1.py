#Get principal amount, rate of interest and duration (time) as inputs from user
#Write a program to calculate simple interest (formula: SI = P × R × T)
#Here, the rate is given in percentage (r%) is written as r/100

SI = 0
principle =int(input("Please enter principle value:"))
rate = float(input("Please enter rate value:"))
time = int(input("Please enter time value:"))

if SI<=0:
    SI = principle*(rate/100)*time
    print(SI)
    print(type(SI))