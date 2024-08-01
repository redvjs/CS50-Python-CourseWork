def main():
    greeting = value(input("Greeting: ").lower().strip())
    print(f"${greeting}")

def value(greeting):
    lower_case = greeting.lower().strip()
    if lower_case.startswith("hello"):
        return 0
    elif lower_case.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()





