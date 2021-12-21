# Python Basics

## Introduction
In this module, you will be learning the basics of Python. You can run all of this code within the terminal. Simply write **python3** and hit **enter**, that will allow you to write Python straight into the terminal, otherwise, you can use your preferred ide (Integrated development environment).

## Learning Objectives
* Create and execute a Python file
* Write and run Python code in Visual Sudio Code
* Python concepts: 
  * Printing to the console
  * Basic Variables
  * Input and Output 
  * Setup files
  * Open and create new file
  * .py format
  * Running file

## How to Read This

**>>>** means the code is being run in the Python interpreter. Insert the Python code that  is displayed after the symbols. Do not write those symbols in your script.

- Navigate with the [generated table of contents](https://github.blog/changelog/2021-04-13-table-of-contents-support-in-markdown-files/) by navigating to the left top, floating menu of this README file.


# Variables

Python objects can be stored in names known as variables.

```python
>>> month = "January"
``` 

Python follows the PEP8 guidelines for naming variables. Here is the [documentation]("https://www.python.org/dev/peps/pep-0008/#naming-conventions")

There are a lot of ways to assign a name to a variable. It helps to have a descriptive name and to be consistant when naming. The following naming styles are recognized:
* b (single lowercase letter)
* B (single uppercase letter)
* lowercase
* lower_case_with_underscores
* UPPERCASE
* UPPER_CASE_WITH_UNDERSCORES
* CapitalizedWords
* mixedCase
* Capitalized_Words_With_Underscores

The general practice is to usa a lowercase single letter, word or words. If there is a space in the variable name, it is represented with an underscore to improve readability.

``` Python
>>> first_name = "Vi"
>>> last_name = "Pope"
```

Indexing
============
Each character is inherently given a number in relation to it's position, whether is be in a sting, list, or another data type. Python is zero based indexing, which has the first value by given a 0 position. The subsequent values will increase by 1 count, which is positive indexing.

``` Python
>>> month = "January"
>>> month[1]
'a'

>>> season = "Autumn"
>>> season[-3]
'u'
```

If you would like to access the item from the end, you use the negative index. Start with the number -1 and decrease by 1 as you move left in the item.




Keywords
============
Keywords are reserved word within Python. These reserved words cannot be used as variable names, function names or any other identifier. Keywords are case sensitive and a list of Python Keywords can be found in this [keywords handout](pyKeywords.pdf).

Here is an example for the keyword del, which removes the listed index in the square brackets:

```python
>>> animals = ["tiger", "bear", "lion"]
>>> del animals[0]
['bear', 'lion']
```

[Keywords Handout](../assets/pyKeywords.pdf)




Indentation
============
<blockquote>Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements. </blockquote>

- [Python Documentation]("https://docs.python.org/3/reference/lexical_analysis.html?highlight=reserved%20words#indentation")

Python uses whitespace to delimit control flow blocks. The total number of spaces preceding the first non-blank character then determines the line’s indentation. Indentation cannot be split over multiple physical lines using backslashes; the whitespace up to the first backslash determines the indentation.

``` Python
values = ["a", "b", "c"]

def looping_list():
  for i in range(3):
      return "range:", i

  for i in values:
      return "for loop in list", i

for index in range(len(values)):
    print("for range(len): ", index, values)

print(looping_list())
```


Input Output
============
You are able to compose your Python script and when you run the file, you see the ouput in the terminal.

You can practice printing in the terminal with **print()** functions and have a variable or another data type in between the parentheses. Python to see the data type of an object:

``` Python
>>> num = 123
>>> type(num)
<class 'int'>
``` 


Comments
============
Comments can be very helpful to both the programmer, as well as, the person reading the code. Comments allows the programmer to put notes within the script that are not processed by the computer. These notes often detail what the desired behavior of the code is, what a variable stands for, an outline of the code, required steps to get the code running or for many more reasons. A hash mark (#) will begin a comment and anything to the right of the hash mark will be ignored by the Python interpreter.

``` Python
>>> # This is a comment!
>>> print("Hello World")
Hello World
```




Tips
============
* Run code with print() to test code
* use help("keywords") to get a list of available keywords




Exercises
============
You can create a Python script or continue working in the terminal or IDLE. The provided solutions will be in an IDE (Integrated development environment)


1. Create a variable for your name
2. Access the second letter of your name, using the positive and negative index.
3. Go back to 3 lines of your previous script and add a comment. It should be something regarding the code behavior with your name at the top of the file.
4. Write out a name of your favorite meal in the interpreter and get a NameError to occur. Now store that name in a variable and call the variable. See if you get the error again.




Vocabulary
============
type()
print()




Contributing
============
Thanks for checking out this page, since the more positive edits and critics of this repo will help this project benefit more individuals.

Submit an issue or I encourage you to fork this repo and make another page in the changes directory and contribute to this project!

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



Contact
============
![Twitter](https://img.shields.io/twitter/follow/wonntann?color=red&style=for-the-badge)


