# def my_function():
#     print("Hello")
#
# my_function()
#
#
def greetings(first_name, last_name):
    #print("Hello", first_name, last_name)
     print(f"Hello {first_name} {last_name}")

greetings("Ramya", "Shantha")

#1. Function that performs a specific task, and doesn't return anything
# 2. Function that performs a task and return a value.


# list of numbers, my function should return only the even numbers
#docstring
def find_even_numbers(my_numbers):
   ''''
    This function accepts a list and returns a list which contains only even numbers
   :param my_numbers:
   :return:
   '''
   even_number_list = []
   for number in my_numbers:
        if number %2 == 0:
            even_number_list.append(number)
   return even_number_list






my_numbers = [2, 5, 7, 9, 14, 10, 13, 15, 19, 24, 30]

even_numbers = find_even_numbers(my_numbers)

print(even_numbers)