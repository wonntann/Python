# Conditionals

## Introduction
In this module, you will be learning the conditionals of Python. You can run all of this code within the terminal. Simply write **python3** and hit **enter**, that will allow you to write Python straight into the terminal, otherwise, you can use your preferred ide (Integrated development environment).

## Learning Objectives
* Create and execute a Python file
* Write and run Python code in Visual Sudio Code
* Python concepts: 
  * Open and create new file
  * .py format
  * Running file
  * Conditionals concepts

## How to Read This

**>>>** means the code is being run in the Python interpreter. Insert the Python code that is displayed after the symbols. Do not write those symbols in your script. If the code does not have any symbols before it, it is being run in an IDE.



# Boolean Expressions
A Boolean expression is just another name for a conditional test, either True or False. Boolean values are found keeping track of certain conditions, i.e. to check whether a game is running or if a user has the authority to login a website.

Examples

``` python
car = 'subaru'
cars = ["audi", "ford", "mercedes"]

def print_boolean():       
    if "ford" in cars:
        print("I predict True")
    if "u" in car:
        print("I predict True")

name = input("type of car prefer Audi or Ford:\n")
if name.lower() == "audi":
    print("Yep, an audi")

def conditional_booleans():
    if car == "subaru":
        return True

def conditional_false():
    if car != "audi":
        return False

print(conditional_booleans())
print(conditional_false())
```

# if-else Statements

When working with a conditional statement, you will take an action often using the if-else statement. An if block sets a test condition and identifies what to do if the test condition runs true or false. An else block is the default behavior if the initial if block was false.

``` python
x = 15
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")
```

# Testing Multiple Conditions
Sometimes, you will have to test multiple conditions, if … elif … elif … sequence eill test the set conditions in order until one evaluates to true. Anytime during the eavulation of the test, if a condition runs true, that if … elif … elif … sequence will stop executing.

``` python
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x equals 10")
else:
    print("x is not greater than 10")
```


# Exercise
1. Making an order of an ice cream sundae with your choice of toppings.

2. Print out 2 conditions that one is True and the other one is False.


3. Create a blank list, use a conditional statement to add to the blank list and check if not empty.


