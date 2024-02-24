with open ("./deepa/my_file.txt", "r") as file:
    content = file.readlines()

print(content)


    # Absloute path C:/users/deepa/.....
    # Relative path, relative to your current file
try:
 with open("../day10/deepa_practice_file1", "r") as my_file:
    print(content)

    new_content = my_file.readlines()
    content = my_file.readlines()

    print(new_content)
except ArithmeticError:
    print("File not available in given path")



# def my_function():
#     course = "python"
#
# print(course)


name = "Mani"


name = "Raja"

print(name)