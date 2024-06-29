# Favorite problem instead of favorite language

import csv

from collections import Counter

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = Counter()

    # Iterate over CSV file, counting favorite problem
    for row in reader:
        favorite_problem = row["problem"]
        counts[favorite_problem] += 1

# Print decreasing problem counts
for favorite_problem, count in counts.most_common():
    print(f"{favorite_problem}: {count}")
