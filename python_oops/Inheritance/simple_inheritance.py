
class A():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    def Add(self):
        print("Addition is: ", self.num1 + self.num2)
    def Subtract(self):
        print("Subraction is: ", self.num1 - self.num2)

class B(A):
    def Muliply(self):
        print("Multiplication is: ", self.num1 * self.num2)
    def Div(self):
        print("Division is: ", self.num1 / self.num2)

obj=B()
obj.Add()
obj.Div()