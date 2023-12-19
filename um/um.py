import re

def main():
    print(count(input("Text: ")))


def count(s):
    x = re.findall(r"\bum\b[\,|\.|\?]?", s, re.IGNORECASE)
    counter = 0
    for word in x:
        counter += 1
    return counter




if __name__ == "__main__":
    main()