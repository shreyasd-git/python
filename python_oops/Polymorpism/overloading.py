#Polymorphism
#Method Overloading

class A:
    # def greet(self):
    #     print("Welcome")

    # def greet(self,firstname=''):
    #     print("Welcome",firstname)

    def greet(self,firstname='',lastname=''):
        print("Welcome",firstname,lastname)

obj=A()
obj.greet()
obj.greet('Shreyas')
obj.greet('Shreyas','Devarkar')