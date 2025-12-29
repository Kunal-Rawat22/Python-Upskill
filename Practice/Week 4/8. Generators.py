def square_numbers(nums):
    results = []
    for num in nums:
        results.append(num*num)
    return results

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

def square_numbers_generator(nums):
    for num in nums:
        yield num*num

my_nums = square_numbers_generator([1,2,3,4,5])
print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
