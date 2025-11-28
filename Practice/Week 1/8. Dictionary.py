student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "CompSci"],
    1: "One"
}

print("\n\nOriginal Dictionary:", student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student.get("age"))
print("Courses:", student.get("courses"))
print("1:", student[1])

# Using get() to access the data
print("\nName:", student.get("name"))
print("Non-existing key:", student.get("grade"))
print("Non-existing key with default value:", student.get("grade", "Not Available"))

# Adding or updating key-value pairs
student["age"] = 22  # Update existing key
student["grade"] = "A"  # Add new key
print("\nDictionary after adding/updating:", student, sep="\n")

# Using update() method to add/update multiple key-value pairs
student.update({"name": "Jane Doe", "major": "Physics"})
print("\nDictionary after update():", student, sep="\n")

# Removing key-value pairs
age = student.pop("age")  # Remove key and return its value
print("\nRemoved age:", age)
print("Dictionary after pop():", student, sep="\n")

del student[1]  # Remove key-value pair using del
print("\nDictionary after del:", student, sep="\n")

# Using popitem() to remove the last inserted key-value pair
last_item = student.popitem()
print("\nRemoved last item using popitem():", last_item)
print("Dictionary after popitem():", student, sep="\n")

# Dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length of Dictionary:", len(student))

# Looping through a dictionary
print("\nLooping through keys:")
for key in student:
    print(key, ":", student[key])

print("\nLooping through key-value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Nested Dictionaries
students = {
    "student1": {"name": "John", "age": 21},
    "student2": {"name": "Jane", "age": 22}
}
print("\n\nNested Dictionary:", students, sep="\n")
print("Student1's Name:", students["student1"]["name"])
print("Student2's Age:", students["student2"]["age"])

