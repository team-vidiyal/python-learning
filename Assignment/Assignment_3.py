# Assignment day -4:

# Calculate discounted amount. Get the amount input from user. (float type)
#
# Amount <=1000, then 10% discount.
#
# 1000 < amount <=5000, then 20% discount
#
# 5000<amount <=10000, then 30% discount
#
# 10000<amount, then 40% discount.
#
# You need to print output in the below format.
#
# For e.g. if input is 5000.00
#
# Total Amount is 5000.00 dollars, discount is 1000.00 dollars, net amount is 4000.00 dollars









#program to calculate the discounted amount
######option1

Amount= float(input("Enter the Amount: "))
if Amount <= 1000:
    discount_percent = float(10 / 100)

elif Amount > 1000 and Amount <= 5000:
    discount_percent = float(20 / 100)

elif Amount > 5000 and Amount <= 10000:
    discount_percent = float(30 / 100)

else:
    discount_percent = float(40 / 100)

discount = Amount * discount_percent
net_amount = Amount - discount
print(f"Total Amount is {Amount} dollars, discount is {discount} dollars, net amount is {net_amount} dollars")

