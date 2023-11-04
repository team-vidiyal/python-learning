#program to calculate simple Interest

principle = float(input("Enter the principle amount : "))
rate = float(input("Enter the interest rate : " ))
duration = float(input("Enter the duration in years for the FD : "))

# Formula for simple interest is SI = PNR/100
SI = principle * duration * rate / 100

print("Simple Interest is : ", SI)
