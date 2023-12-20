#You are given an integer list. You need to all add elements in that list except the number at index.
# E.g. [1, 2, 3, 4, 5] The zx-[p899output should be [14, 13, 12, 11, 10]

user_list = [1, 2, 3, 4, 5]
added_value = 0
for item in user_list:
    added_value += item
#option 1
final_output =[]
for item in user_list:
    result = added_value - item
    final_output.append(result)
print(f"User_list = {user_list}")
print(f"The Total added value in list : {added_value}")
print(f"Option1 = {final_output}")

#option 2
output1 = [added_value-item for item in user_list]
print(f"Option2 = {output1}")