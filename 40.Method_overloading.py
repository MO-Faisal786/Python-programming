class ToFindArea:
    def findArea(self, a=None, b=None):
        if a != None and b != None:
            print("The area of rectengle:",(a*b))
        elif a != None :
            print("The area of Square:",(a*a))
        else :
            print("Nothing to find...")


obj = ToFindArea()
obj.findArea(2, 7)
obj.findArea(2)
obj.findArea()
