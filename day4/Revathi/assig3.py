def GetDiscountedAmount(pA, percent):
    discountedAmount = pA * (percent / 100)
    netamount = pA-discountedAmount
    print(f"Purchase Amount: {pA}, Discounted Amount:  {discountedAmount} , Net Amount: {netamount}")
    return  discountedAmount

purchaseAmount = float(input("Total amount is :"))
if purchaseAmount <= 1000:
     discountedAmount = GetDiscountedAmount(purchaseAmount, 10)
elif purchaseAmount > 1000 and purchaseAmount <= 5000:
    discountedAmount = GetDiscountedAmount(purchaseAmount, 20)
elif purchaseAmount > 5000 and purchaseAmount <= 10000:
    discountedAmount = GetDiscountedAmount(purchaseAmount, 30)
elif purchaseAmount < 10000:
    discountedAmount = GetDiscountedAmount(purchaseAmount, 40)
else:
    print("invalid input")



# Another method

def calculatediscount(amount, price):
    discount = amount * (price /100)
    balance = amount - discount
    print(f"amount is : {amount} , discount is :  {discount} , balance amount is :  {balance}")
    return discount

t_amount = float(input("purchase amount is : "))
if t_amount <=1000 :
    discount = calculatediscount(t_amount ,10)
elif t_amount > 1000 and t_amount <= 5000:
    discount = calculatediscount(t_amount, 20)
elif t_amount > 5000 and t_amount <= 10000:
    discount = calculatediscount(t_amount, 30)
elif t_amount < 10000 :
    discount = calculatediscount(t_amount, 40)
else:
    print("invalid input")