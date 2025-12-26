class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # @property makes function into property attribute (Getter)
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @property
    def email(self):
        return f'{self.fname}.{self.lname}@email.com'
    
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.lname = lname
        self.fname = fname

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.lname = None
        self.fname = None
    
emp_1 = Employee('John', 'Smith')

print("\nGetter")
print(emp_1.fname)
print(emp_1.email)
print(emp_1.fullname)

print("\n\nSetter")
emp_1.fullname = "Kunal Rawat"
print(emp_1.fname)
print(emp_1.email)
print(emp_1.fullname)

print("\n\nDeleter")
del emp_1.fullname
print(emp_1.fname)
print(emp_1.email)
print(emp_1.fullname)