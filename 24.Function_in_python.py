# Function in python:
    # A Function is block of statement which can be used repetitively in a program. it saves the time of a developer. In Python concept of function is same as inother language.
        # 1: Simple Function
        # 2: Function with Arguments
        # 3: Return Type


# def myFunction():
#     print("Faisal Malik")

# myFunction()


def myFunction(num1,num2 = 5):
    # print(num1+num2)
    return num1+num2

a = int(input("Enter a number:- "))
b = int(input("Enter second number:- "))
# sum = myFunction(a,b)
sum = myFunction(a)
print(sum)