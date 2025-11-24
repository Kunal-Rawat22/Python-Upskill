cs_courses = {"History", "Maths", "Physics", "CompSci"}
print("\n\nOriginal Set:", cs_courses)

# Adding an element
cs_courses.add("Art")
print("\nSet after adding Art:", cs_courses)

# Removing an element
cs_courses.remove("Maths")
print("\nSet after removing Maths:", cs_courses)

# Sets are unordered collections with no duplicate elements
duplicate_set = {"History", "Maths", "Physics", "CompSci", "History"}
print("\nSet with duplicates (duplicates removed):", duplicate_set)       

art_courses = {"Art", "Design", "Photography", "CompSci", "History"}
print("\nArt Courses Set:", art_courses)

# Set Operations
print("\nUnion of CS and Art Courses:", cs_courses.union(art_courses))          # Union
print("Intersection of CS and Art Courses:", cs_courses.intersection(art_courses))  # Intersection
print("Difference (CS - Art):", cs_courses.difference(art_courses))          # Difference
print("Difference (Art - CS):", art_courses.difference(cs_courses))          # Difference
print("Symmetric Difference between CS and Art Courses:", cs_courses.symmetric_difference(art_courses))  # Symmetric Difference 

# Checking membership
print("\nIs 'Physics' in CS Courses?", "Physics" in cs_courses)
print("Is 'Maths' in CS Courses?", "Maths" in cs_courses)

# Set Comprehension
squared_numbers = {x**2 for x in range(1, 6)}
print("\nSet Comprehension (squared numbers from 1 to 5):", squared_numbers)

# Frozen Sets
frozen_set = frozenset(["History", "Maths", "Physics", "CompSci"])
print("\nFrozen Set:", frozen_set)
# frozen_set.add("Art")  # This will raise an error since frozensets are immutable
print("Is 'Maths' in Frozen Set?", "Maths" in frozen_set)

# Empty Lists, Tuples, and Sets
empty_list = []                 # list() also works
empty_tuple = ()                # tuple() also works
empty_set = set()               # Note: {} creates an empty dictionary, not a set
print("\nEmpty List:", empty_list)
print("Empty Tuple:", empty_tuple)
print("Empty Set:", empty_set)