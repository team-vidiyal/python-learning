# # str
# #int
# #float
# # boolean
# # complex
#
# # list
# #tuple
# # set
# # dict
#
# # 3 ways to represent a string
# book = '''Ponniyin Selvan
#           Parthiban kanavu
#           '''
#
# message = "Bangalore is a garden city"
# #angalo
#
# # print(message[1:7])
# #
# # print(message [:7])
# #
# # print(message[2:])
# #
# # print(message[-3:-1])
# #
# # print(message[:-1])
# #
# # print(message[::-1])
# #
# # print(message[10])
# #
# # print(message.endswith('city'))
# #
# print(message)
# print(type(message))
# print(message.strip("Ba"))
# print(message.find("a"))
#
# # https://www.w3schools.com/python/python_ref_string.asp
# profession = 'IT'
#
# #int
#
# age = 37
#
# print(type(age))
#
# year = 2023
#
# profit = 2_323_434_454
#
# print(profit)
#
#
# # float
#
# salary = 546464.34233
#
# print(round(salary, 2))
#
# interest_rate = 7.2
#
#
# #Boolean
#
# is_hot = True
# is_cold = False
#
# # complex a+ib
# a = 7+8j
# b = 5+9j
#
#
#
#
# print(a+b)
#
#
#
#
#
#
#
#

#print ("Hello", "Francis")

# print("Hello", end = "------------")
# print("Francis")

# fav_movies_set = {'Matrix', 'Leo', 'Billa', 'Jailer', "Billa", "Jailer"}
# #no duplicate
# # not ordered
# print(fav_movies_set)

#fav_movies_list = ['Leo', 'Billa', 'Anniyan', "Jailer"]
#
# fav_movies_list1 =[['Leo', 'Billa', 'Anniyan', "Jailer"], ['Matrix', 'John', 'Fargo']]
#
# my_fav_numbers = [3, 7, 1]
#
# print(fav_movies_list1[1][1])



# fav_movies_list.append("Mari")
# fav_movies_list.append("Indian")
#
# fav_movies_list.insert(1, 'Basha')
#
# fav_movies_list.remove("Billa")

# print(fav_movies_list.index("Billa"))
#
# fav_movies_list.pop(3)
#
# print(fav_movies_list)
#
# week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# employee_details = {
#     {'name' : 'Deepa', 'state': 'SC', 'department': 'IT', 'age': 32},
#     {'name': 'Kavitha', 'state': 'MD', 'department': 'IT', 'age': 32},
#     {'name': 'Francis', 'state': 'MD', 'department': 'IT', 'age': 32},
#     {'name' : 'Jawahar', 'state': 'Va', 'department': 'IT', 'age': 37}
#
# }

deepa_details = {'name' : 'Deepa', 'state': 'SC', 'department': 'IT', 'age': 32}

# print(deepa_details['dfdf'])



#print(deepa_details.get('country', 'Country key is not part of deepa_details'))


# for loop
# while loop

# for loop 2 variant

name = "Megala"

# if name== "Megala":
#     print("you are Megala")

# for x in range (1, 100, 5):
#     print(x, end = " ")


fav_movies_list = ['Leo', 'Billa', 'Anniyan', "Jailer", "Padayappa", "Chandramukhi", "Sivaji", "Virumandi", "VTV"]
# print(fav_movies_list[0])
# print(fav_movies_list[1])
# print(fav_movies_list[2])
# print(fav_movies_list[3])
# print(fav_movies_list[4])
count = 0
# for item in fav_movies_list:
#     print(item)
#     count = count+1 #count+=1
#     if count >=3:
#         break


while count<=3:
    print(fav_movies_list[count])
    count = count + 1  # count+=1
    if count >= 3:
        break


# count = 0
# while True:
#     print("dfdf")
#     count+=1
#     if count >=10:
#         break

# fav_movies_list = ['Leo', 'Billa', " ", "    ", "Anniyan", "Jailer"]
#
# count=0
# for movie in fav_movies_list:
#     if len(movie.strip())>0:
#      print(movie)
#      count+=1
#      print("count =", count)
#
#     print("dfdfdfd ")

# sports = ["Swimming", " ","     ", "Soccer", "Cricket","Shooting", "Carrom"]
#
# for sport in sports:
#     if len(sport.strip())==0:
#         continue;
#     print(sport)


# i=1
# while i<=5:
#     print(i)
#     i+=1









