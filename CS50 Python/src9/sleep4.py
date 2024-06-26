# Uses yield


def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# yield is a generator that returns iterators asynchronously
# return rows of 1 in n of 🐑 at a time
# generator retains state while Python suspends the function
def sheep(n):
    for i in range(n):
        yield "🐑" * i # generator


if __name__ == "__main__":
    main()
