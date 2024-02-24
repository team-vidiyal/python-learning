#Write a python function that takes two arguments (list1, list2) that returns true if two lists when combined form a consecutive sequence. Returns False otherwise
# E.g. list1 = [7,5,1,4] and list2= [2,3,6] return True.  because when combined 1,2,3,4,5,6,7 forms a sequence..
#E.g. 2 list1=[34,37] and list2=[35,38] returns False .Since combined 34, 35, 37, 38 doesn't form sequence as 36 is missing#



list1 = [7,5,1,4]
list2 = [2,3,6]
list3 = list1 + list2
list3.sort()
print(list3)

def check_sequence (list3):

 for i in range(1,len(list3)):
        if list3[i] - list3[i - 1] != 1:
         return False
        #print("Non sequence number ")

 return True
 #print("sequence numbers ")

result = check_sequence(list3)
print(result)

