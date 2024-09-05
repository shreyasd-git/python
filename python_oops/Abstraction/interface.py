#Interfaces

#Abstract class with only abstract menthod is called Interface, no normal methods
#override the abstract method in child class with implementation

from abc import ABC, abstractmethod

class Shape():
    @abstractmethod
    def show(self):
        pass

class Square():
    def show(self):
        print("Square has 4 sides...")

class Circle():
    def show(self):
        print("Circe has radius/diameter...")


c=Square()
c.show()

