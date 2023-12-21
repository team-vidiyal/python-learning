text = input("Enter the text: ")
times = int(input("Enter the number of times: "))

#Option 1
# text_with_space = text + " "
#
# result = text_with_space*times
# final_result = result.strip();
#
# print(final_result)

#Option 2

#rjust Country
input_text_with_space = text.rjust(len(text)+1)
result = input_text_with_space*times
final_result = result.lstrip()
print(final_result)