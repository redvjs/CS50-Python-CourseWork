camelcase = input("camelCase: ")

snake_case = ""

for uppercase in range(len(camelcase)):
    if camelcase[uppercase].isupper():
        snake_case = snake_case + "_" + camelcase[uppercase].lower()
    else:
        snake_case += camelcase[uppercase]
print("snake case :", snake_case)