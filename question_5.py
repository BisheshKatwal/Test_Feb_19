#Q5. Define an employee class and initialize it with name and salary.
# Now, make a classmethod that takes in a string parameter "name-2000" which creates an instance and returns the instance based on parameter.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary

    @classmethod
    def getObjFromString(cls,inp):
        name,salary= inp.split("-")
        return cls(name,salary)

    def getname(self):
        return self.name
    def getSalary(self):
        return self.salary

emp= Employee.getObjFromString("Bishesh-500")
print(emp.getname())
print(emp.getSalary())
