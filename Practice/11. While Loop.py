# While Loop = A control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
num = int(input("Enter a positive integer b/w (1-10):"))

while num < 1 or num > 10:
    print("Invalid input! Please try again.")
    num = int(input("Enter a positive integer b/w (1-10):"))
print(f"You entered: {num}")