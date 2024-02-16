def sum(a, b, c):
    return a + b + c


result = sum(3, 4, 5)
print(result)

print((lambda x: [ fruit for fruit in x if len(fruit) > 5 ])([ 'banana', 'apple', 'grapes' ]))
