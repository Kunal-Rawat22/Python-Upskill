# Task 1
print("\n------------Task 1------------\n")
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print("Original List:", numbers)
print("Max :", max(numbers))
print("Min :", min(numbers))

# Task 2
print("\n------------Task 2------------\n")
setn = {5, 10, 3, 15, 2, 20}
print("Original Set :", setn)
print("Min: ", min(setn))
print("Max: ", max(setn))

# Task 3
print("\n------------Task 3------------\n")
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
print("Original List:", words)
output = (min(words, key=len),max(words, key=len))
print("Output (Shortest and Longest words):", output)