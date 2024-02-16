def emp_id_with_names(**kwargs):
    sum = 0
    for salary in kwargs.values():
        sum += salary
    return sum


# def emp_id_with_names(kavitha, deepa, manimegala, ramya):
#     pass

print(emp_id_with_names(kavitha=1000, deepa=2000, manimegala=3000, ramya=5000, bhanu=200, kathir=7000))

total_salary = emp_id_with_names(kavitha =1000, deepa = 2500, manimegala = 3000, Ramya = 5000)

print(total_salary)
