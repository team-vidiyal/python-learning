#Calculate the discounted amount

Total_amount = float(input("Enter the amount: "))
if float(Total_amount) <= 1000:
    print("Total amount is",Total_amount,";", "10% Discount Amount is", float(Total_amount * .10), ";", "Net amount is",float(Total_amount * .90))
elif float(Total_amount) <= 5000:
    print("Total amount is",Total_amount,";", "20% Discount Amount is", float(Total_amount * .20), ";", "Net amount is",float(Total_amount * .80))
elif float(Total_amount) <= 10000:
    print("Total amount is",Total_amount,";", "30% Discount Amount is", float(Total_amount * .30), ";", "Net amount is",float(Total_amount * .70))
