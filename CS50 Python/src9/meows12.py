"""
CMD line arg general convention:
single-dash for single char
double--dash for string
"""


# Use command-line argument library
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# python meows12.py -n 5
# will not run python meows.py w/o -n int