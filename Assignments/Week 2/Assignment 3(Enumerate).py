# Task 1
print("\n------------Task 1------------\n")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Task 2
print("\n------------Task 2------------\n")
person = {"name": "Alice", "age": 30, "city": "New York"}
for index,(key, value) in enumerate(person.items()):
    print(f"{key}: {value}")

# Task 3
print("\n------------Task 3------------\n")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits_tuple_list = []
for index, fruit in enumerate(fruits, start=1):
    if(index%2==0):
        fruits_tuple_list.append((index, fruit))
    
print("List of Tuples:", fruits_tuple_list)