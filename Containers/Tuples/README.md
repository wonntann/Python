# Tuples

## Learning Objectives
- Create and execute a Python file
- Write and run Python code in Visual Sudio Code
- Python concepts: 
  - Tuples
  - Manipulate Tuples
  - Common Errors


## Table of Contents
- [Tuples](#tuples)
- [Actions on a Tuple](#actions-on-a-tuple)
- [Slicing](#slicing)
- [Unpacking](#slicing)
- [Common Error](#common-error)
- [Exercise](#exercise)



### Tuples
A tuple is the collection data type that is ordered, allows duplicate items, and immutable. Immutable refers to not being able to change the list after its creation. Tuples are created with parentheses, however, parentheses are not required.

``` Python
>>> my_tuple = ("Apple", 6, "New York")
```

A tuple can exist with one item, however, must include a comma at the end of the first word:
``` Python
>>> my_tuple = ("Apple",)
>>> print((type(my_tuple)))
<class 'tuple'>
```

Creating a tuple from a list:
``` Python
>>> my_tuple = (["Apple", 6, "New York"])
>>> print(my_tuple)
['Apple', 6, 'New York']
```

### Actions on a Tuple
Print out the entire tuple, line by line.
``` Python
>>> my_tuple = ("Apple", 6, "New York")
>>> for i in my_tuple:
...     print(i)
... 
Apple
6
New York
```
#### Slicing
``` Python
>>> my_tuple = ("Apple", 6, "New York", "Stars", "Libery", 23)
>>> tuple_edit = my_tuple[:3]
>>> print(tuple_edit)
('Apple', 6, 'New York')
```

#### Unpacking
You can assign a name to each item in the tuple. 
``` Python
>>> my_tuple = "Melissa", 22, "Baseball"
>>> name, age, sport = my_tuple
>>> print(name)
Melissa
>>> print(age)
28
>>> print(sport)
Baseball
```

``` Python
>>>my_foods = ("bread", "pan", "loaf", "cheese", "brie")
>>>for i in my_foods:
...    print(i)
```

The assigned elements must equal the number of items to avoid a ValueError.
``` Python
>>> my_tuple = "Melissa", 22, "Baseball"
>>> name, age, sport = my_tuple
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

In order to unpack multiple items, use an asterick (*)
``` Python
>>> my_tuples = (2, 3, 1, 4, 1, 0)
>>> a, *b, c = my_tuple
>>> print(a)
2
>>> print(c)
0
>>> print(b)
[3, 1, 4, 1]
```

### Common Error
If the index is too large:
``` Python
>>> my_tuple = ("Apple", 6, "New York")
>>> print(my_tuple[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

If you try to reassign values in a tuple:
``` Python
>>> my_tuple = ("Apple", 6, "New York")
>>> my_tuple[0] = "Banana"
>>> print(my_tuple[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```


## Exercise
  Ex.1 my_list = ["Sally", 31, "Hawaii"]
  Ex.2 my_dates = ("Monday", "Friday", "Sunday", "Tuesday")
  Ex.3 my_tuple = ("Sally", "Dan", "Geoffrey")
  Ex.4 my_letter = ("s", "d", "f", "s")

1. Create a tuple from the provided list in Ex.1
2. Iterate over a tuple in Ex.1.
3. Check if any element is inside a tuple using a conditional statement from the provided list in Ex.2.
4. Print the first index in the Ex.2, and print the last index in Ex.3.
5. Print the length of Ex.2 tuple.
6. Count how many "s" letters are in tuple Ex.4.
7. Slice from Friday to the end in Ex.2.
8. Get each separate element for Ex.3.


## Vocabulary
tuple()
count()
len()
index()
    