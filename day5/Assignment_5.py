#####Accept a single character from user. If it's a vowel print it's a vowel, otherwise print consonant.
#####E.g.  User input:   e   Output: 'e' is a vowel

user_option = input("Enter a alphabet : ")

####option1-----------------------------
if len(user_option)>1 or not user_option.isalpha():
    print("please enter a single Alphabet only")
else:
    print(f"Option 1 \n\t User Input : {user_option}")
    if user_option == "a" or user_option =="e" or user_option == "i" or user_option == "o" or user_option == "u" :
        print(f"\t Output : '{user_option}' is vowel")
    else:
        print(f"\tOutput : '{user_option}' is consonant")

#option2----------------------------------

vowels = ["a","e","i","o","u"]
if len(user_option)>1  or not user_option.isalpha():
    print("please enter a single Alphabet only")
else:
    print(f"Option 2 \n\t User Input : {user_option}")
    if user_option in vowels:
        print(f"\t Output : '{user_option}' is vowel")
    else:
        print(f"\t Output : '{user_option}' is consonant")

#option3 ------------------------------------------+
    print(f"Option 3 \n\t User Input : {user_option}")
    if user_option in 'aeiou':
        print(f"\t Output : '{user_option}' is vowel")
    else:
        print(f"\t Output : '{user_option}' is consonant")



