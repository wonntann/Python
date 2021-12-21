# Python
Python Basics

## Introduction
In this module, you will be learning the basics of Python.

## Learning Objectives
* Create and execute a Python file
* Write and run Python code in Visual Sudio Code
* Python concepts: 
  * [Loops](https://docs.python.org/3.10/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
  

## Tips
* Be mindful of the indentation of the code. You might get an IndentationError:
```Python
>>> for i in elements:
... print(i)
  File "<stdin>", line 2
    print(i)
    ^
IndentationError: expected an indented block
```

## How to Read This

- **>>>** means the code is being run in the Python interpreter. Insert the Python code that  is displayed after the symbols. Do not write those symbols in your script.

- Navigate with the [generated table of contents](https://github.blog/changelog/2021-04-13-table-of-contents-support-in-markdown-files/) by navigating to the left top, floating menu of this README file.

# Loops
Looping permits the user to repeat the code without having to write it again. This can shorten the programming process and allow for simpler and more manageable code. 

<p align="right"><a href="top">Back to Top</a></p>

# for Loops
"The [for statement](https://docs.python.org/3/reference/compound_stmts.html#for) is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object"

``` Python
elements = ["Earth", "Wind", "Water", "Fire"]
for element in elements:
    print(element)
```
Which will output:

``` Python
Earth
Wind
Water
Fire
```

In this example, Python runs the code inside the for loop by first printing out the first value of the provided list and then continuing to print the subsequent items in sequential order. This is known as iteration. The letter i to the right of for serves as a temporary variable. This variable can have assigned to any name, however, it is helpful to assign a meaningful name. Commonly, a single letter is used to simplify the for loop creation.

``` Python
planets = ["Mars", "Earth", "Saturn", "Jupiter"]
for planet in planets:
    print(f"{planet} is one of my favorite planets.")
```
Which will output:
``` Python 
Mars is one of my favorite planets.
Earth is one of my favorite planets.
Saturn is one of my favorite planets.
Jupiter is one of my favorite planets.
```

# Continuing to Code After Running a for Loop
You will want to get out of the scope of the for loop inorder to continue with the same code. The Python interpreter will only repeat the code that is indented underneath the for loop. 

``` Python
planets = ["Mars", "Earth", "Saturn", "Jupiter"]
for planet in planets:
    print(f"{planet} is one of my favorite planets.")
print("I live on the planet Earth, which is my absolute favorite.")
```
Which will output:

``` Python
Mars is one of my favorite planets.
Earth is one of my favorite planets.
Saturn is one of my favorite planets.
Jupiter is one of my favorite planets.
I live on the planet Earth, which is my absolute favorite.
```
<p align="right"><a href="top">Back to Top</a></p>

# range() Function

``` Python
for item in range(1, 7):
    print(item)
```
Which will output:

``` Python
1
2
3
4
5
6
```
start, stop, pattern

<p align="right"><a href="top">Back to Top</a></p>

Working With a List
============
## Slicing
``` Python
names = ["Sally", "John", "Greg", "Frida"]
print(names[0:2])
```
Which will output:

``` Python
['Sally', 'John']
```

Omit the number to the left and/or the right of the colon (:) and the list will be read from the beginning to the end of the list, respectively.
``` Python
names = ["Sally", "John", "Greg", "Frida"]
print(names[2:])

names = ["Sally", "John", "Greg", "Frida"]
print(names[:])

names = ["Sally", "John", "Greg", "Frida"]
print(names[-2:])
```
Which will output:

``` Python
['Greg', 'Frida']
['Sally', 'John', 'Greg', 'Frida']
['Greg', 'Frida']
```
<p align="right"><a href="top">Back to Top</a></p>

# Exercise
1. Quickly make a list of even numbers.
2. Make a list with 100 numbers, starting with 1.
3. Add all of the numbers together.
4. Find the even numbers from the list.

# Vocabulary
min()
max()
sum()
