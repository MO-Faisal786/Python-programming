class BikeShop:
    def __init__(self, stock) -> None:
        self.stock = stock

    def displayBIke(self):
        print("Total Bike",self.stock)
    
    def rentForBike(self,q):
        if q <= 0:
            print("Enter a positive value or greater than zero...")
        elif q>self.stock:
            print("Enter the value (less than stock)...")
        else:
            self.stock = self.stock-q
            print("Total Price", q*100)
            print("Total Available Bikes",self.stock)

while True:
    obj = BikeShop(100)
    userChoice = int(input('''
1 Display stocks
2 Rent a Bike
3 Exit
    '''))

    if userChoice == 1:
        obj.displayBIke()
    elif userChoice == 2:
        n = int(input("Enter the Qty: "))
        obj.rentForBike(n)
    else :
        break
