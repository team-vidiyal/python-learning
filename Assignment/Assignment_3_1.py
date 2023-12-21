###option2
Amount= float(input("Enter the Amount: "))
match Amount:
    case _ if Amount <= 1000:
        discount_percent = float(10/100)
    case _ if Amount > 1000 and Amount <= 5000:
        discount_percent = float(20 / 100)
    case _ if Amount > 5000 and Amount <= 10000:
        discount_percent = float(20 / 100)
    case _:
        discount_percent = float(40 / 100)

discount = float(Amount * discount_percent )
net_amount = Amount - discount
print(f"Total Amount is {Amount} dollars, discount is {discount} dollars, net amount is {net_amount} dollars")


