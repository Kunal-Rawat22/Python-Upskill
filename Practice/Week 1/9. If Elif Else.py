# If Elif Else Practice
temp = 20
if temp > 25:
    print("It's a hot day")
elif temp < 15:
    print("It's a cold day")
else:
    print("It's a pleasant day")
print("Enjoy your day!")

# Elif Else Challenge
age = 18
message = ""
if age < 0:
    message = "Invalid age"
elif age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Ternary Operator
age = 20
message = "Eligible" if age >= 18 else "Not Eligible" # (ternary operator) (age>=18 ? "Eligible" : "Not Eligible")
print(message)

# Logical Operators
age = 25
if age >= 18 and age <= 65:
    print("Eligible for work")
if 18 <= age <= 65:
    print("Eligible for work (short form)")
if age < 18 or age > 65:
    print("Not eligible for work")
if not(age < 18 or age > 65):
    print("Eligible for work (using not)")

# Short Circuiting
high_income = True
good_credit = False
student = False
# Short Circuiting with and, or, not i.e the evaluation stops as soon as the result is determined
if high_income and good_credit and not student:
    print("Eligible for loan")
elif high_income or good_credit or not student:
    print("Maybe eligible for loan")
else:
    print("Not eligible for loan")

# Chaining Comparison Operators
age = 30
if 18 <= age <= 65:
    print("Eligible for work (chained comparison)")
