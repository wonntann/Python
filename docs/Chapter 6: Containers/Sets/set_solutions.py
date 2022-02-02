"""
# Exercise 1
my_set = set((1, 2, 2, 3, 4))
print(my_set)

"""

"""
# Exercise 2
my_set = set()
print(type(my_set))

"""

"""
# Exercise 3
this_set = set("maroon aquamarine pink violet")
print(len(this_set))

"""

"""
# Exercise 4
my_set = {"salut", "hello", "hola", "ciao", "hola"}
my_set.add("viva")
my_set.add("marhaba")
print(my_set)

"""

"""
# Exercise 5
my_set = {"salut", "hello", "hola", "ciao", "hola"}
count = (str(my_set)).split()
for item in count:
    print(item)

"""

"""
# Exercise 6
my_set = set((1, 2, 2, 3, 4))

if "l" in my_set:
    print("\"l\" is the my_set")
else:
    print("No, try searching another character")

"""

"""
# Exercise 7
my_set1 = (1, 2, 2, 3, 4)
my_set1 = set(my_set1)
my_set2 = {"salut", "hello", "hola", "ciao", "hola"}
u = my_set1.union(my_set2)
print(u)

"""


""" # Exercise 8
my_set1 = (1, 2, 2, 3, 4)
my_set1 = set(my_set1)
my_set2 = {3, 4, 5, 6, 7, 8}
diff = my_set1.symmetric_difference(my_set2)
print(diff) """