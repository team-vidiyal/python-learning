#Assignment 2:  Create a Tuple ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
# you should reverse each string in this tuple and save it in list.
# Output = [yadonM, 'yadseuT', 'yadsendeW', 'yadsruhT','yadirF','yadrutaS','yadnuS']

weekday_tuple=('Monday','tuesday','wednesday','thursday','friday','Saturday','Sunday')
print(f"\n Tuple={weekday_tuple} ")
print(type(weekday_tuple))
#reverse tuple
reverse_list = list(weekday_tuple[::-1])
print(f" \n  list = {reverse_list}")
print(type(reverse_list))
#reverse items in list
weekday_list = []
for items in weekday_tuple :
   result = items[::-1]
   weekday_list.append(result)
print(f" \n Result : {weekday_list}")
