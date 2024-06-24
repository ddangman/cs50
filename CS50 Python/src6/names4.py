# Adds context manager

name = input("What's your name? ")

# with automatically handles exceptions and release resources
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
