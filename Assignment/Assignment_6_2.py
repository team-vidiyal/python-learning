# Given a dictionary {2:12, 3:15, 5:20, 7:24},Write a program to create a list with sum of key value pairs.Output:[14, 18, 25, 31]

dict = {2:12, 3:15, 5:20, 7:24}
print(dict[2])

print(f"Dictionary : {dict}\n")
result=[]
# for key,value  in dict.items():
#     print(f"Keys: {key} and Value: {value} = Result :{key + value}")
#     result.append(key + value)
for key in dict.keys():
    result.append(key + dict[key])

print(f"Result: {result}")
