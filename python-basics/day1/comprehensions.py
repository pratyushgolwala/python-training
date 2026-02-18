
# LIST COMPREHENSION - Create lists elegantly

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)            # [1, 4, 9, 16, 25]

# List comprehension (one line!)
squares = [i ** 2 for i in range(1, 6)]
print(squares)            # [1, 4, 9, 16, 25]

# Syntax: [expression for item in iterable]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)              # [0, 2, 4, 6, 8]

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)             # ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension (2D list)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)             # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# DICTIONARY COMPREHENSION


# Create dict from two lists
names = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(names, values)}
print(my_dict)            # {'a': 1, 'b': 2, 'c': 3}

# Square numbers dict
squares = {x: x**2 for x in range(1, 6)}
print(squares)            # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter dict
prices = {"apple": 100, "banana": 40, "mango": 150}
expensive = {k: v for k, v in prices.items() if v > 50}
print(expensive)          # {'apple': 100, 'mango': 150}


# SET COMPREHENSION


# Unique squares
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in nums}
print(unique_squares)     # {1, 4, 9}