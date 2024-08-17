#Polymorphism
#Method Overloading

#Parent class
class A:
    def Disp(self):
        print("This is Parent Class")

#Class B extends class A
class B(A):
    def Disp(self):
        super().Disp()
        print("This is Child Class")

obj=B()
obj.Disp()