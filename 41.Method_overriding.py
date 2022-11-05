# Method overriding is the method having the same name with the same argument. 
# It is implemented with inheritence also ..
# It mostly used for memory reducing process

class A:
    def showData(self):
        print("Welcome to class A...")

class B(A):
    def showData(self):
        print("Welcome to class B...")

obj = B()
obj.showData()

# It is method overriding...