# assignments
import sys

word = input("Enter a word to print : ")
n_times=int(input("Enter the number: "))
underline= "-"

if n_times>=1:
   print(f"Word Entered : {word}, to print {n_times} times repetitively")
   print(underline * 50)
else:
   print("Please enter a valid number to print.")
   sys.exit(1)

#option 1
print(word * n_times)
result_with_space = (word + " ") * n_times
final_result=result_with_space.rstrip()
print(result_with_space)
print(final_result)

#option2
option2_add_space=word.rjust(len(word)+1)
option2_result=option2_add_space * n_times
print(option2_result.strip())

#option3
print(word, end=" ")
