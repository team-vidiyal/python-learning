#sports = [" ", "                 ", " ","Swimming","Soccer", "Cricket","Shooting"]

sports_1 = ["Swimming","Soccer", "Cricket","Shooting", "Carrom"]
# game = "    Football   ";
# print(game.strip())
#break- break out of the loop
#continue - continue with next iteration, (ignore all the statements after continue)
# for sport in sports:
#     if len(sport.strip())==0:
#         break
#     print(sport)
#
# for sport in sports:
#     if len(sport.strip())==0:
#         continue;
#     print(sport)

# for sport in sports:
#     if len(sport.strip())>1:
#         print(sport)
#         break

# for item in sports_1:
#     if item.startswith("S"):
#         print(item)


numbers = [1, 2, 3, 4, 5]
squared = [number**2 for number in numbers]
print(squared)


#newlist = [expression for item in iterable if condition == True]

# result = []
# for number in numbers:
#     result.append(number**2)
# print(result)

# #list comprehension
# # [output forloop ifcondition]
# #result = [item for item in sports_1 if item.startswith("S")]
#
# result = [item for item in sports_1 if len(item)<=6]
# print(result)












