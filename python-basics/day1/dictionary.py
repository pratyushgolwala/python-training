# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "marks": 85
}

# Accessing values
print(student["name"])       # Rahul
print(student.get("age"))    # 22
print(student.get("email", "Not found"))  # Not found (default if key missing)

# Adding/Modifying
student["email"] = "rahul@email.com"  # Add new key
student["age"] = 23                    # Update existing key

# Removing
del student["marks"]                   # Delete by key
removed = student.pop("email")         # Remove and return value

# Checking keys
if "name" in student:
    print("Name exists!")

# Looping through dictionary
for key in student:
    print(key, ":", student[key])

# Or using .items()
for key, value in student.items():
    print(f"{key} = {value}")

# Get all keys and values
print(student.keys())    # dict_keys(['name', 'age', 'course'])
print(student.values())  # dict_values(['Rahul', 23, 'Python'])