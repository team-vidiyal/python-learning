try:
    with open("./hello.txt", "w") as file:
     file.write("Some content")

except Exception:
    print("Error occurred")