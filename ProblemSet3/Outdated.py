x = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
        date = input("Date: ")
        try:
            month, day, year = date.strip(" ").split("/")
            if (int(month) <= 12 and int(month) > 0 and int(day) >= 1 and int(day) <= 31):
                break
        except:
            try:
                month2, day2, year = date.split(" ")
                month = x.index(month2) + 1
                if day2.endswith(","):
                    day = day2.replace(",","")
                else:
                    print()
                    pass
                if (int(month) <= 12 and int(month) > 0 and int(day) >= 1 and int(day) <= 31):
                    break
            except:
                print()
                pass
print(f"{year}-{int(month):02}-{int(day):02}")




