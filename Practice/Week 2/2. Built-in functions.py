# All and any functions:
# all(): Returns True if all elements in the iterable are true (or if the iterable is empty).
# any(): Returns True if any element of the iterable is true. If the iterable is empty, returns False.
print("\nAll and Any functions:")
bool_list = [True, True, False, True]
nums = [1, 2, 3, 0, 5]
string = ["", "Hello", "World"]

# Testing all() and any() with Boolean list
print("Boolean List:", bool_list)
print("All elements are True:", all(bool_list))
print("At least one element is True:", any(bool_list))

# Testing all() and any() with Numeric list
print("\nNumeric List:", nums)
print("All elements are non-zero:", all(nums))
print("At least one element is non-zero:", any(nums))

# Testing all() and any() with String list
print("\nString List:", string)
print("All strings are non-empty:", all(string))
print("At least one string is non-empty:", any(string))

# Useful when used with logical conditions
ages = [22, 25, 18, 30, 27]
print("\nAges List:", ages)
print("All ages are 18 or older:", all(age >= 18 for age in ages))
print("At least one age is 25 or older:", any(age >= 25 for age in ages))

# Numpy example
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
print("\nNumpy Array:\n", array)
print("All elements in the array are non-zero:", np.all(array))
print("At least one element in the array is non-zero:", np.any(array))

power_level_list = np.array([9000, 8500, 7800, 9200])
print("\nPower Level List:", power_level_list)
print("All power levels exceed 8000:", np.all(power_level_list > 8000))
print("At least one power level exceeds 9000:", np.any(power_level_list > 9000))

# Enumerate function:
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# Syntax: enumerate(iterable, start=0)
print("\nEnumerate function:")
fruits = ['apple', 'banana', 'cherry']

print("Fruits List:", fruits)
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("\nEnumerate with custom start index:")
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")