# Min and Max functions:
# min(): Returns the smallest item in an iterable or the smallest of two or more arguments.
# max(): Returns the largest item in an iterable or the largest of two or more arguments.
# works with tuple, liat, dict, numbers, strings, and other comparable data types.
# Syntax: min(iterable, *[, default=obj, key=func]) or min(arg1, arg2, *args[, key=func])

print("\nMin and Max functions:")
numbers = [10, 3, 6, 2, 8, 15]
print("Numbers List:", numbers)
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
    
# Using min and max with strings
# Strings are compared lexicographically based on Unicode values.
strings = ["apple", "banana", "cherry", "date"]
print("\nStrings List:", strings)
print("Minimum string:", min(strings))  # 'apple' has the lowest Unicode value
print("Maximum string:", max(strings))  # 'date' has the highest Unicode value

print("Min:", min("efwgavhbjKLQKOWNJEDHBS"))
print("Max:", max("efwgavhbjKLQKOWNJEDHBS"))

# Using min and max with list of strings based on length
print("\nUsing key parameter with length of strings:")
print("Strings List:", strings)
print("Shortest string:", min(strings, key=len))  # 'date' is the shortest
print("Longest string:", max(strings, key=len))   # 'banana' is the longest

# Using min and max with dictionaries
print("\nUsing min and max with dictionaries:")
sample_dict = {'apple': 5, 'banana': 2.21, 'cherry': 8}
print("Dictionary:", sample_dict)
print("\nMinimum key:", min(sample_dict))  # 'apple' 
print("Maximum key:", max(sample_dict))  # 'cherry'
print("\nMin keys:", min(sample_dict.keys()))  # 'apple'
print("Max keys:", max(sample_dict.keys()))  # 'cherry'
print("\nMinimum value:", min(sample_dict.values()))  # 2.21
print("Maximum value:", max(sample_dict.values()))  # 8
print("Min items:", min(sample_dict.items()))  # ('apple', 5)

# Using min and max with tuples
# Tuples are compared element by element.
# (x1, y1) < (x2, y2)
# If x1 < x2, then (x1, y1) < (x2, y2)
# If x1 == x2, then compare y1 and y2.

tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
print("\nUsing min and max with tuples:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Minimum tuple:", min(tuple1, tuple2))  # (1, 2, 3)
print("Maximum tuple:", max(tuple1, tuple2))  # (3, 2, 1)

# Using min and max with key and default parameters
print("\nUsing key and default parameters:")
numbers = []
print("\nNumbers List:", numbers)
print("Minimum with default:", min(numbers, default="List is empty"))  # List is empty
print("Maximum with default:", max(numbers, default="List is empty"))  # List is empty

words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print("\nWords List:", words)
print("Minimum by last character:", min(words, key=lambda x: x[-1])) # 'banana' (last char 'a')
print("Maximum by last character:", max(words, key=lambda x: x[-1])) # 'grapefruit' (last char 't')

numbers = ["10", "2", "33", "4"]    
print("\nNumbers as strings List:", numbers)
print("Minimum as integer:", min(numbers, key=int))  # '2'
print("Maximum as integer:", max(numbers, key=int))  # '33'