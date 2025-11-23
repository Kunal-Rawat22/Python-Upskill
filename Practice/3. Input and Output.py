name = input("Enter your name: ") # input() function always returns a string
print(f'Hello, {name}! Welcome to the program.')

age = input("Enter your age: ")
# TypeError: can only concatenate str (not "int") to str
age_next_year = int(age) + 1  # Convert age to integer for arithmetic operation 
print(f'Next year, you will be {age_next_year} years old.')

# Taking float input
height = float(input("Enter your height in meters (e.g., 1.75): "))
# ValueError: could not convert string to float: '2.8b'
print(f'Your height is {height} meters.')
