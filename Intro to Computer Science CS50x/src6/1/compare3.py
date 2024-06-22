# Conditionals, Boolean expressions, relational operators

from cs50 import get_int

# Prompt user for integers
x = get_int("What's x? ")
y = get_int("What's y? ")

# Compare integers
if x < y: # parenthesis optional
    print("x is less than y")
elif x > y: # parenthesis optional
    print("x is greater than y")
else: # there is no other case for integers
    print("x is equal to y")
