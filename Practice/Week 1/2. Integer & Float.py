num = 3
float_num = 3.5

print(type(num))
print(type(float_num))

# Arthmetic Operations
print('\n--- Arithmetic Operations ---')
a = 10
b = 3   
print('Addition:', a + b)            # Addition
print('Subtraction:', a - b)         # Subtraction
print('Multiplication:', a * b)      # Multiplication
print('Division:', a / b)            # Division (float result)
print('Floor Division:', a // b)     # Floor Division (integer result)
print('Modulus:', a % b)             # Modulus
print('Exponentiation:', a ** b)     # Exponentiation

# Short hand Operators
print('\n--- Shorthand Operators ---')
x = 5
print('Original x:', x)
x += 2  # x = x + 2
print('After x += 2:', x)
x -= 3  # x = x - 3
print('After x -= 3:', x)
x *= 4  # x = x * 4
print('After x *= 4:', x)
x /= 2  # x = x / 2
print('After x /= 2:', x)
x **= 2 # x = x ** 2
print('After x **= 2:', x)

# Functions with Numbers
print('\n--- Numeric Functions ---')

print('Absolute value of -7:', abs(-7))  # Absolute value
print('Round 3.6:', round(3.6))          # Rounding
print('Round 3.4578:', round(3.4578, 3))    # Rounding to 3 decimal places
print('Floor of 3.9:', int(3.9))         # Floor value

# Comparison Operators
print('\n--- Comparison Operators ---')
p = 7
q = 10
print('p == q:', p == q)   # Equal to
print('p != q:', p != q)   # Not equal to
print('p > q:', p > q)     # Greater than
print('p < q:', p < q)     # Less than
print('p >= q:', p >= q)   # Greater than or equal to
print('p <= q:', p <= q)   # Less than or equal to  

# Type Conversion
print('\n--- Type Conversion ---')
int_num = 5
float_num = 4.7
str_num = '10'  
print('Integer to Float: ', float(int_num))  # Integer to Float
print('Float to Integer:', int(float_num))   # Float to Integer
print('String to Integer:', int(str_num))    # String to Integer
print('String to Float:', float(str_num))     # String to Float
print('Integer to String:', str(int_num))    # Integer to String
print('Float to String:', str(float_num))     # Float to String 
# Note: Converting non-numeric strings to numbers will raise an error
