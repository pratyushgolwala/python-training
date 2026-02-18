# Print 1 to 5
for i in range(1, 6):    # range(start, stop) - stop not included
    print(i, end = ' ')
# Output: 1, 2, 3, 4,5

# Print 0 to 4
for i in range(5):       # Same as range(0, 5)
    print(i)
# Output: 0, 1, 2, 3, 4

# Count by 2
for i in range(0, 10, 2):  # range(start, stop, step)
    print(i)
# Output: 0, 2, 4, 6, 8

# Loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for letter in "Python":
    print(letter)
    
    
    
    
    


# break - exit the loop immediately
for i in range(1, 10):
    if i == 5:
        break           # Stop when i is 5
    print(i)
# Output: 1, 2, 3, 4

# continue - skip current iteration
for i in range(1, 6):
    if i == 3:
        continue        # Skip when i is 3
    print(i)
# Output: 1, 2, 4, 5









