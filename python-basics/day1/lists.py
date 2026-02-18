fruits = ["apple", "banana", "mango"]


# Adding elements
fruits.append("grape")       # Add to end
fruits.insert(1, "kiwi")     # Add at index 1

# Removing elements
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove and return last item
del fruits[0]                # Delete by index

# List length
print(len(fruits))


print ([x for x in range(0,11) if x % 2 ==0]) # List comprehension to create a list of even numbers from 0 to 10