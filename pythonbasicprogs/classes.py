#Class example
#__init__ method -> should have self (can be any name but the frst parameter)

class Person:
    def __init__(self, name, age):
         self.name = name
         self.age = age

    def printdetail(self):
         print(f"{self.name}, {self.age}")

p1 = Person("John", 30)
p1.printdetail()

class Student(Person):
     def __init__(self, name, age, year):
          super().__init__(name, age)
          self.gradyear = year

     def printSuddetail(self):
         print(f"{self.name}, {self.age}, {self.gradyear}")

x = Student("John", 30, 2008)
x.printSuddetail()

