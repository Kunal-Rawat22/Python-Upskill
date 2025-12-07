# Task 1
print("\n------------Task 1------------\n") 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Alice", 30)
print("Person instance:", p.name, p.age)


# Task 2
print("\n------------Task 2------------\n") 
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

acct = BankAccount("001122", "Bob", 100.0)
print("Initial balance:", acct.check_balance())
acct.deposit(50)
print("After deposit:", acct.check_balance())
try:
    acct.withdraw(200)
except ValueError as e:
    print("Withdraw error:", e)
acct.withdraw(50)
print("After withdraw:", acct.check_balance())


# Task 3
print("\n------------Task 3------------\n") 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, s):
        parts = [p.strip() for p in s.split(",", 1)]
        if len(parts) != 2:
            raise ValueError("String must be 'Title, Author'")
        return cls(parts[0], parts[1])

book = Book.from_string("Python Programming, John Doe")
print("Book:", book.title, "by", book.author)


# Task 4
print("\n------------Task 4------------\n") 
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement sound()")

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()
print("Dog sound:", dog.sound())
print("Cat sound:", cat.sound())


# Task 5
print("\n------------Task 5------------\n") 
class Flyer:
    def fly(self):
        return "I can fly"

class Swimmer:
    def swim(self):
        return "I can swim"

class Duck(Flyer, Swimmer):
    def sound(self):
        return "Quack"

donald = Duck()
print("Duck sound:", donald.sound())
print(donald.fly())
print(donald.swim())
