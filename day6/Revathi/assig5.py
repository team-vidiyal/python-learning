# get two inputs(3 digits int input)from user.find all the num divisible by 7 b/w those two numbers.print once at the end both no are inclusive
# eg:num1=104,num2=135
# output [105,112,119,126,133]


no1=int(input("enter num 1 : "))
no2=int(input("enter num 2 : "))
output = []
for i in range(no1,no2):
    if(i%7==0):
        output.append(i)

print(output)