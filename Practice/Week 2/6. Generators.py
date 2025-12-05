# Generators in Python are a simple and powerful tool for creating iterators. 
# They allow you to declare a function that behaves like an iterator, i.e., it can be used in a for loop. 
# Generators use the `yield` statement to produce a series of values over time, instead of returning a single value and terminating.
def square_numbers(nums):
    for num in nums:
        yield num * num

numbers = [1, 2, 3, 4, 5]
squared_gen = square_numbers(numbers)
squared_values = list(square_numbers(numbers))
print("Squared values using Generator Function:", squared_values)
print(next(squared_gen))
print("Using Generator Function to square numbers:")
for square in squared_gen:
    print(square, end=' ')
print('\n')

# Generator Expression
# [return_value using expression for item in iterable]
gen_exp = (num * num for num in numbers)
squared_values_exp = list(gen_exp)
print("Squared values using Generator Expression:", squared_values_exp)

# Advantages of Generators:
# 1. Memory Efficiency: Generators do not store all values in memory; they generate values on the fly.
# 2. Represent Infinite Stream: Generators can represent an infinite stream of data.
# 3. Composability: Generators can be composed together to form pipelines of operations.