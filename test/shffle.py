import random

# original list
items = ["apple", "banana", "cherry", "grape", "mango"]

# shuffle the list
random.shuffle(items)
print("Shuffled List:", items)
print()

# pop values one by one
while items:
    removed = items.pop(0)   # removes from the front
    print("Popped:", removed)
    print("Remaining:", items)
    print("-" * 40)
