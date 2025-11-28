duplicate_nums = [1, 2, 2, 3, 4, 4, 5]

# Normal way
my_set = set()
for n in duplicate_nums:
    my_set.add(n)
print("Normal way - Set with unique values:", my_set, sep='\n', end='\n\n')

# Using Set Comprehension
my_set_comp = {n for n in duplicate_nums}
print("Using Set Comprehension:", my_set_comp, sep='\n', end='\n\n')

# Generator Expression
# I want to yield 'n*n' for each 'n' in nums

nums = [1,2,3,4,5,6,7,8,9,10]
def gen_func():
    for n in nums:
        yield n*n
gen = gen_func()
print("Using Generator Function:")
for value in gen:
    print(value, end=' ')
print('\n')

# Using Generator Expression
# [return_value using expression for item in iterable]
gen_exp = (n*n for n in nums)
print(gen_exp)
print("Using Generator Expression:")
for value in gen_exp:
    print(value, end=' ')
print()
