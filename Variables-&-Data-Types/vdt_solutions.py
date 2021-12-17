# Each solution is commented by string literals, simply delete the first 3 double quotation marks.
""" # 1. Print out addition, subtraction, division, and multiplication that results in the integer number 10.
addition = 5 + 5
subtraction = 15 - 5
division = 100 / 10
multiplication = 5 * 2
print(addition)
print(subtraction)
print(int(division))
print(multiplication) """

""" # 2. Print out addition, subtraction, division, and multiplication that results in the float number 8.0
addition = 5 + 3.0
subtraction = 13.0 - 5
division = 64 / 8
multiplication = 4 * 2.0
print(addition)
print(subtraction)
print(division)
print(multiplication) """

""" # 3. Save a new script called name_strings.py. Print out your first and last name in a sentence, using 2 different variables using an f string. 
first_name = "Lucille"
last_name = "Ball"
print(f"{first_name} {last_name} was an American actress with many talents.") """

""" # 4. Get an input from a user for their first name. Print out a greeting to a person by their first name using an f string.
first_name = input("What is your first name?\n").capitalize()
print(f"Welcome {first_name}! I can't wait until you start to create projects using the Python language.") """

""" # 5. Convert a variable to all lowercase and uppercase.
num = "Five"
print(num.upper())
print(num.lower()) """

""" # 6. Print out a your favorite animal, color, and sport in a comprehensive sentence. 
color = "maroon"
animal = "bobcat"
sport = "soccer"
my_sentence = f"{animal.capitalize()}s are not known for being good at {sport} nor are they {color}."
print(my_sentence) """

""" # 7. Get an input with extra white space and use the listed methods to eliminate the spaces.
extra_spaces = input("What month is it?")
extra_spaces.lstrip()
print(extra_spaces) """


""" 8. Remove the blank spaces in the string on Ex.1
my_string = "         Hello World   "
print(my_string.strip()) """

""" 9. Replace the second word with Sunshine in Ex.1 with the spaces removed.
my_string = "         Hello World   "
my_string.replace("World", "Sunshine")
print(my_string.strip()) """
