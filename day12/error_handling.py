# import math
# my_list = [25, 36, 78, "Hello", 100, 99, 45]
#
# for item in my_list:
#  try:
#
#         result = math.sqrt(item)
#         print(result)
#  except Exception:
#     print(f"{item} is not a number" )


try:
 new_list = [12, 34, 56]
 print(new_list[10])
except IndexError:
    print("This index is out of range")


print("Hello")



