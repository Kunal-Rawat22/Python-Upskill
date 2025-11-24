# Task 1
print("\n------------Task 1------------\n")
nums = [1,2,3,4,5]
print("Maximum in nums:", max(nums))
print("Minimum in nums:", min(nums))

# Task 2
print("\n------------Task 2------------\n")
a = [1,2,3,4]
b = [5,6,7,8]
print("a: ", a)
print("b: ", b)
a.extend(b)
print("b merged in a:", a)

# Task 3
print("\n------------Task 3------------\n")
a = [1,3,4,5,2,1,3,9,3]
print("Count of value 3:", a.count(3))

# Task 4
print("\n------------Task 4------------\n")
a = [1,3,4,5,2,1,3,9,3]
print("Original list:", a)
a.sort()
print("Sorted List:", a)

# Task 5
print("\n------------Task 5------------\n")
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)
numbers.add(6)
print("Updated set:", numbers)

# Task 6
print("\n------------Task 6------------\n")
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)
numbers.remove(3)
print("Updated Set:", numbers)

# Task 7
print("\n------------Task 7------------\n")
set1 = {1, 2, 3}    
set2 = {3, 4, 5}
print("Intersection Set1 and Set2:", set1.intersection(set2))

# Task 8
print("\n------------Task 8------------\n")
fruits = ('apple', 'banana', 'apple', 'cherry')
print("Count of 'apple':", fruits.count('apple'))

# Task 9
print("\n------------Task 9------------\n")
tuple1 = (1, 2, 3)     
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

# Task 10
print("\n------------Task 10------------\n")
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Person Dictionary:", person)
print("Age of the person:", person.get("age"))
print("City of the person:", person['city'])

# Task 11
print("\n------------Task 11------------\n")
person = {"name": "Alice", "age": 30, "city": "New York"}
person.update({"gender": "M"})
print("Updated Person Dictionary:", person)

# Task 12
print("\n------------Task 12------------\n")
person.pop('city')
print("Person Dictionary after removing city:", person)

# Task 13
print("\n------------Task 13------------\n")
dict1 = {"a": 1, "b": 2}    
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", dict3)