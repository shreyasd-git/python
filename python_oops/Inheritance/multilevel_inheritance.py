#Multilevel - single parent, multiple child classes

class Father():
    surname = "Singh"

class Son(Father):
    def Show(self):
        print("Yuvraj",self.surname)


class Gson(Son):
    def Display(self):
        print("Mandeep",self.surname)


obj=Gson()
obj.Show()
obj.Display()
