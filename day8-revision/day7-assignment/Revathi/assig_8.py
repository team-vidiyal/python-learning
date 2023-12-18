
week_days = ["Monday" ,"Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


print("The original list is :" +str(week_days))
result= [i[::-1] for i in week_days]
print("The reversed string list is : " +str(result))

# week_days=[tuple(reversed(t)) for t in week_days]