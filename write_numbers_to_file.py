with open("numbers.txt", "w") as f:
    for i in range(100):
        f.write(str(i))
        f.write("\n")