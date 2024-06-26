# Argument ... has incompatible type


# type hint
# n should be integer
def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number) # mypy meows3.py
