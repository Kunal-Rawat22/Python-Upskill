print("\n------------Task 1------------\n")
float_int = 3.75
string_float = "123"
int_boolean = 0
boolean_string = False
print(f"1.1 Converting {float_int} to integer: {int(float_int)}")
print(f"1.2 Converting {string_float} to float: {float(string_float)}")
print(f"1.3 Converting {int_boolean} to boolean: {bool(int_boolean)}")
print(f"1.4 Converting {boolean_string} to string: {str(boolean_string)}")

print("\n------------Task 2------------\n")
x = "hello"
x_upper = x.upper()
print(f"2. Original string: {x}")
print(f"2. Uppercase string: {x_upper}")

print("\n------------Task 3------------\n")
x = 5
y = 3.14
z = x + y
print(f"3. The result of adding integer {x} and float {y} is: {z} (Type: {type(z)})")
print(f"3. z converted to integer: {int(z)} (Type: {type(int(z))})")

print("\n------------Task 4------------\n")
s = 'hello'
print(f"4. Original string: {s}")
print(f'4.1 Uppercase: {s.upper()}')
print(f"4.2 Replace: {s.replace('e', 'a')}")
print(f'4.3 startswith "he": {s.startswith("he")}')
print(f'4.4 endswith "lo": {s.endswith("lo")}')