# Task 1
print("\n------------Task 1------------\n")
name = input("Enter your name: ")
print(f"Hello, {name}! Have a nice day!.")

# Task 2
print("\n------------Task 2------------\n")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
sum = number1 + number2
multiplication = number1 * number2
division = number1 / number2
print(f"The sum of {number1} and {number2} is: {sum}")
print(f"The multiplication of {number1} and {number2} is: {multiplication}")
print(f"The division of {number1} by {number2} is: {division}")

# Task 3
print("\n------------Task 3------------\n")
list_of_names = input("Enter names separated by commas: ")
names = list_of_names.split(',')
print("You have entered the following names:", names)

# Task 4
print("\n------------Task 4------------\n")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Task 5
print("\n------------Task 5------------\n")
value = 3.14159
print(f"The value of pi up to 2 decimal places is: {value:.2f}")