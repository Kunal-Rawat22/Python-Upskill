for number in range(3):                 # Single argument means 0 to n-1
    print("Iteration number:", number)

for letter in 'Python':                 # Iterating through a string
    print("Current letter:", letter)

for number in range(1, 3):              # Two arguments means start to end-1   
    print("Number in range 1 to 2:", number)

for number in range(1, 10, 2):          # Three arguments means start to end-1 with step
    print("Odd number in range 1 to 9:", number)

successful = False
for number in range(3):
    print("Attempt:", number)
    if successful:
        print("Successful!")
        break
else:                                   # This else corresponds to the for loop
    print("Attempted 3 times and failed!")


# Iterables
# An iterable is an object that can be iterated over (looped through)
# Examples of iterables: lists, strings, tuples, sets, dictionaries, ranges, etc.

# Iterating through a list:
print("\n\nIterating through a list:")
courses = ['Math', 'CompSci', 'History']
for course in courses:
    print(course)

# Iterating through a string:
print("\n\nIterating through a string:")
course_str = "Math-CompSci-History"
for char in course_str:
    print(char)

# Iterating through a dictionary:
print("\n\nIterating through a dictionary:")
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
for key in student:
    print(key, ":", student[key])   

# Iterating through a set:
print("\n\nIterating through a set:")
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)   

# Iterating through a tuple
print("\n\nIterating through a tuple:")
point = (10, 20)
for coordinate in point:
    print(coordinate)

# Iterating through a range
print("\n\nIterating through a range:")
for number in range(5):
    print(number)