# Task 1
print("\n------------Task 1------------\n")
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)

# Using all() to check if all numbers are positive
all_positive = all(num > 0 for num in numbers)
print("All numbers are positive:", all_positive)

# Task 2
print("\n------------Task 2------------\n")
numbers = [1, 3, 5, 7, 8]
print("Original List:", numbers)
# Using any() to check if there is any even number
any_even = any(num % 2 == 0 for num in numbers)
print("There is at least one even number:", any_even)

# Task 3
print("\n------------Task 3------------\n")
nums = [1,2,3,5,11,16,20]
print("Original List:", nums)
divisible_by_5 = any(num % 5 == 0 for num in nums)
print("Any number is divisible by 5:", divisible_by_5)