f = open("C:/Deepa/file1.txt", "r")
print(f.read())

f1 = open("deepa_practice_file", "w")
print(f1.write("new line added"))
f1.close()

f2 = open("deepa_practice_file", "a")
f2.write("\none new line added")
f2.close()

f3 = open("deepa_practice_file", "r")
print(f3.read())