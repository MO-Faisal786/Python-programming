class Student:
    def __init__(self) :
        self.__name = ""
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name


    
obj = Student()
obj.setName("testing")
name = obj.getName()
print(name)