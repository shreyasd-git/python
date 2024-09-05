#hierarchical inheritance - single parent class multiple child classes

class Father():
    surname="Curran"
    def show(self):
        print("Surname is: ", self.surname)

class Son1(Father):
    def disp(self):
        print("My name is Tom", self.surname)

class Son2(Father):
    def display(self):
        print("My name is Sam", self.surname)

s2=Son2()
s2.show()
s2.display()

s1=Son1()
s1.disp()
s1.show()