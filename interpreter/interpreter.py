expression = input("Expression: ")

x, y, z = expression.split(" ")

convert_x = float(x)
convert_z = float(z)

if y == "+":
    result = convert_x + convert_z
elif y == "-":
    result = convert_x - convert_z
elif y == "*":
    result = convert_x * convert_z
elif y == "/":
    result = convert_x / convert_z

print(round(result, 1))