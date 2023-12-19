class Student:
    def __init__(self, name, house):
        self.house = house
        self.name = name

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    print(Student.get())

if __name__ == "__main__":
    main()