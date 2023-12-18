#get two int inputs from user
# number  length
# write a program to a return multiples of number until the list length reaches the length


Number = int(input("Enter the Number : "))
Length = int(input("Enter the Length : "))
output  = []
for i in range (Length):
    output.append((i+1)*Number)
print("Output : ",output)

