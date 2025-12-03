# Task 1
print("\n------------Task 1------------\n")
a = [1, 2, 3, 4]
print("Original List:", a)
double_value = list(map(lambda x:x*2, a))
print("Doubled Value List:", double_value)

# Task 2
print("\n------------Task 2------------\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x:x%2 == 0, numbers))
print("Original List:", numbers)
print("Even Numbers List:", even_numbers)

# Task 3
print("\n------------Task 3------------\n")
from functools import reduce
words = ["apple", "banana", "cherry", "date"]
longest_word = str(reduce(lambda x,y: x if len(x)>=len(y) else y, words))
print("Original List:", words)
print("Longest Word:", longest_word)

# Task 4
print("\n------------Task 4------------\n")
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_and_round = list(map(lambda x: round(x**2, 1), my_floats))
print("Original List:", my_floats)
print("Squared and Rounded Off List:", square_and_round)

# Task 5
print("\n------------Task 5------------\n")
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filtered_names = list(filter(lambda x: len(x)<=7, my_names))
print("Original List:", my_names)
print("Filtered List:", filtered_names)

# Task 6
print("\n------------Task 6------------\n")
nums = [1, 2, 3, 4, 5]
sum = int(reduce(lambda x, y: x+y, nums))
print("Original List:", nums)
print("Sum of List:", sum)