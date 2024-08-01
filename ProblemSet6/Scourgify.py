import sys
import csv

def main():
    filenames = check_sys()
    before, after = filenames
    output = []
    with open(before,"r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            split_names = row["name"].split(",")
            last_name, first_name = split_names
            output.append({"first": first_name.lstrip(), "last": last_name, "house": row["house"]})

    with open(after, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first","last","house"])
        writer.writerow({"first": "first", "last": "last", "house":"house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_sys():
    before = sys.argv[1]
    after = sys.argv[2]
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
        return [before, after]
    else:
        print("Need at least one command-line argument, with file format .csv")
        sys.exit

if __name__ == "__main__":
    main()
