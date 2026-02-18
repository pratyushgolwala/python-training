fruits = {"apple", "banana", "mango","kiwi"}  


# Removing elements
fruits.remove("banana")   # Error if not found
fruits.discard("grape")   # No error if not found
popped = fruits.pop()     # Remove random item


# Set operations (very powerful!)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - all elements from both
print(set1 | set2)                    # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))               # Same

# Intersection - common elements
print(set1 & set2)                    # {4, 5}
print(set1.intersection(set2))        # Same

# Difference - in set1 but not in set2
print(set1 - set2)                    # {1, 2, 3}
print(set1.difference(set2))          # Same

# Symmetric difference - in either but not both
print(set1 ^ set2)                    # {1, 2, 3, 6, 7, 8}

# Check membership (very fast!)
print(3 in set1)                      # True
print(10 in set1)                     # False

# Practical: Remove duplicates from list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(my_list))
print(unique_list)                    # [1, 2, 3, 4]