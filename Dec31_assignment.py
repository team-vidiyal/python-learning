# Get sentence alphanumeric sentence from the user and print the alpha&numbers counts separately n dictionary format
from typing import Dict, Any

#Get user input
user_input= input("Enter an alphanumeric sentence:")

print(f"user entered Sentence is:{user_input}")


# dictionaries for digit and alpha counts
digit_count = {}
alpha_count = {}
# for separate letters and numbers count
for char in user_input:
    if char.isdigit():
            digit_count[char] = digit_count.get(char, 0) + 1
    elif char.isalpha():
            alpha_count[char] = alpha_count.get(char, 0) + 1
print("Alphabetic Character Counts:", alpha_count)
print("Digit Counts:", digit_count)

digit_count = 0
alpha_count = 0

# for total letters and numbers count
for char in user_input:
    if char.isdigit():
            digit_count +=1
    elif char.isalpha():
            alpha_count+=1
print("Alphabetic Character Counts:", alpha_count)
print("Digit Counts:", digit_count)