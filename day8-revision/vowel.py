# while True:
#     input_text = input("Enter a word: ")
#     if not input_text.isalpha():
#         print("Please enter only alphabets.")
#         continue
#     break
#
# output = []
# for character in input_text:
#     if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#         output.append(character)
#
# print(len(output))
#
# print(len([character for character in input_text if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]))

my_list = [ 22.5, 33.5, 44.5, 66.7]

for item in my_list:
    print(item)

print("Second approach")
for number in range(len(my_list)):
    print(my_list[number])

print("While loop approach")
count = 0
while count <len(my_list):
    print(my_list[count])
    count+=1

print("enumeration approach")

for index, item in enumerate(my_list):
    print(index, item)