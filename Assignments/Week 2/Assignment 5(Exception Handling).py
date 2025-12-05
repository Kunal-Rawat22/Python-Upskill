# Task 1
print("\n------------Task 1------------\n")
try:
    a = 10
    b = 0
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Task 2
print("\n------------Task 2------------\n")
my_list = [1, 2, 3]
try: 
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}")

# Task 3
print("\n------------Task 3------------\n")  
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        print(f"Result: {result}")

try:
    safe_divide(1, 0)
    safe_divide(1, "a")
finally:
    print("Execution completed.")