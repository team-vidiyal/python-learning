try :
 with open("C:/Deepa/file3.txt", "r") as my_python:
    content = my_python.readlines()
    print(content)
 new_content = []
 for each_line in content:
    new_content.append(each_line.replace("Python" , "Java"))


 with open("C:/Deepa/file2.txt", "w") as my_python:
    my_python.writelines(new_content)

except FileNotFoundError:
    print('The file could not be found.')




