#program to calculate simple interest

print("To Calculate Simple Interest ")
amt = float(input("Enter the principal amt: "))
#amt1 = input("Enter the principal amt: ")
#print(type(amt))
#print(type(amt1))
rate = float(input("Enter the rate: "))
year = float(input("Enter the time/year: "))
print("Principal amount :", amt)
print("Rate : ", rate)
print("year : ", year)
si = (amt * rate * year)/100
print("calculated Simple_Interest : ", si)
