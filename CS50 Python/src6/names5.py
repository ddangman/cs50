# Reads from a file
# default open() is 'r'ead

with open("names.txt") as file:
    lines = file.readlines()

# end="" could be used
for line in lines:
    print("hello,", line.rstrip())

# strip() is used to delete all the leading and trailing characters mentioned in its argument.
# lstrip() is used to delete all the leading characters mentioned in its argument.
# rstrip() is used to delete all the trailing characters mentioned in its argument.