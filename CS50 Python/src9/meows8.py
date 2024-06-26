# Success


def meow(n: int) -> str:
    return "meow\n" * n # multiplication is overloaded to repeat strings


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
