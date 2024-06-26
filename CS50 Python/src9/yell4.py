# Uses list comprehension


def main():
    yell_list_comprehension("This", "is", "CS50")
    yell2("This takes", "arbitrarily", "many", "args")
    yell_map("This is Sparta")


def yell_list_comprehension(*words):
    # list comprehension takes [Python expression]
    uppercased = [arg.upper() for arg in words]  # [word.upper() for word in words]
    print(*uppercased)


def yell2(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell_map(*words):
    # pass str.upper to map() by reference
    # map() will append () to str.upper()
    # and iterate
    # map( str.upper(for word in words) )
    # return mapped list
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()

# reformat using black
# black yell4.py