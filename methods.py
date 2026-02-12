# classes and store 2 things---> data/Attributes(properties) and functions that belongs to objects


class Student:
    college_name="University"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    # methods
    def welcome(self):
        print("Welcome Students",self.name)

    def get_marks(self):
        return self.marks

s1=Student("yashveer",23)
print(s1.name)
print(s1.marks)

s1.welcome()

print(s1.get_marks())




# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    
    # method to get average og three subs
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        return sum/3
    
    @staticmethod
    def hello():
        print("Hello")
    
s1=Student("john cena",[23,24,25])
print(s1.name)
print(s1.marks)

print(s1.average())

Student.hello()
s1.hello()