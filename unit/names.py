names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")

#with open("names.txt", "r") as file:
 #   for line in file:
  #      print("hello,", line.rstrip())

    #lines = file.readlines()

#for line in lines:
 #   print("hello,", line.rstrip())

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
    # file.write(f"{name}\n")

#file = open("names.txt", "a")

#file.close()

#names = []

# for _ in range(3):
    #names.append(input("What's your name? "))

#for name in sorted(names):
#    print(f"Hello, {name}")
