from timeit import default_timer as timer
my_list = ['a'] * 200000

start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)


start = timer()
my_string = " ".join(my_list)
stop = timer()
print(stop - start)