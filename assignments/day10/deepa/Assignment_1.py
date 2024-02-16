# Write a function that takes a string. It should return a list of two-paired characters. If the string has odd number of characters, add a star * to the last pair.
# Input ->  "Kavitha"  , Output-> ["Ka", "vi", "th", "a*"]

user_input = input('Enter any string : ')
print(user_input)
result= []
for i in range(0,len(user_input),2):
    result2 = user_input[i:i+2]
    result.append(result2)
print(result)

for i in result:
     if len(i)!=2:
         result.remove(i)
         val=f"{i}*"
         result.append(val)
print(result)



#result5 = [user_input[i:i+2] for i in range(0,len(user_input),2)]
#print(result5)