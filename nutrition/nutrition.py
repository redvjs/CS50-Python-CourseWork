fruit_dict = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pinapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "tangerine" : 50,
    "watermelon" : 80
}
item = input("Item: ")
for word in fruit_dict:
    if word == item:
        print("Calories:", fruit_dict[word])
