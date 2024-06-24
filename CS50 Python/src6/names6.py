# Reads from a file, one line at a time
# super clean code if no sorting

with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())
