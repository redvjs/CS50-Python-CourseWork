def main():
    amount = 50
    while amount > 0:
        print(f"Amount due: {amount}")
        insert = int(input("Insert coin: "))
        if insert == 25 or insert == 10 or insert == 5:
                amount -= insert
    amount_owed = abs(amount)
    print(f"Amount owed: {amount_owed}")
main()

