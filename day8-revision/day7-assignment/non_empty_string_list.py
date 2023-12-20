user_input = int(input("Enter a number: "))
sports = ["  ", " ", " ", "Tennis","Cricket", "Foot ball", "Carom", "Swimming"]



#len(sport.strip())>0)
#

# new_list = []
# for item in sports:
#     if len(item.strip())>0:
#         new_list.append(item)
#
# print(new_list[user_input])


new_list = [item for item in sports if len(item.strip())>0]
print(new_list[user_input])



# # [output_expression for loop if condition (optianal)]

#Method 1
# output_list = []
# for sport in sports:
#     if len(sport.strip()>0):
#         output_list.append(sport)
#
# print(output_list[user_input])



# #Method 2:
# output = [sport for sport in sports if len(sport.strip())>0]
# print(output[user_input])