# chr() function takes in an integer as a input convert into a charector, so it returns a charector string
# convert integer 65 to asscii charector ('A')

# num = int(input("Enter the number to check ASCII CodeS:- "))
for i in range(1,124):
    ch = chr(i)
    print(ch)


# ord() function takes in an charector as a input convert into a integer, so it returns a integer
# convert asscii unicode charector ('A') to 65
str = input("Enter the charector to check value in integer:- ")
val = ord(str)
print(val)