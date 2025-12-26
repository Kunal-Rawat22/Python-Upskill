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
        self.pay = int(self.pay * self.raise_amount)

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
    
class Developer(Employee):
    raise_amount = 1.08

    def __init__(self, fname, lname, pay, prog_lang):
        # Works well with single inheritance
        super().__init__(fname, lname, pay)

        # Works well with multiple inheritance
        # Employee.__init__(self, fname, lname, pay)

        self.prog_lang = prog_lang

class Manager(Employee):
        
    def __init__(self, fname, lname, pay, employees = None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# print(help(Developer))
dev_1 = Developer('Test','User', 50000, 'Python')
dev_2 = Developer('Test2','User2', 60000, "JAVA")

print(dev_1.pay)
dev_1.raise_pay()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Jane', 'Smith', 896879, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps()

print('\nIsInstance\n')
# isInstance checks if the instance is the instance of the given class or parent class
print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))

print("\nisSubClass\n")
# isSubClass checks if class is subclass of the other given class 
print(issubclass(Developer, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))
