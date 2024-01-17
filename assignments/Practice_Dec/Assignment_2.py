
#Write a python function that takes a sentence as a parameter. The function should return longest even length word. If no even length word in a given sentence the function should return "00".
#She sells seashells by the seashore. We have two even length words 'by' and 'seashore . seashore is the longest even length word.

user_input=input("Enter the sentence :")
print(user_input)

long_word=""
word_length = 0
for each_word in user_input.split():
    if len(each_word) % 2 == 0 and len(each_word) > word_length:
         long_word = each_word
         word_length = len(long_word)

if len(long_word) > 0 :
    print(long_word)
else:
    print("No even length word : 00")

#result=[]
#for i in user_input.split():
#    res = len(i)
#   result.append(res)
#print(result)
#even_list=[]
