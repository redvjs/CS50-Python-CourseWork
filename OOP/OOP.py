

def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
# for a dictionary we can change the input when incorrect:
## if student["name"] == "Padma":
    ## student["house"] = "Ravenclaw"

# for a list we can change the input when incorrect:
## if student[0] == "Padma":
    ## student[1] = "Ravenclaw
def get_student():

    # alternatively we can make this shorter and make the dict
    # in the return function^
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

    ##student = {}
    ##student["name"] = input("Name: ")
    ##student["house"] = input("House: ")
    ## name = input("Name: ")
    ## house = input("House: ")
    # returning (name, house) returns a tuple which is immutable,
    #if you need to change these values you should return it as a list using []
    ## return [name, house]
#we can tighten this up into a single function

##def get_name():
##    return input("Name: ")
##def get_house():
##    return input("House: ")

if __name__ == "__main__":
    main()
#now we should start writing our own functions to make
#building blocks to make more complicated programs

##name = input("Name: ")
##house = input("House: ")
##print(f"{name} from {house}")
#start by writing program very procedurally