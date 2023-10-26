# Assignment
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
print((word + " ") * n_times)
#print((word * n_times), end= " ")



#option2
result=(word + " ") * n_times
result1=(word * n_times)
print(result)
print(result1, end=" ")
