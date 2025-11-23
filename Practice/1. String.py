message = 'Hello World'
# Using escape character to include single quote
message2 = 'Booby\'s House'
# Using double quotes to include single quote without escape
message3 = "Booby's House"
# Multi-line string using triple quotes
message4 = """This is a multi-line string.
It can span multiple lines.
You can include 'single quotes' and "double quotes" easily."""

print(message)
print(message2)
print(message3)
print(message4)

print('\n--- String Operations ---')
# Checking the type and length of the string
print(type(message))
print(len(message))

print('\n--- String Indexing and Slicing ---')
# Accessing characters by index
print(message[0])  # First character
print(message[6])  # Seventh character
print(message[-1]) # Last character
print(message[-6]) # Sixth from last character

print('\n--- String Slicing ---')
# Slicing the string
print(message[0:5])  # Substring from index 0 to 4
print(message[6:11]) # Substring from index 6 to 10
print(message[:5])   # Substring from start to index 4
print(message[6:])   # Substring from index 6 to end

print('\n--- String Methods ---')
# String methods
print(message.upper())        # Convert to uppercase
print(message.lower())        # Convert to lowercase
print(message.count('o'))    # Count occurrences of 'o'
print(message.find('World'))  # Find index of substring 'World'
print(message.replace('World', 'Universe')) # Replace 'World' with 'Universe' and return new string instead of modifying original
print(message.split(' '))    # Split string into a list by spaces
print(message.startswith('Hello')) # Check if string starts with 'Hello'
print(message.endswith('World'))   # Check if string ends with 'World'
print(message.capitalize())   # Capitalize the first character
print(message.title())        # Title case the string
print(message.strip())       # Remove leading and trailing whitespace
print(message.isalpha())     # Check if all characters are alphabetic
print(message.isdigit())     # Check if all characters are digits
print(message.isalnum())     # Check if all characters are alphanumeric
print(message.index('o'))    # Get index of first occurrence of 'o'


print('\n--- Immutability of Strings ---')
# Demonstrating immutability
original_message = 'Hello'
modified_message = original_message.replace('H', 'J')
print('Original Message:', original_message)  # Original remains unchanged
print('Modified Message:', modified_message)  # New string with modification    

print('\n--- String Concatenation and Repetition ---')
# String concatenation
greeting = 'Hello'
name = 'Kunal'
message = greeting + ', ' + name + '. Welcome!'
message2 = f'{greeting}, {name.upper()}. Welcome!'
message3 = '{}, {}. Welcome!'.format(greeting, name.lower())

print(message3)
print(message2)
print(message)

# String repetition
repeated = 'Ha' * 3
print(repeated)

print(dir(name))  # List all methods and attributes of the string object 'name'
# print(help(str))  # Display help documentation for string class
# print(help(str.lower()))  # Display help documentation for lower method of string class