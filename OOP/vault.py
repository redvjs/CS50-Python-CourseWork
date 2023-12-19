class Vault:
    def __init__(self, gold=0, silver=0, copper=0):
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def __str__(self):
        return f"{self.gold} Gold, {self.silver} Silver, {self.copper} Copper"

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        copper = self.copper + other.copper
        return Vault(gold, silver, copper)
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)