class Student:
    __name = "Faisal Malik"
    def __init__(self) -> None:
        print(self.__name)
        self.__displayInfo()
    def __displayInfo(self):
        print("Welcome to Faisal Place...")

obj = Student()