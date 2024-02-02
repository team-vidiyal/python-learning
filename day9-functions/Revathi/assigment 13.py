# write a program that accepts a sentence from user that may contain letters and digits.
# the output should be a dictionary as shown in the example below
# HelloWorld123


def digi_let():
    word=input("Enter the word : ")
    count = 0
    numbers = 0
    for user_input in word:
        if user_input.isalpha():
            count = count+1
        else:
            numbers = numbers + 1
    print("No.of letters : " , count)
    print("no.of digits : ",numbers)
digi_let()



# str = input("enter the string : ")
# countl = 0
# countn = 0
# for i in str:
#     if i.isalpha():
#         countl = countl + 1
#     else:
#         countn = countn + 1
# print("The number of letters : ", countl)
# print("The number of Digits : ", countn)
