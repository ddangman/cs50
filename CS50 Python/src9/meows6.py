# Prints None because mistakes meow as having a return value


def meow(n: int):
    for _ in range(n):
        print("meow") # side effect here


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
