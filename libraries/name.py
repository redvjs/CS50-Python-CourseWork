import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# elif len(sys.argv) > 2:
    # sys.exit("Too many arguments")
## we can also loop over sys.argv if we want to print multiple peoples "name tags"
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)



#try:
    #print("Hello, my name is", sys.argv[1])
#except IndexError:
    #print("need a name")

