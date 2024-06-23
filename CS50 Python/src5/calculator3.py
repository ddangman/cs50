# Demonstrates try assert except test_calculator.py catching incorrect square function


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n


if __name__ == "__main__":
    main()
