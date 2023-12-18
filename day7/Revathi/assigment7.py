sports = ["","       ","","swimming","soccer","cricket","chess","carom","tennis"]

n = int(input("Enter n = "))
cnt = 0
for sport in sports:
    if len(sports) < n:
        print("No Such Element")
        break
    if len(sport.strip()) >= 1:
        cnt = cnt + 1
        if cnt == n:
            print(sport)
            break