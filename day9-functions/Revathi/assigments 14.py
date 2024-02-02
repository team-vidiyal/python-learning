# write a python function that takes a sentence as a parameter.the function should return longest even lengh word.
# if no even lengh word in a given sentence the function should return "00"
# e.g:
# she sells seashells by the seashore

def printWords(s):
    s = s.split(' ')
    for word in s:
        if len(word) % 2 == 0:
            print(word)
        else:
            print("00")

s = "she sells seashells by the seashore"
printWords(s)