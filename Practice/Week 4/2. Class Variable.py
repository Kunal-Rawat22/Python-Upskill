# class variable is similar to static variable
class Employee:
    raise_amount = 1.04
    nums_of_emp = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@company.com'
        self.pay = pay
        Employee.nums_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def raise_pay(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
emp_3 = Employee('Test','User', 50000)
emp_2 = Employee('Test2','User2', 60000)
print(emp_3.email)
print(emp_3.pay)
emp_3.raise_pay()
print(emp_3.pay)

print(Employee.raise_amount)

# It checks if the instance has the variable, if yes then returns the value 
# else it checks the class or any class it inherits from contains it
print(emp_3.raise_amount)
print(emp_3.__dict__)

Employee.raise_amount=1.05
print("Changed the raise amount from Employee Class")
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)

emp_3.raise_amount = 1.08
print("Changed the raise amount from Employee Instance")
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_3.raise_amount)

# only instance varibale amount changed because it created a new varibale for the instance
print(emp_3.__dict__)

print(Employee.nums_of_emp)
# print(Employee.__dict__)
