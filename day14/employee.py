# class is blue print of a object

{'name': 'Deepa', 'pay': 3434}
{'name': 'Kavitha', 'pay': 1234}
{'name': 'Francis', 'pay': 3423}
[ 0, 1, 2 ]


class Employee:
    # first_name
    # last_name
    # pay
    # department
    def __init__(self, first_name, last_name, pay, department):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.department = department


emp1 = Employee('Deepa', 'Prakash', 30000, 'IT')
print(emp1.first_name)

emp2 = Employee('Kavitha', 'Loganathan', 50000, 'IT')
print(emp2.first_name)


# Class, Object, instance (emp1, emp2)