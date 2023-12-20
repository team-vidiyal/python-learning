#Write a program to get a string input from user and print how many vowels are in the word.
#E.g. Celebration Output: Number of vowels in the word Celebration is 5
#option1
user_input=input("Enter a String : ")
print(f" User_input : {user_input}")
total_vowels=0
for str in user_input:
   if str in 'AEIOUaeiou':
      total_vowels += 1
      continue
print(f" Option 1 - Number of Vowels : {total_vowels}")

#option2
result=[str for str in user_input if str in 'AEIOUaeiou']
print(f" Option 2 - Total_vowels : {len(result)}")