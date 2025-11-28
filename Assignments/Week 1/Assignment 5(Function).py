print("\n------------Task 1------------\n")
def calculate_area(length, width=10):
    return length * width

area1 = calculate_area(5)
area2 = calculate_area(5, 20)
print(f"Area 1: {area1}")
print(f"Area 2: {area2}")

# Task 2
print("\n------------Task 2------------\n")
def factorial(n):
    if(n<0):
        return "Negative numbers do not have factorials"
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
print(factorial(5))
print(factorial(0))
print(factorial(-3))

# Task 3
print("\n------------Task 3------------\n")
def reverse_string(str):
    new_str = ''
    for char in str:
        new_str = char + new_str
    return new_str
print(reverse_string("Hello World"))


# Task 4
print("\n------------Task 4------------\n")
def sum_of_lists(list1, list2):
    sum = None
    sum = sum_of_list(list1)
    sum += sum_of_list(list2)
    return sum

def sum_of_list(list):
    sum = 0
    for num in list:
        sum+=num
    return sum

a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]

print(sum_of_lists(a,b))

# Task 5
print("\n------------Task 5------------\n")
a = [4,1,2,3,3,1,3,4,5,1,7]
def sort_and_distinct_list(list):
    list.sort()
    sorted_list = []
    unique_num = set()
    for num in list:
        if(num not in unique_num):
            unique_num.add(num)
            sorted_list.append(num)
    return sorted_list

print(sort_and_distinct_list(a))


