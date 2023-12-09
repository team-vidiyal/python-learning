#Given this list # sports = [" ", "                 ", " ","Swimming","Soccer", "Cricket","Chess","Carom", "Tennis" ].
# Get an int input from user (n) and print the nth non empty string from the list.
sports = [" ", "                 ", " ","Swimming","Soccer", "Cricket","Chess","Carom", "Tennis"]
User_input = int(input("Enter the value:"))
print(f"Result_Before :{sports[User_input]}")
sports_final=[]
for sport in sports:
    if len(sport.strip())>0:
        sports_final.append(sport)
        continue
#print(sports_final)
print(f"Result_After :{sports_final[User_input]}")



