''' # 1. Quickly make a list of even numbers.

my_list = list(range(1, 20))
print(my_list)

even_nums = [x for x in my_list if x % 2 == 0]
print(even_nums)
'''

""" # 2. Make a list with 100 numbers, starting with 1.
my_list = list(range(1, 100))
print(my_list)

"""

""" # 3. Add all of the numbers together in the original list of 1 - 100.
my_list = list(range(1, 100))

print(sum(my_list))

list_sum = 0
for x in my_list:
    list_sum += x
print(list_sum)
"""
