#create a function that accepts two string parameters "s" &"t" return true if "s" is anagram of "t" and false otherwise


def string_parameters(s1,s2):

    if (sorted(s1) == sorted(s2)):  #sorted is shorting into assending order
        return True
    else:
        return False

s1 = "heart"
s2 = "earth"
print(sorted(s1))
print(sorted(s2))
print(string_parameters(s1,s2))

#print("The strings are anagrams.")
#print("The strings aren't anagrams.")