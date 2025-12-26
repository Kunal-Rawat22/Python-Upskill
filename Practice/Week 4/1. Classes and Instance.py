class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

############## Before INIT ################
# emp_1 = Employee()
# emp_2 = Employee()
# print(emp_1)
# print(emp_2)

# emp_1.fname = 'Kunal'
# emp_1.lname = 'Rawat'
# emp_1.email = 'kunal.rawat@tothenew.com'
# emp_1.pay = 567890

# emp_2.fname = 'qsdw'
# emp_2.lname = 'Rawdwfevat'
# emp_2.email = 'kudqwfevdnal.rawqwfat@tothenew.com'
# emp_2.pay = 56723890

# print(emp_1.email)
# print(emp_2.email)

################ After INIT ################
emp_3 = Employee('Test','User', 232334)
print(emp_3.email)

# If class instance calls class method then it doesn't need to pass down the instance in the function as parameter
print(emp_3.fullname())

# If class calls class method then it needs to pass instance in the function as parameter
print(Employee.fullname(emp_3))