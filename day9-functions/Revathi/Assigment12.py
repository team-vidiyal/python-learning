#list=[1,2,3,4,5]
# you are given an integer list.you need to all add elements in that list except the number at index


int_list=[1,2,3,4,5]
print("The given list is :",end="")
print(int_list)

someofelement=0

output = []
for eachelement in int_list:
    output.append(sum(int_list) - eachelement)

print("Some of the element is : ", output)

