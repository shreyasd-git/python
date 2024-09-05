#Encapsulation - 
# _a  - Protected (can be accesed outside function in same class)
# __b - Private (cannot be access even inside the function of same class)

class A():
    _a = 10
    __b = 20
    def Show(self):
        # __b = 20
        print("Can access Protected", self._a)
        print("Can access Protected", self.__b)
        # print("Can access Private", __b)


obj=A()
obj.Show()