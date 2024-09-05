#Abstraction - Hide Implmentation 

#object cannot be created of anstract method
#python has 'abc' module for anstraction
#we use @abstractmethod decorator to define abstract menthod 
# IMPT - 
#Absraction has common action different implementation

from abc import ABC,abstractmethod

class Car(ABC):
    def show(self):
        print("A Car has 4 wheels")

    @abstractmethod
    def Speed(self):
        pass

class Ferrari(Car):
    def Speed(self):
        print("Speed is 200KM/Hr")

class Suzuki(Car):
    def Speed(self):
        print("Speed is 100KM/Hr")

obj=Suzuki()
obj.show()
obj.Speed()

#TypeError: Can't instantiate abstract class Car without an implementation for abstract method 'Speed'
obja=Car()
obja.show()