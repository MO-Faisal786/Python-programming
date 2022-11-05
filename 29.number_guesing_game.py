import random

cNumber = random.randrange(1,101)
userInput = int(input("Enter your number:- "))
if userInput > cNumber:
    print("Computer Number: ",cNumber)
    print("Your number is too high...")

elif userInput < cNumber:
    print("Computer Number: ",cNumber)
    print("Your Number is too low...")

else:
    print("Computer Number: ",cNumber)
    print("Your number is equal...")
