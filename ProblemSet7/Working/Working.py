import re

pm_conversions = {
        "x":"y",
        "1":"13",
        "2":"14",
        "3":"15",
        "4":"16",
        "5":"17",
        "6":"18",
        "7":"19",
        "8":"20",
        "9":"21",
        "10":"22",
        "11":"23",
        "12":"24",
    }

def main():
    print(str(convert(input("Hours: "))))

def convert(s):
    try:
        if match := re.search(r"\b([1-9]|1[0-2])\b\:?\b(0[0-9]|[0-5][0-9])?\b\s(AM|PM){1}\sto\s\b([1-9]|1[0-2])\b\:?\b(0[0-9]|[0-5][0-9])?\b\s(AM|PM)", s):
            if match.group(3) == "AM" and match.group(6) == "AM":
                return(f"{int(match.group(1)):02}:{match.group(2)} to {int(match.group(4)):02}:{match.group(5)}")
            elif match.group(3) == "AM" and match.group(6) == "PM":
                return(f"{int(match.group(1)):02}:{match.group(2)} to {int(pm_conversions.get(match.group(4)))}:{match.group(5)}")
            elif match.group(3) == "PM" and match.group(6) == "AM":
                return(f"{int(pm_conversions.get(match.group(1))):02}:{match.group(2)} to {int(match.group(4)):02}:{match.group(5)}")
            elif match.group(3) == "PM" and match.group(6) == "PM":
                return(f"{int(pm_conversions.get(match.group(1))):02}:{match.group(2)} to {int(pm_conversions.get(match.group(4)))}:{match.group(5)}")
    except(NameError):
        raise


if __name__ == "__main__":
    main()
