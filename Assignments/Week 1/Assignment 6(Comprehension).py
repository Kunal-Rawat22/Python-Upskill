# Task 1
print("\n------------Task 1------------\n")
strings = ["1", "2", "3", "4", "5"]
nums = [int(n) for n in strings]
print("Original List:", strings)
print("Converted List:", nums)

# Task 2
print("\n------------Task 2------------\n")
numbers = [1, 5, 13, 4, 16, 7]
greater_than_10 = [n for n in numbers if n>10]
print("Original List:", numbers)
print("Converted List:", greater_than_10)

# Task 3
print("\n------------Task 3------------\n")
squared_nums = [n*n for n in range(1,6)]
print("Squared nums:", squared_nums)

# Task 4
print("\n------------Task 4------------\n")
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
flat_list = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
print("Matrix:", matrix)
print("Flat List:", flat_list)

# Task 5
print("\n------------Task 5------------\n")
keys = ['a', 'b', 'c'] 
values = [1, 2, 3]
dict_comp = { key: value for key, value in zip(keys, values)}
print("Dict:", dict_comp)

# Task 6
print("\n------------Task 6------------\n")
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
above_80 = {name: value for name, value in scores.items() if value > 80 }
print("Original dict:", scores)
print("Updated Dict:", above_80)
