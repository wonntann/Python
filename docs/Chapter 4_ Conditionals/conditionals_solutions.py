"""
# 1. Making an order of an ice cream sundae with your choice of toppings:

requested_toppings = input("What toppings would you like: marshmellows, almonds, or/and syrup\n")

if 'marshmellows' in requested_toppings:
    print("Adding marshmellow.")
if 'almonds' in requested_toppings:
    print("Adding almonds.")
if 'syrup' in requested_toppings:
    print("Adding syrup.")

print("\nHere is your sundae!") 
"""


"""
# 2. Print out 2 conditions that one is True and the other one is False.

dog_breed = ["cocker spaniel", "chow chow", "beagle", "german shepard"]
if "cocker spaniel" in dog_breed:
    print("You have a beautiful dog!")
if "chow chow" not in dog_breed:
    print("Nope, it is.") 
"""


"""
# 3. Create a blank list, use a conditional statement to add to the blank list and check if not empty.

requested_toppings = []
toppings = input("List one topping for your frozen yogurt or leave blank for no topping:\n")
requested_toppings.append(toppings)

if toppings not in requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}.")
    print("\nFinished making your frozen yogurt!")
else:
    print("You are getting plain frozen yogurt")
"""
