# import random
# print("Enter letter= ")
# vowels=["a","e","i","o","u"]
# random_value=random.randint(0,4)
# print(random_value)
# print(vowels[random_value])


user_input=input("Enter a alphabet : ")

vowels = ['a','e','i','o','u']

if user_input in vowels:
 print(f"{user_input} is a vowels")
else:
 print(f"{user_input} is not a vowels")