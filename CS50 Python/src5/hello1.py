def main():
    name = input("What's your name? ")
    print(hello(name)) # caller should handle all printing


# returning string more readily testable
def hello(to="world"):
    return f"hello, {to}" # function should return a str instead


if __name__ == "__main__":
    main()
