# Tests a function with multiple functions via pytest
# square is correct but input NOT converted to integer


def main():
    x = input("What's x? ")
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
