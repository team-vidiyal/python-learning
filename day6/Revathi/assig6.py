#given a dictionary{2:12,3:15,5:20,7:24}
# write a program to create a list with sum of key value pairs
# output:[14,18,25,31]


dict={2:12,3:15,5:20,7:24}
print(f"current dict is : {dict}")
result=[]
for key,value in dict.items():
    print(f"keys: {key} and value:{value} = Result : {key + value}")
    result.append(key + value)

print(f"Result : {result}")