department = "Data Science"

def scope_function():
   global department
   department = "IT"
   print(department)

def scope_function2():
    print(department)

print(department)

scope_function()

scope_function2()