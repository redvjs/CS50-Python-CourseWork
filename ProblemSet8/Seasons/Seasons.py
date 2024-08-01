import datetime
import sys
from datetime import date
import inflect

p = inflect.engine()

class Person:
    def __init__(self, dob):
        self.dob = dob

    def get_age(self):
        today = datetime.date.today()
        age = today - self.dob
        return int(age.total_seconds() / 60)
def main():
    print(datetime.date.today())
    dob_input = converter(input("What is your D.O.B? (Formated as YYYY-MM-DD): "))
    print(dob_input)

def converter(dob_input):
    try:
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
        person = Person(dob)
        minutes = person.get_age()
        in_words = p.number_to_words(minutes, andword = "").capitalize()
        return (f'{in_words} minutes')
    except:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()

