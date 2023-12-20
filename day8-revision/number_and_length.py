# Two inputs
# 1. Number and
# 2. length
# use case: print multiples of number for the given length
  # number = 7
  # length = 3
  # [7,14,21]

  # number 11
  # length 6
  # [11, 22, 33, 44, 55, 66]


while True:
 number = input("Enter an integer number: ")
 if number.isdigit():
    number = int(number)
    break
 print("Only Integer numbers are allowed. Please enter integer only..")

while True:
 length = input("Enter your second integer number: ")
 if length.isdigit():
    length = int(length)
    break
 print("Only Integer numbers are allowed. Please enter integer only..")

counter = 1
output = []
while counter <=length:
    output.append(number*counter)
    counter+=1
# for item in range(1, length+1):
#     output.append(item*number)


print(output)







