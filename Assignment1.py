#Get principal amount, rate of interest and duration (time) as inputs from user
#Write a program to calculate simple interest (formula: SI = P × R × T)
#Here, the rate is given in percentage (r%) is written as r/100

SI = 0
principle =float(input("Please enter principle amount:"))
rate = float(input("Please enter rate of interest value:"))
time = int(input("Please enter time duration:"))

if SI<=0:
    SI = (principle*time*rate)/100
    print('Simple Interest is :',SI)
    print(type(SI))