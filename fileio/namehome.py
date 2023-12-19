import csv

def making_list():
    while True:
        name = input("What's your name? ")
        home = input("Where's your home? ")
        with open("namehome.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"name": name, "home": home})
        more = input("Would you like to add more to your list?")
        if more.startswith("y"):
            return False
        elif more.startswith("n"):
            return True

making_list()