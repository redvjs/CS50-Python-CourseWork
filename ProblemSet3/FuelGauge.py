
while True:
    fuel = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        new_x = int(x)
        new_y = int(y)
        calc = new_x / new_y
        if calc <= 1:
            break
    except (ValueError, ZeroDivisionError, TypeError):
        pass
percent = calc * 100
if percent <= 1:
     print("E")
elif percent >= 99:
     print("F")
else:
    print(f"{percent:.0f}%")

