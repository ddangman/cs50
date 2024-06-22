# Implements get_int with a loop

def get_int(prompt):
    while True: # forever loop until user inputs integer
        try:
            return int(input(prompt)) # exit forever loop
        except ValueError:
            print("Not an integer")
            # pass


def main():

    # Prompt user for x
    x = get_int("x: ")

    # Prompt user for y
    y = get_int("y: ")

    # Perform addition
    print(x + y)


main()
