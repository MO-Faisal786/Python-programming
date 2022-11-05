# Polymorphism means same function name (but difference signature) being uses for different type 

# l = [10,20,30,40]
# print(len(l))

# s = "Welcome"
# print(len(s))

# class Ws:
#     def displayInfo(self, name = ''):
#         print("Welcome to faisal Place... "+name)

# obj = Ws()
# obj.displayInfo("faisal Malik")



class Ws:
    def displayInfo(self):
        print("Welcome to faisal Place... ")

class IIP(Ws):
    def displayInfo(self):
        super().displayInfo()
        print("Welcome to IIP")


obj = IIP()
obj.displayInfo()

