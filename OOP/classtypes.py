# class methods @classmethod can be used to specify that this method is not an instance method (i.e specific to individual functions, but global to the class)
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")