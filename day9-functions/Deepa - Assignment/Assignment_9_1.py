#Create a function that accepts two string parameters  's' and 't',  return True if 's' is anagram of 't' and false otherwise
#Note:  Anagram is a word formed by rearranging the letters of another, such as cinema, formed from iceman.
#E.g. for anagrams 1. cinema, iceman 2. heart, earth 3. listen, silent


word1=input("Enter the first anagram  word : ")
word2=input("Enter the second anagram word : ")
#option1
def anagram(input1, input2):

    if (sorted(input1) == sorted(input2)):
        print(" Option 1: Its anagram")
    else:
        print("Option 1 :Not an anagram")
#result
anagram(word1,word2)

#option2
def check_anagram(list_word1,list_word2):
    list_word1 = [items for items in word1]
    list_word2 = [items for items in word2]
    list_word1.sort()
    list_word2.sort()
    #if (sorted(list_word1) == sorted(list_word2)):
    if(list_word1 == list_word2):
        print("Option 2 : Its anagram")
    else:
        print("Option 2 : Not an anagram")
#result
check_anagram(word1,word2)




