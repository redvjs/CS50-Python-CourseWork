import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")







# students = []

#with open("students.csv") as file:
 #   for line in file:
  #      name, house = line.rstrip().split(",")
   #     student = {"name": name, "house": house}
            #student = {}
            #student["name"] = name
            #student["house"] = house
    #    students.append(student)


#def get_name(student):
 #   return student["name"]
# or simply use:
#for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in {student['house]}")

#for student in sorted(students, key=get_name):
 #   print(f"{student['name']} is in {student['house']}")


# with open("students.csv") as file:
  #  for line in file:
   #     name, house = line.rstrip().split(",")
    #    print(f"{name} is in {house}")



# with open("students.csv") as file:
    # for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")
