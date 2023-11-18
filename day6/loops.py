# for loop
  # - range
  # -collection

#use case -> print numbers between 1 to 100.

# for number in range(31, 50, 2): # start value (optional, default 0 if not provided), end value (not included, only till previous value is considered), step (optional, default 1 if not provided)
#     print(number)

wild_animals = ["Tiger", "Cheetah" ,"Zebra", "elephant", "shark", 2.0] #List is mutable

for animal in wild_animals:
    if animal.startswith('C'):
        print(animal)



# for number in range(len(wild_animals)):
#     print(number, wild_animals[number])


# while loop