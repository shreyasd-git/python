#multiple_inheritance - multiple parent class, single child class

class Resource1():
    Back="Oracle & Java"
    def Backend(self):
        print("Backend Task Implemented using: ",self.Back)

class Resource2():
    Front="CSS & JavaScript"
    def Frontend(self):
        print("Frontend Task Implemented using: ",self.Front)

class Teamlead(Resource1, Resource2):
    def Show(self):
        print("Dynamic Website Created...")

obj=Teamlead()
obj.Backend()
obj.Frontend()
        
        

