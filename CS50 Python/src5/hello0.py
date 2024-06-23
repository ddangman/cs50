# assert in 
#$ python -m pytest
# are designed to test arguments into functions
# and return values ie ==
# NOT side-effects eg print(side-effect)


def main():
    name = input("What's your name? ")
    hello(name)


# print is side effect that's difficult to test
# better to return string
def hello(to="world"):
    print("hello,", to) # caller should handle all printing


if __name__ == "__main__":
    main()
