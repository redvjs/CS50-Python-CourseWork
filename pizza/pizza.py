import sys
import csv
from tabulate import tabulate
def main():
    filename = check_sys()
    table = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            table.append(row)
        print(tabulate(table, headers = "firstrow", tablefmt="grid"))
def check_sys():
    filename = sys.argv[1]
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        return filename
    else:
        print("Need at least one command-line argument, with file format .csv")
        sys.exit
if __name__ == "__main__":
    main()