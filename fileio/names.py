names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"Hello, {name}")


#5 with open("names.txt") as file:
    #5 for line in sorted(file):
        #5 print("hello,", line.rstrip())


#4 with open("names.txt", "r") as file:
    #4 for line in file:
        #4 print("Hello,", line.strip())


    #3 lines = file.readlines()
#3 with open("names.txt", "r") as file:
#3 for line in lines:
    #3 print(f"Hello, {line.rstrip()}")




#1/2 name = input("What's your name? ")

#1 file = open("names.txt", "a")
#2 with openm("names.txt", "a") as file:
    #1/2 file.write(f"{name}\n")
#1 file.close()



# names = []

# for _ in range(3):
    # names.append(input("What's your name?"))

# for name in sorted(names):
    # print(f"Hello, {name}")