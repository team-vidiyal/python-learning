programming_language = input("Enter your programming language: ")
years_of_experience = int(input("Enter your years of experience: "))

# if programming_language == "Java":
#     print("You are a Java programmer")
# elif programming_language == "Python":
#     print("You are a Python programmer")
# elif programming_language == "PHP":
#     print("You are a PHP programmer")
# else:
#     print("You are a programmer")


#Java programmer with 10 years experience
match programming_language:
    case "Java":
        print("You are a Java Programmer")
        if years_of_experience >= 10:
            print("You are a java expert")
    case "Python":
        print("You are a Python programmer")
    case "PHP":
        print("You are a PHP programmer")
    case _:
        print("You are programmer")