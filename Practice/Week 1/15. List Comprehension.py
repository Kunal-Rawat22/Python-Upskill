# I want 'n' value for each 'n' value in nums list
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = []

# Normal way
print("'n' values for each 'n' in nums:")
for n in nums:
    my_list.append(n)
print("Normal way:", my_list)

# Using List Comprehension
my_list_comp = [n for n in nums]
print("Using List Comprehension:", my_list_comp)


# I want 'n*n' value for each 'n' value in nums list
print("\n'n*n' values for each 'n' in nums:")
# Normal way
my_list_squared = []
for n in nums:
    my_list_squared.append(n*n)
print("Normal way:", my_list_squared)

# Using List Comprehension
# [return_value using expression for item in iterable]
my_list_squared_comp = [n*n for n in nums]
print("Using List Comprehension:", my_list_squared_comp)

# Using Map and Lambda
my_list_squared_map = list(map(lambda n: n*n, nums))        # map(function, iterable), converts each item using the function
print("Using Map and Lambda:", my_list_squared_map)

# I want 'n' value for each 'n' value in nums list if 'n' is even
print("\nEven 'n' values for each 'n' in nums:")

# Normal way
my_list_even = []
for n in nums:
    if n % 2 == 0:
        my_list_even.append(n)
print("Normal way:", my_list_even)

# Using List Comprehension
my_list_even_comp = [n for n in nums if n % 2 == 0]
print("Using List Comprehension:", my_list_even_comp)

# Using Filter and Lambda
my_list_even_filter = list(filter(lambda n: n % 2 == 0, nums))   # filter(function, iterable), filters items using the function
print("Using Filter and Lambda:", my_list_even_filter)

# I want a (letter, index) pair for each letter in 'abcd' and each number in '0123'
print("\n(letter, index) pair for each letter in 'abcd':")
my_list_letters = []

# Normal way
for letter in 'abcd':
    for i in range(4):
        my_list_letters.append((letter, i))
print("Normal way:", my_list_letters, sep='\n')

# Using List Comprehension
my_list_letters_comp = [(letter, i) for letter in 'abcd' for i in range(4)]
print("Using List Comprehension:", my_list_letters_comp, sep='\n')

# values/variables names written in left must match the ones in for loops
# The order of for loops must be same as written in left side
# The parentheses around (letter, i) are necessary to create tuple
# You can use other data structures like [letter, i] for list or {letter: i} for dictionary