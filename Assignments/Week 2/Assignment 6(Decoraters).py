# Task 1
import time
print("\n------------Task 1------------\n")
lists = []

def calculate_performance(func):
    def wrapper():
        startTime = time.time()
        print("Starting the function execution at:", startTime)
        func()
        endTime = time.time()
        print("Function execution ended at:", endTime)
        print("Total time taken in appending to the list: {:.6f} seconds".format(endTime - startTime))
    return wrapper

@calculate_performance
def func_to_append():
    for i in range(1, 1000):
        lists.append(i)


func_to_append()

# Task 2
print("\n------------Task 2------------\n")

def retry(nums_times):
    def repeated_func(func):
        def wrapper(*args, **kargs):
            for i in range (0, nums_times):
                func(*args, **kargs)
        return wrapper
    return repeated_func

@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Kunal")
    

# Task 3
print("\n------------Task 3------------\n")

def validate_positive(func):
    def wrapper(*args, **kargs):
        if(all(arg>0 for arg in args)):
            return func(*args, **kargs)
        else:
            print("Only find square root of positve numbers")
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(1))

# Task 4
print("\n------------Task 4------------\n")

cacheStruct = {}

def cache(func):
    def wrapper(*args, **kargs):
        value = cacheStruct.get(args[0])
        print(f"Data from cache: {value} for {args[0]}")
        if(value is None):
            print(f"Data for {args[0]} not found")
            value = func(*args, **kargs)
            cacheStruct[args[0]]=value
        return value
    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

print(expensive_computation(5))
print(expensive_computation(5))

# Task 5
print("\n------------Task 5------------\n")

def requires_permission(func):
    def wrapper(*args, **kargs):
        user_name = args[0]['name']
        user_permission = list(args[0]['permissions'])
        print(f'{user_name} has {user_permission} permissions')
        if(user_permission.count('admin')>0):
            func(*args, **kargs)
        else:
            print("Access Denied")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

user_list = [user1, user2, user3]
for index, user in enumerate(user_list):
    delete_user(user, index+1)
