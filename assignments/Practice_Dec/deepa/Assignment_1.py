##Write a program that accepts a sentence from user that may contain letters and digits. The output should be a dictionary as shown in the example below.

user_input = input("Enter a Sentence : ")
print(f"Sentence :{user_input}")
letters=0
digits=0
for str in user_input:
   if str.isalpha():
      letters+= 1
      continue
   else:
       if str.isdigit():
           digits+=1
           continue

print(f"Letters: {letters}")
print(f"Digits : {digits}")