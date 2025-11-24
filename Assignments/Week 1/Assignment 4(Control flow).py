# Task 1
print("\n------------Task 1------------\n")
for i in range(3):
    num = int(input(f"Enter number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Task 2
print("\n------------Task 2------------\n")
list_str = ['civic', 'hello']
for str in list_str:
    str_reverse = ''
    for char in str:
        str_reverse = char + str_reverse
    if(str == str_reverse):
        print(f'{str} is palindrome')
    else:
        print(f'{str} is not palindrome')
        
# Task 3
print("\n------------Task 3------------\n")
n = int(input("Enter a number for fibonacci: "))
if n <= 0:
    print("Enter a positive integer")
else:
    if n == 1:
        c = 0
    elif n == 2:
        c = 1
    else:
        a, b = 0, 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        c = b

print(f"Fibbonacci for {n}:", c)

# Task 4
print("\n------------Task 4------------\n")
num = [1,2,3,4,5]
n = len(num)
pair = []
for i in range(n):
    for j in range(i+1, n):
        if(num[i]+num[j]==9):
            pair.append(num[i])
            pair.append(num[j])
print("Pairs with sum 9:", pair)

# Task 5
print("\n------------Task 5------------\n")
i=1
while i<=20:
    if i%2==0:
        print(i, "is Even")
    i+=1

# Task 6
print("\n------------Task 6------------\n")
numbers = [10, 20, 30, 40, 50]
search_for = 30
for num in numbers:
    if num == search_for:
        print(f"Found {search_for} in the list.")
        break
else:
    print(f"{search_for} not found in the list.")

# Task 7
print("\n------------Task 7------------\n")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    i+=1

# Task 8
print("\n------------Task 8------------\n")
for i in range(5):
    if i == 3:
        pass  
    print(i)

# Task 9
print("\n------------Task 9------------\n")
def type_of_day(day):
    match day.lower():
        case "saturday" | "sunday":
            return "weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "weekday"
        case _:
            return "Invalid day"
        
print(type_of_day(input("Enter a day: ")))   
