# we can use classes to make our own data types, using class
# everytime we use a class we create an object (hence object orriented programming)

class Student:
    # __init__ instance method, allows you to initialize the contents of this class
    # we are adding instance variables to objects
    def __init__(self, name, house): # self has to come first, which gives you access to the current object that was just created
        self.name = name
        self.house = house
    # with the def str method, we can define how strings are called, i.e. in a print statement
    def __str__(self): #this method only takes in self
        return f"{self.name} from {self.house}"

    # properties is an attribute that has defence mechanisms
    # decorators are functions that modify the behaviour of other functions
    # Getter - you have to set the getter as @property
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    # Setter - this has to be set as @name.setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    # we can still simplify this as follows:
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    # so whats different?
    # now we are setting the stage for more powerful features of classes
    # now we are standardizing how we pass data into the class
    # we have more control over the correctness of our data
    # clasess come with certain methods
    # these allow you to determine the behaviour in a standard way
    ##return Student(name, house) # this constructs a student object using the class as a mould

    ## student = Student()
    ## student.name = input("Name: ")
    ## student.house = input("House: ")
    ## return student
    # classes have attributes, using the syntax.

if __name__ == "__main__":
    main()