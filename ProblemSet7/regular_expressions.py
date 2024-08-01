## we can use re library for regular expressions, lets you define, look for and find patterns (i.e patterns for email address)
## for future self, these two lines are included in the other ones below
import re
email = input("What's your email? ").strip()
## can also use the | syntax:
## A|B = either A or B
## (...) = a group
## (?:...) non-capturing version

if re.search(r"^\w+@\w+\.(edu|com|gov|org)$", email):
    print("Valid")
else:
    print("Invalid")

## built in are some additional patterns we can use instead of typing it out ourselves:
## here they are:
## \d decimal digit, \D not a decimal digit
## \s whitespace characters \S not a whitespace character
## \w word character (inc numbers and underscore)
## \W not a word character
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

## alternatively, we can use a range of characters using the [] syntax:
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
## there is also the following syntax:
## [] = set of characters
## [^] = complementing the set --> any character except i.e. [^@]
## below we see that we filter that we can have anything EXCEPT @ "[^@]
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

## if we want to check if the email has .edu at the end, we cant simply add .edu because the "." is used as an expression
## instead, we need to convert the string to a raw string r".+...." and use a backslash "\":
## we can add "^" (matches start of string) to say that (to match start and end) this is how the string should start, and "$" (matches end of the string just before the newline) to say how it should end:
if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

## Simple and essentially does the same thing as we did initially.
## .* means we want something to the left of the @ and something to the right
## this means even if its blank we will still get valid as per below
## instead should use + (1 or more reps) or ..* (. any character, .* 0 or more)
## . (any character except newline), * (0 or more repititions), + (1 or more repititions), ? (0 or 1 repitition) {m} or {m,n} (m or m-n repititions)
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

## will give true answer if username == if anything except none or ""
## dont get confused, these are two different bools, if username.... and "." in domain.
if username and "." in domain:
## to be more specific we can change from "." in domain to .endswith():
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

## alternatively we can use the split function:

email = input("What's your email? ").strip()

username, domain = email.split("@")

## Checking if valid email, however typing @. will still print valid, also @ can be anywhere and . can be anywhere.
## we want . and @ in the right place
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("invalid")




