total_rate=  float(input("Enter the total rate"))

print("The total rate of the goods purchased:",total_rate)

if total_rate<=1000:
    print("10% percent discount applied")
    discounted_amount=float(total_rate*0.1)
    print("Discounted Amount is:", discounted_amount)
    Final_rate=total_rate-discounted_amount
    print("The final rate after discount is",Final_rate)

elif 1000 < total_rate <= 5000:
    print("20% percent discount applied")
    discounted_amount = float(total_rate * 0.2)
    print("Discounted Amount is:", discounted_amount)
    Final_rate = total_rate - discounted_amount
    print("The final rate after discount is", Final_rate)

elif 5000 < total_rate <= 10000:
    print("30% percent discount applied")
    discounted_amount = float(total_rate * 0.3)
    print("Discounted Amount is:", discounted_amount)
    Final_rate = total_rate - discounted_amount
    print("The final rate after discount is", Final_rate)

elif 10000 < total_rate:
    print("40%percent discount")
    discounted_amount = float(total_rate * 0.4)
    print("Discounted Amount is:", discounted_amount)
    Final_rate = total_rate - discounted_amount
    print("The final rate after discount is", Final_rate)
else:
    print("Enter some value to calculate discount")


