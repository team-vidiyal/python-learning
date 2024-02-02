# write a python function that takes two arguments(list1,list2)that returns ture if two lists when combined
# from a consecutive sequence.returns false otherwise


list1=[7,5,1,4]
list2=[2,3,6]
list3 = list(set(list1 + list2))
print(list3)
sorted_list = sorted(list3)
range_list=list(range(min(list3), max(list3)+1))
if sorted_list == range_list:
   print("True")
else:
   print("False")

# E.g-2
listA = [34,37]
listB = [35,38]
listC = list(set(listA + listB))
print(listC)
sorted_list = sorted(listC)
range_list=list(range(min(listC), max(listC)+1))
if sorted_list == range_list:
   print("Ture")
else:
   print("False")