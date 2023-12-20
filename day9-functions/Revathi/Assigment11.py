#create a function that accepts two string parameters "s" &"t" return true if "s" is anagram of "t" and false otherwise


def string_parameters(s,t):

    if (sorted(s) == sorted(t)):  #sorted is shorting into assending order
        return True
    else:
        return False

s = "listen"
t = "silent"
print(sorted(s))
print(sorted(t))
print(string_parameters(s,t))

#print("The strings are anagrams.")
#print("The strings aren't anagrams.")