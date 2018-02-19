#Q2. Create a class Circle which has a class variable PI with value=22/7.
# Make two methods getArea and getCircumference inside this Circle class.
#  Which when invoked returns area and circumference of each ciecle instances.

class Circle:
    PI= 22/7
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        return Circle.PI* self.radius**2

    def getCircumference(self):
        return 2* self.PI * self.radius


cir= Circle(5)
print("The area is : {}".format(cir.getArea()))
print("The circumference is : {}".format(cir.getCircumference()))
