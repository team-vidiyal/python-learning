#Get 2 integer inputs from user(number and length)-
#   Write a program to a return multiples of number until the list length reaches the length.
#Number = 7   Length = 5  Output = [7,14,21,28,35]
#Note: Add validation, if user inputs anything other than integer, keep prompting user to enter integer only until he gives the correct input
#option1
while True:
  user_number = input("Enter a user_number : ")
  user_length = input("Enter the user_length : ")
  print(f"User_number:{user_number} \nUser_length:{user_length}")
  if user_number.isdigit() and user_length.isdigit():
    print(f"Option 1 - Output = {[num * int(user_number) for num in range(1, int(user_length) + 1)]}")
    break
  else:
    print("........Enter only integer value..........")

# #option2
# user_number = input("Enter a user_number : ")
# user_length = input("Enter the user_length : ")
# result1 = []
# intial_value=1
# if user_number.isdigit() and user_length.isdigit():
#    while len(result1) < int(user_length):
#         result1.append(intial_value*int(user_number))
#         intial_value+=1
#    print(f"Option 2 - Output = {result1}")
# else:
#        print("........Enter only integer value..........")

# #option3
# user_number = int(input("Enter a user_number : "))
# user_length = int(input("Enter the user_length : "))
# print(f"user_number:{user_number} \n user_length: {user_length}")
# #option1
# result=[]
# for num in range(1,user_length):
#     multiple=num*user_number
#     result.append(multiple)
# print(f"Option 1 - Output = {result}")


