# Scope

# this has global scope
department = "Data Science"

def scope_function():
    #language local scope
    language = "Python"
    print(language)

def scope_function2():
    department = "IT"
    language = "Java"
    print(language)



print(department)

scope_function()

scope_function2()


