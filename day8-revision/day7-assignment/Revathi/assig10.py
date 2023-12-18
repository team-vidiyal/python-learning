#write a program to get a string input from user and print how many vowels are in the word

def vowels_count():
    str=input("Enter the word : ")
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count+1
    print("No.of vowels in the word : " , count)

vowels_count()


# user_input = input("Enter the word : ")
#
# vowels = ['a','e','i','o','u']
#
# if user_input in vowels():
#     print(f"Number of vowels in the word {user_input} is : ")