This repository contains the coursework completed throughout Harvard University's CS50 - Introduction to Programming with Python course.

Please see a detailed overview of what the tasks entailed below.

--- Problem Set 0 - Functions and Variables ---

- Indoor Voice:
    WRITING IN ALL CAPS IS LIKE YELLING.
    Best to use your “indoor voice” sometimes, writing entirely in lowercase.
    In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged.
    You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
  
- Playback Speed:
    Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.
    In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
  
- Making Faces:
    Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!
    In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
    and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
    Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
    You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
  
- Einstein:
    Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc^2, wherein E represents energy (measured in Joules), m represents mass (measured in kilograms),
    and c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.
    In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
  
- Tip Calculator:
    In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
    Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
    dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
    percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
    Assume that the user will input values in the expected formats.



--- Problem Set 1 - Conditionals ---

- Deep Thought:
    In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
  
- Home Federal Savings Bank:
    In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. 
    The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.
    In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
    If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
    
- File Extensions:
    Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. 
    For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.
    Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. 
    When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. 
    To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.
    See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.
    In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
    .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
    If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
    
- Math Interpreter:
    Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.
    In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
    Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
    x is an integer
    y is +, -, *, or /
    z is an integer
    For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
    Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

- Meal Time:
    Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
    In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
    If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
    And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
    Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
  
--- Problem Set 2 - Loops ---
- camelCase:
    In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. 
    For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.
    Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.
    In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
    
- Coke Machine:
    Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
    In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
    Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
    
- Just setting up my twttr:
    When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
    In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
    
- Vanity Plates: 
    In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
        “All vanity plates must start with at least two letters.”
        “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
        “No periods, spaces, or punctuation marks are allowed.”
    In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. 
    Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

- Nutrition Facts:
    The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”.
    In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. 
    Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
  


--- Problem Set 3 - Exceptions ---
 
- Fuel Gauge:
    Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
    In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
    If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
    If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
     
- Felipe’s Taqueria:
    One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:
    {
    "Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00 
    }
    In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
    After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
    Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

- Grocery List:
    Suppose that you’re in the habit of making a list of items you need from the grocery store.
    In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
    Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
    Treat the user’s input case-insensitively.
    Be sure to avoid or catch any KeyError.
    Note that you can sort a dictionary’s keys alphabetically by passing that dictionary as an argument to sorted.
    
- Outdated:
    In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
    Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!
    Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
    no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.
    In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.



--- Problem Set 4 - Libraries ---

- Emojize:
    Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. 
    Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.
    See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.
    In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

- Frank, Ian and Glen’s Letters:
    FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art
    Among the fonts supported by FIGlet are those at figlet.org/examples.html.
    FIGlet has since been ported to Python as a module called pyfiglet.
    In a file called figlet.py, implement a program that:
    Expects zero or two command-line arguments:
    Zero if the user would like to output text in a random font.
    Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.
    If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

- Adieu, Adieu:
    In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:
    Adieu, adieu, to yieu and yieu and yieu
    Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:
    Adieu, adieu, to yieu, yieu, and yieu
    To be fair, “yieu” isn’t even a word; it just rhymes with “you”!
    In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. 
    Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 'n' names with 'n-1' commas and one and, as in the below:
      Adieu, adieu, to Liesl
      Adieu, adieu, to Liesl and Friedrich
      Adieu, adieu, to Liesl, Friedrich, and Louisa
      Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
      Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
      Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
      Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

- Guessing Game:
    I’m thinking of a number between 1 and 100…
    What is it?
    In a file called game.py, implement a program that:
        Prompts the user for a level, 
        . If the user does not input a positive integer, the program should prompt again.
        Randomly generates an integer between 1 and 
        , inclusive, using the random module.
        Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output Just right! and exit.
    
- Little Professor:
    One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. \
    If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. 
    And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).
    In a file called professor.py, implement a program that:
        Prompts the user for a level, 
        . If the user does not input 1, 2, or 3, the program should prompt again.
        Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
         digits. No need to support operations other than addition (+).
        Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 
        If the user has still not answered correctly after three tries, the program should output the correct answer.
        The program should ultimately output the user’s score: the number of correct answers out of 10.
    Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
    and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

Bitcoin Price Index:
    Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.
    Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.
    In a file called bitcoin.py, implement a program that:
      Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
      Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions.




--- Problem Set 5 - Unit Tests using PyTest ---

- Testing my twttr:
    In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, 
    whether inputted in uppercase or lowercase.
    Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py

- Back to the Bank:
    In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns an int, namely 0 if that str starts with “hello”, 
    20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.
    Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_bank.py
    
- Re-requesting a Vanity Plate:
    In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, 
    but main is only called if the value of __name__ is "__main__":
    Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_plates.py
    
- Refueling:
    In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
      convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
      If Y is 0, then convert should raise a ZeroDivisionError.
      gauge expects an int and returns a str that is:
      "E" if that int is less than or equal to 1,
      "F" if that int is greater than or equal to 99,
      and "Z%" otherwise, wherein Z is that same int.
    Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:



--- Problem Set 6 - File I/O ---
- Lines of Code:
    One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. 
    Of course, just because a program (or even function) has more lines of code than another doesn’t necessarily mean it’s more complex.
    even though the former has (more than) twice as many lines of code. In fact, the former might arguably be simpler if it’s easier to read! So lines of code should be taken with a grain of salt.
    Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. 
    If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
    Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

- Pizza Py:
    Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”
    Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:
        Sicilian Pizza,Small,Large
        Cheese,$25.50,$39.95
        1 item,$27.50,$41.95
        2 items,$29.50,$43.95
        3 items,$31.50,$45.95
        Special,$33.50,$47.95
    See regular.csv for a CSV file of regular pizzas as well.
    Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:
    In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
    a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist,
    the program should instead exit via sys.exit.

- Scourgify:
    Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:
    - Data not included due to length -
    Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. 
    Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:
      Dear Potter, Harry,
    Rather than with, for instance:
      Dear Harry,
    In a file called scourgify.py, implement a program that:
      Expects the user to provide two command-line arguments:
      the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
      the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
      Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
      If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
      
- CS50 P-Shirt:
    After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?
    In a file called shirt.py, implement a program that expects exactly two command-line arguments:
      in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
      in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
    The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.
    Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
    using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, 
    per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
    The program should instead exit via sys.exit:
      if the user does not specify exactly two command-line arguments,
      if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
      if the input’s name does not have the same extension as the output’s name, or
      if the specified input does not exist.
    Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
    If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code. 
    But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!



--- Problem Set 7 - Regular Expressions ---

- NUMB3RS:
    An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive.
    Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!
    In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
    Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
    Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly, each of whose names should begin with test_ 
    so that you can execute your tests.
  
- Watch on YouTube:
    In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. 
    Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.
        http://youtube.com/embed/xvFZjo5PgG0
        https://youtube.com/embed/xvFZjo5PgG0
        https://www.youtube.com/embed/xvFZjo5PgG0
    Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
  
- Working 9 to 5:
    In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
    Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
        9:00 AM to 5:00 PM
        9 AM to 5 PM
        9:00 AM to 5 PM
        9 AM to 5:00 PM
    Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
    But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
    Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

- Regular, um, Expressions:
    In a file called um.py, implement a function called count that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. 
    For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0.
    Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
    Either before or after you implement count in um.py, additionally implement, in a file called test_um.py, three or more functions that collectively test your implementation of count thoroughly,
    each of whose names should begin with test_ so that you can execute your tests with:

- Response Validation:
    In a file called response.py, using either validator-collection or validators from PyPI, implement a program that prompts the user for an email address via input and then prints Valid or Invalid, respectively, if the input is a syntatically valid email address.
    You may not use re. And do not validate whether the email address’s domain name actually exists.



--- Problem Set 8 - Object Oriented Programming ---

- Seasons of Love:
    Assuming there are 365 days in a year, there are 365 x 24 x 60 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have additional minutes. 
    In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. 
    Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.
    In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. 
    Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. 
    In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
    You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.
    Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

- Cookie Jar:
    Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:
        __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
        __str__ should return a str with 🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    capacity should return the cookie jar’s capacity.
    size should return the number of cookies actually in the cookie jar, initially 0.
    Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.
    Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
    Note that it’s not as easy to test instance methods as it is to test functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables). To test one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit). But the method you call first might itself not be correct!
    And so programmers sometimes mock (i.e., simulate) state when testing methods, as with Python’s own mock object library, so that you can call just the one method but modify the underlying state first, without calling the other method to do so.
    For simplicity, though, no need to mock any state. Implement your tests as you normally would!

- CS50 Shirtificate:
    Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.
    In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:
    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.
    All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.
    Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.
    No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!

