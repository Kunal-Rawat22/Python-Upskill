from functools import reduce

# Lambda functions are anonymous functions that can be used to create small functions without a name.
# They are defined using the lambda keyword.
# They are also known as anonymous functions.
# They are used to create small functions without a name.
# They are used when we need to pass a function as an argument to another function.

# Syntax: lambda arguments: expression
# Example:
print("\nLambda functions:")
square = lambda x: x * x
print(square(5))

# Example:
add = lambda x, y: x + y
print(add(5, 3))

# Example:
multiply = lambda x, y: x * y
print(multiply(5, 3))


# Map function:
# The map function is used to apply a function to each item in an iterable.
# It returns a new list with the results of the function applied to each item.
# Syntax: map(function, iterable)       # iterable: list, tuple, set, dictionary    
# Example:
print("\nMap function:")
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
squared = list(map(lambda x: x ** 2, numbers))
print("Squared list:", squared)

# Filter function:
# The filter function is used to filter items in an iterable.
# Syntax: filter(function, iterable)
# Example:
print("\nFilter function:")
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Reduce function:
# The reduce function is used to reduce an iterable to a single value.
# In this function, the first argument is always the result of the previous function call known as the accumulator.
# Syntax: reduce(function, iterable)
# Example:
print("\nReduce function:")
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
# Without initializing the accumulator:
sum = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum)

# With initializing the accumulator:
sum = reduce(lambda x, y: x + y, numbers, 10)
print("Sum of numbers with initializing the accumulator:", sum)

# Using if else:
sum = reduce(lambda x, y: x + y if y % 2 == 0 else x, numbers, 0)
print("Sum of even numbers with initializing the accumulator:", sum)

# Sort function:
# The sort function is used to sort an iterable.
# It returns None and modifies the list in place.
# If reverse=True is passed, the list is sorted in descending order.
# If key=function is passed, the list is sorted by the function.
# Syntax: sort(key=function)
# Example:
print("\nSort function:")
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
numbers.sort(key=lambda x: x % 2)
print("Sorted list:", numbers)

# Using sorted() function:
# The sorted() function is used to sort an iterable.
# It returns a new list and does not modify the original list.
# Syntax: sorted(iterable, key=function)
# Example:
print("\nSorted function:")
numbers = [(1,"b","hello"),(2,"a","world"),(3,"c","python"), (4,"a","uhygfdx")]
print("Original list:", numbers)
sorted_numbers = sorted(numbers, key=lambda x: x[1])   # Sort by the second element of the tuple
print("Sorted list:", sorted_numbers)
sorted_numbers = sorted(numbers, key=lambda x: x[1], reverse=True)   # Sort by the second element of the tuple in descending order
print("Sorted list in descending order:", sorted_numbers)
sorted_numbers = sorted(numbers, key=lambda x: x[1]+x[2])   # Sort by the sum of the second and third elements of the tuple
print("Sorted list:", sorted_numbers)

