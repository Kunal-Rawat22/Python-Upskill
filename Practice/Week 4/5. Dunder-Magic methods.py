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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)
    
    @staticmethod
    def is_workday(day):
        if(day.weekday()==5 or day.weekday()==6):
            return False
        return True
    
    def __repr__(self):
        # Used to represention of objects for developers and is a must have because it is the fallback of __str__ (if not present) 
        return 'Employee({}, {}, {})'.format(self.fname, self.lname, self.pay)

    def __str__(self):
        # Used to represention of objects for readable format
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        # Dunder Add 
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Test','User', 50000)
emp_2 = Employee('Test2','User', 66000)

# print(emp_1)

print(repr(emp_1))
print(str(emp_1))

# print(emp_1.__str__())
# print(emp_1.__repr__())

# Dunder Add
# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))

print(emp_1 + emp_2)

# Dunder Length Function
# print(len("Test"))
# print("test".__len__())

print(len(emp_1))

