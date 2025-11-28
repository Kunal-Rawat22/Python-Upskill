print("----------- Lists -----------")
# Lists are ordered, mutable collections that allow duplicate elements
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Accessing elements
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Slicing
print("Sliced List (1 to 3):", my_list[1:4])
print("Slicing with step (0 to end, step 2):", my_list[0::2])

# Modifying elements
my_list[1] = 20
print("Modified List:", my_list)

# List methods
courses = ['Math', 'Science', 'History', 'CompSci']
courses_2 = ['Drawing', 'Economics']
print("Original Courses List:", courses)
print("Second Courses List:", courses_2)

courses.insert(0, courses_2)                # Inserting a list
print("After Inserting courses_2 at index 0:", courses)
courses.remove(courses_2)                   # Removing the inserted list

courses.append('Art')                       # Appending an element
print("Append Function:", courses)

courses.insert(2, 'Biology')                # Inserting an element
print("Insert Function:", courses)

courses.remove('History')                   # Removing an element
print("Remove Function:", courses)

popped_course = courses.pop()               # Popping the last element
print("Popped Course:", popped_course)
print("List after Pop:", courses)

courses.extend(courses_2)                  # Extending the list with another list
print("Extend Function:", courses)

courses.sort()                             # Sorting the list
print("\n\nSorted Courses:", courses)

courses.reverse()                          # Reversing the list
print("Reversed Courses:", courses)

nums = [5, 2, 9, 1, 5, 6]
nums.sort(reverse=True)                    # Sorting in descending order
print("Sorted Numbers (Descending):", nums)

# All the sorting methods and functions return None and modify the list in place
newNums = sorted(nums)                                      # Using sorted() function
print("Using sorted() function:", newNums)                  # New sorted list
print("Original nums after sorted():", nums)                # Original list remains unchanged
 
print('\n\nMinimum Number:', min(nums))                         # Minimum value
print('Maximum Number:', max(nums))                         # Maximum value
print('Sum of Numbers:', sum(nums))                         # Sum of elements
print("Index of 'CompSci':", courses.index('CompSci'))      # Index of an element
print("Count of 'Math':", courses.count('Math'))            # Count of an element
print("Art in courses?", 'Art' in courses)                  # Membership test


# Iterating through a list
print("\n\nIterating through courses:")
for course in courses:
    print(course, end=", ")

print("\n\nEnumerating courses with index:")
for index, course in enumerate(courses):
    print(f"Index {index}: {course}")

print("\n\nEnumerating courses with custom start index:")
for index, course in enumerate(courses, start=3):
    print(f"Index {index}: {course}")

# Joining and Splitting lists
course_str = ', '.join(courses)
print("\n\nJoined Course String:", course_str)

split_courses = course_str.split(', ')
print("Split Courses List:", split_courses)

mixed_list = [1, 'Hello', 3.14, True]
print("\n\nMixed List:", mixed_list)