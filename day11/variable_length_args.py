def sum(*args):
    # print(type(args))
    sum = 0
    for number in args:
        sum += number
    return sum


output = sum(12, 20, 24, 45, 56, 343, 3434, 3434, 5454)

print(output)


def concat(*names):
    output = ""
    for name in names:
        output = output + name
    return output


print(concat("Kavitha", "Deepa", "Manimegala", "Thilipan", "Ramya", "Mekala"))


def length_of_names(*names):
    output = [ ]
    for name in names:
        output.append(len(name))
    return output


final_output = length_of_names("Kavitha", "Deepa", "Manimegala", "Thilipan", "Ramya", "Mekala", "Bhanu")

print(final_output)
