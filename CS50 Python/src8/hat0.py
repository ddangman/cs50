# Implements sort() with an instance method

import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name): # instance method are passed 'self', the current object
        print(name, "is in", random.choice(self.houses))


hat1 = Hat() # we need to allow at most one Sorting Hat
hat1.sort("Harry")

hat2 = Hat()
