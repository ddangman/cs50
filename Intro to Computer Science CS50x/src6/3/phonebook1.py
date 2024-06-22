# Implements linear search for names using `in`

# A list of names
names = ["Carter", "David", "John"]

# Ask for name
name = input("Name: ")

# Python linear search
if name in names:
    print("Found")
else:
    print("Not found")
