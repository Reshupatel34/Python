class Student:
    name ="karan"

# creating objects/instances  of the class
s1=Student()
print(s1)


s2=Student()
print(s2.name)



class Car:
    color="Blue"
    brand="Mercedes"

car1=Car()
print(car1.color)
print(car1.brand)



# constructor--->all classes have a function know as __init__/constructor which will get hit each time we create an object
# if we dont make our contrustor then python will hit the default contructor

class Student:
    def __init__(self):
        print(self)
        print("Adding new student in Database..")

s1=Student()  #we use () bracket with our class while creting object is to invoke the constructor
#  self-->and s1 they both are the same thing they both are pointing towards the same address
print(s1)

# <__main__.Student object at 0x0000029FEEE1EC90>
# Adding new student in Database..
# <__main__.Student object at 0x0000029FEEE1EC90>
# both the reference values are same




# we can also take multiple parameters as well inside the constructor
class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student")

# creating an object
s1=Student("karan",98)
# self.name==s1.name
# jo bhi name hum likh rahe hai vo equalts to the fullname
print(s1.name) #karan
print(s1.marks)


# Attributes-->the data stored inside the class are called attributes


# Atrributes--> 1). Class Atrribute and another is 2). object Atrribute


class Student:
    # class.att
    college_name="University"
    nmae="abc"
    def __init__(self,fullname,marks):
        self.name=fullname  #obj.att>class.att
        self.marks=marks
        print("Added to the databases")

# object
s1=Student("karan",94)
# obj.att
print(s1.name)
print(s1.marks)
# class.att
print(Student.college_name)
# we can also access it by obj.att
print(s1.college_name)
# obj.att>class.att
print(s1.name) # it will print karan and not abc even tho we have the same claa.att as obj.att in our class because of the precedence

