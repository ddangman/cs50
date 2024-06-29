# Sorts favorites by value using .get

import csv

from collections import Counter

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counter object
    counts = Counter()

    # Iterate over CSV file, counting favorite language
    for row in reader:
        favorite_language = row["language"]
        counts[favorite_language] += 1

# Print decreasing language counts
for favorite_language, count in counts.most_common():
    print(f"{favorite_language}: {count}")
