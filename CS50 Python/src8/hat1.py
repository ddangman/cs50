# Implements sort() with a class method and class variable

import random

# assume no objects of this class
# remove __init__ to implement Singleton
# class Hat is now a container for conceptually related data and functionality
class Hat: # has no reference to self

    # class variable exist w/in the class itself 
    # is unique (having only 1 copy) to be shared by all copies
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod # use classmethod decorator since hats can't be instantiated 
    def sort(cls, name): # reference to class instead of self. 'cls' used to not conflict with 'class'
        print(name, "is in", random.choice(cls.houses)) # cls.houses referral instead of self.houses


Hat.sort("Harry") # call method w/o instantiating object
