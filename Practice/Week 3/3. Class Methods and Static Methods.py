# Methods that receive the class itself (cls) as the first parameter, not an instance.
# Methods that don't access class or instance data. They're just utilities.
# Useful for helper functions related to the class
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

emp_1 = Employee('Test','User', 50000)
emp_2 = Employee('Test2','User2', 60000)

Employee.set_raise_amount(1.07)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)

emp_3 = Employee.from_string('Kunal-Rawat-45678')

print(emp_3.email)
import datetime
my_date = datetime.date(2016, 7, 8)
print(Employee.is_workday(my_date))