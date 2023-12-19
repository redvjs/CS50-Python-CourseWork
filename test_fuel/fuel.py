def main():
    enter = input("Enter A Fraction: ")
    fraction = convert(enter)
    percentage = gauge(fraction)
    print(percentage)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        percent = (int(x)/int(y)) * 100
        return percent
    except (ValueError, ZeroDivisionError, TypeError):
        raise

def gauge(percentage):
    if percentage <=1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()