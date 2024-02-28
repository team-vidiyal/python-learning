import os
import shutil
import datetime


print(type(datetime.date.today()))
# os.mkdir("../assignments/day10")
# os.remove("./hello.txt")
try:
 shutil.move("./hello.txt", "../assignments/day10/hello.txt")
except Exception:
    print("File not found")
#
try:
    os.mkdir(str(datetime.datetime.now()))
except Exception:
    print("Exception occurred")


