# Python
Python Basics: Doctionaries

## Learning Objectives
- Create and execute a Python file
- Write and run Python code in Visual Sudio Code
- Python concepts: 
  - Dictionaries 

### Dictionary
A dictionary is a collection data type that is unordered and mutable. It consists of a collection of key value pairs, where each value pair maps the key to its addociated value. Each pair is seperated by a comma.
my_dict = {"keys": "value", "keys": "value"}

``` Python
>>> my_dict = {"brand": "Honda", "model": "Prius","year": 1997}
>>> print(my_dict)
{'brand': 'Honda', 'model': 'Prius', 'year': 1997}
```


### Manipulating Dictionaries
You can create a new dictionary initialized from a mapping object's (key, value) pairs. Keys do no need quotation marks.

``` Python
>>> my_dict2 = dict(name="Diane", age=19, country="New Zealand")
>>> print(my_dict2)
{'name': 'Diane', 'age': 19, 'country': 'New Zealand'}
```

You can add a value pair to a dictionary.
``` Python
>>> my_dict2 = {'name': 'Diane', 'age': 19, 'country': 'New Zealand'}
>>> my_dict2["instrument"] = "guitar"
>>> print(my_dict2)
```

### Updating a dictionary

``` Python
my_dict = {"name":"Lee", "year":2013, "city": "New York"}
my_dict2 = dict(name="Tom")

my_dict.update(my_dict2)
print(my_dict)
```

### Accessing Values


``` Python
>>> value = my_dict2["name"]
>>> print(value)
Diane
```

If you enter a name that is not in the value, then this will raise an exception, KeyError.

``` Python
>>> value = my_dict2["date"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'date'
```

### Looping Through a Dictionary
``` Python
>>> nums = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> for key, value in nums.items():
...     print(key, value)
... 
one 1
two 2
three 3
four 4
```

``` Python
my_dict = dict(name="Tom", year=2018, country="USA")
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
```

## Tips
- Run code with print() to test code
- use help("keywords") to get a list of available keywords



### Exercise
       Ex.1: my_favorite = {"color":"red", "food": "tacos", "sport": "soccer"}


1. Create a dictionary for your favorite type of food, colors, and sports.
2. Add 2 value pairs to the above dictionary.
3. Remove the last value pair from the Ex.1 dictionary.
4. Create a dictionary with the following: name, Sally; day, Monday; profession, nurse
5. Find the "date" value of Ex.1 using a conditional statement.


### Vocabulary
- append()
- indexing
- zero-based index
- del
- insert()
- pop()
- dict()
- method
- arguments
- popitem() 
- update()
- get()
