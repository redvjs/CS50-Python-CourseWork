import csv

students =[]

with open("students1.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student ['name']} live at {student ['home']}")



## students = []

## with open("students.csv") as file:
    ## for line in file:
       ##  name, house = line.rstrip().split(",")
        ## student = {"name": name, "house": house}
        ## students.append(student)


# def get_name(student):
    # return student["name"]
# def get_house(student):
    # return student["house"]

# for student in sorted(students, key=get_name):
##for student in sorted(students, key=lambda student:student["name"]):
    #print(f"{student['name']} is in {student['house']}")


# with open("students.csv") as file:
    # for line in file:
        # name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")