# Q3. Create a Student class and initialize it with name and roll number. Make methods to :
#       a. Display - It should display all informations of the student.
#       b. setAge - It should assign age to student
#       c. setMarks - It should assign marks to the student.

class Student:
    # age=0
    # marks=0
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


    @classmethod
    def getObjFromString(cls, inp):
        name, roll = inp.split("-")
        return cls(name, roll)

    def Display(self):
       print("The name is {} and roll no is {} ".format(self.name,self.roll))

    def setAge(self,age):
        return age
    def setMarks(self,marks):
        return marks

s=Student.getObjFromString('Bishesh-621')
s.Display()
print(s.setAge(19))
print(s.setMarks(73))


