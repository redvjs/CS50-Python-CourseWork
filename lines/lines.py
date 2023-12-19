import sys

def main():
    filename = check_sys()
    try:
        file = open(filename, "r")
        lines = file.readlines()
    except (FileNotFoundError):
        print("File Not Found")
        sys.exit
    counter = 0
    for line in lines:
        if check_file(line) == True:
            counter += 1
    print(counter)

def check_sys():
    filename = sys.argv[1]
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        return filename
    else:
        print("Need one file name")

def check_file(line):
    if line.lstrip().startswith("#"):
        return False
    if line.isspace():
        return False
    else:
        return True

if __name__ == "__main__":
    main()