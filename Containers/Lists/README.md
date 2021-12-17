# Python
Python Basics: Lists

## Learning Objectives
- Create and execute a Python file
- Write and run Python code in Visual Sudio Code
- Python concepts: 
  - Lists


## Table of Contents
- [Lists](#lists)
- [Indexing](#indexing-in-a-list)
- [Accessing Lists](#accessing_items-in-a-list)
- [Manipulating Lists](#manipulating-a-list)
- [Slicing](#slicing)
- [Built-in Methods to Manipulate a List](#built-in-methods-to-manipulate-a-list)
- [Copying list](#copying-lists)
- [List Comprehension](#list-comprehension)
- [Common Errors](#common-errors)
- [Exercises](#exercises)
- [Vocabulary](#vocabulary)



### Lists
Lists serve as a collection of ordered items, each item is separated by a comma, mutable and allows for duplicates. Python lists can comprise of different sata types: numeric values, strings and/or alphabet letters. Sqaure brackets ([]) signify lists with all of the items residing in between the open and close square bracket.

``` Python
>>> planets = ["Earth", "Mercury", "Mars"]
>>> print(planets)
['Earth', 'Mercury', 'Mars']
```
When printing out a list, the output will include the square brackets, with single quotes.


### Indexing in a List
Lists are ordered, where each item is assigned an index value, a reference to it's position within the list. Python is based on zero-based indexing, which means that the initial item of a sequence is assigned the index 0. To access a desired item from the list, write the list name followed by square brackets with the index of the item, known as bracket notation.

``` Python
>>> planets = ["Earth", "Mercury", "Mars"]
>>> print(planets[0])
Earth
>>> print(planets[2])
Mars
```
In order to access the items of the list, starting from the end, start counting by index -1.

``` Python
>>> planets = ["Earth", "Mercury", "Mars"]
>>> print(planets[-1])
Mars
```

### Accessing Items in a List
Indexing provides access to an individualized item in the list. We can manipulate the item in the list by using various methods.

``` Python
>>> planets = ["saturn", "neptune", "jupiter"]
>>> msg = f"{planets[1].title()} is the eighth and farthest-known solar planet from the Sun."
>>> print(planets)
Mars
```

### Manipulating a List
Lists are mutable and dynamic. Mutability in lists is defined as an item's ability to alter their values. Bracket notation allows for this process to take place. 

``` Python
>>> sports = ["baseball", "soccer", "volleyball"]
>>> print(sports)
['baseball', 'soccer', 'volleyball']
>>> sports[1] = 3
>>> print(sports)
['baseball', 3, 'volleyball']
```

You can append an item to a list using the function append().
``` Python
>>> my_nums = [5,10,15,20,15,25,30,10,100]
>>> my_list = []
>>> for num in my_list:
...    if num not in my_list:
...        my_list.append(num)
>>> print(my_list)
[5, 10, 15, 20, 3, 25, 30, 100]

```

#### Slicing
Removes an item from the list at a specified index. 
list_name[start:stop] or list_name[start:stop:step index]
If you leave start blank, it starts from the beginning. If you leave the stop blank, it ends counting at the end of the list. One is the default step index.
``` Python
>>> my_nums = [1, 2, 3, 4, 5]
>>> x = my_nums[1:4]
>>> print(x)
[2, 3, 4]
```
``` Python
>>> my_nums = [1, 2, 3, 4, 5]
>>> x = my_nums[1:]
>>> print(x)
[2, 3, 4, 5]
```
``` Python
>>> my_nums = [1, 2, 3, 4, 5]
>>> x = my_nums[:4:]
>>> print(x)
[1, 2, 3, 4]
```
``` Python
>>> my_nums = [1, 2, 3, 4, 5]
>>> x = my_nums[1:-1]
>>> print(x)
[2, 3, 4]
```

Python consists of built-in methods, such as the print() method that we have been using. Some of these methods permit for list manipulation.

``` Python
>>> animals = ["tiger", "bear", "lion"]
>>> print(animals)
['tiger', 'bear', 'lion']
>>> animals.append("cougar")
>>> print(animals)
['tiger', 'bear', 'lion', 'cougar']
```

#### Built-in Methods to Manipulate a List
There are a few built-in methods that can be used to manipulate a list. Here is a list of common methods used:
- append()


The built-in method append() will add the item to the end of the list without altering the order. If you would like to add an item to a particular index of the list, we use the insert method which takes 2 arguments.

``` Python
>>> animals = ["tiger", "bear", "lion"]
>>> print(animals)
['tiger', 'bear', 'lion']
>>> animals.insert(1, "wolf")
>>> print(animals)
['tiger', 'wolf', 'bear', 'lion', 'cougar']
```
Here is a list of built-in methods that can be used to manipulate a list:


pop() 
pop() removes the last item in a list by default, and it allows you to work with the item after removing it.
``` Python
>>> animals = ["tiger", "bear", "lion"]
>>> new_animals = animals.pop()
>>> print(animals)
['tiger', 'bear']
>>> print(new_animals)
lion
```
If specified, pop() can remove an item from any position is a list.
['tiger', 'bear']
``` Python
>>> animals = ["tiger", "bear", "lion"]
>>> animals.pop(0)
>>> print(animals)
['bear', 'lion']
```

reverse() 
reverses the list order.
```python
>>> animals = ["tiger", "bear", "lion"]
>>> animals.reverse()
>>> print(animals)
['lion', 'bear', 'tiger']
```

sort() 
orders the items in ascending order, items must ne the same data type.
```python
>>> alphabet = ["a", "B", "A", "z"]
>>> alphabet.sort()
>>> print(alphabet)
['A', 'B', 'a', 'z']
```
``` Python
>>> numbers = [3, 0, 100, -4, -80]
>>> number.sort()
>>> print(number)
[-80, -4, 0, 3, 100]
```

remove()
removes an item by value within the list. 
```python
>>> animals = ["tiger", "bear", "lion"]
>>> print(animals.remove('bear'))
['tiger', 'lion']
```
If the item is not within the list, a ValueError occurs.
```python
>>> animals = ["tiger", "bear", "lion"]
>>> print(animals.remove('dog'))
 line 11, in <module>
    animals.remove('dog')
ValueError: list.remove(x): x not in list
```


sorted()
returns a new list containing all items from the iterable in ascending order.
  
``` python
>>> animals = ["tiger", "bear", "lion"]
>>> print(animals.remove('bear'))
```


## Copying a list
There are several methods that allow for duplicating a list.

``` Python
>>> org_list = ["blue", "purple", "green"]
>>> cpy_list = org_list.copy()
>>> cpy_list.append("white")
>>> print(org_list)
['blue', 'purple', 'green']
>>> print(cl)
['blue', 'purple', 'green', 'white']
```
``` Python
>>> org_list = ["blue", "purple", "green"]
>>> cpy_list = list(org_list)
>>> cpy_list.append("grey")
>>> print(org_list)
['blue', 'purple', 'green']
>>> print(cl)
['blue', 'purple', 'green', 'grey']
```
``` Python
>>> org_list = ["blue", "purple", "green"]
>>> cpy_list = org_list[:]
>>> cpy_list.append("black")
>>> print(org_list)
['blue', 'purple', 'green']
>>> print(cl)
['blue', 'purple', 'green', 'black']
```


### List Comprehensions
List comprehension offers a shorter syntax when you are creating a list based on the each item in an existing list. List comprehension syntax:

[expression for element in iterable if condition]

Here we can find all of the items containing the letter e in a for loop.

``` Python
>>> animals = ["tiger", "lion", "bear", "shark", "mouse"]
>>> new_animals = []
>>> for i in animals:
...   if "e" in i:
...     new_animals.append(i)
>>> print(new_animals)
['tiger', 'bear', 'mouse']
```

With list comprehension, you can accomplish this is one line of code.
``` Python
>>> animals = ["tiger", "lion", "bear", "shark", "mouse"]
>>> new_animals = [i for i in animals if "e" in i]
>>> print(new_animals)
['tiger', 'bear', 'mouse']
```
You can append an item to another list using a for loop.



## Common Errors
If you call on an item that is not within the range of the list, an error will occur.

``` Python
>>> my_list = [1, 2, 3, 4, "five"]
>>> my_list[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

This error means that Python was unable to locate the item at the given index. To rectify that error, adjust the index number in the square brackets. If the last item in the list is desired, you can start with negative indexing.

``` Python
>>> my_list = [1, 2, 3, 4, "five"]
>>> my_list[-1]
'five'

```


### Exercise
       Ex.1: colors = ["red", "yellow", "blue"]
       Ex.2: [1, 2, 3, 4, 5, 6, 7, 8]
       Ex. 3: my_string = "I like to ride my bicycle"


1. Create a list of six items for your favorite colors.
2. Print out each item from the list you created.
3. Print out the yellow item in the provided list in Ex. 1. 
4. Capitalize the first letter in each item in Ex. 1.
5. Print out a sentence using items of the Ex.1 list using f-strings.
6. Create a blank list called cars and add 3 different types of cars to the list. 
7. Create a list of five favorite fruit. Print out the third item in a sentence using the f-string.
8. Make a list with five 2's.
9. Find the even numbers of Ex.2 using list comprehensions.
10. Convert each element in the string Ex. into a list. Convert it back into a string with spaces.




### Vocabulary
indexing
zero-based index
del
append()
insert()
pop()
reverse() 
sort()
sorted()
copy()
method
arguments
split()
join()
min()
max()
sum()
extend()



## Tips
- Run code with print() to test code. You can always print out your list to see all of the items in it:
``` python
>>> my_list = [1, 2, 3, 4, "five"]
>>> print(my_list)
[1, 2, 3, 4, 'five']

```
- use help("keywords") to get a list of available keywords


