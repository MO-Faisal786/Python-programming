l = []
while True:
    c = int(input('''
        1: Push Element 
        2: Pop Element
        3: Peek Element
        4: Display Element
        exit: to Exit
    '''))

    if c==1:
        n = input("Enter the value:- ")
        l.append(n)
        print(l)
        
    elif c==2:
        if len(l) == 0:
            print("Empty list")
        else :
            delElement = l.pop()
            print(delElement)
            print(l)
    
    elif c==3:
        if len(l) == 0:
            print("Empty list")
        else :
            print("Last value of the stack: ",l[-1])
    
    elif c==4:
        if len(l) == 0:
            print("Empty list")
        else :
            print("All Element are ", l)
    
    elif c==5:
        break

    else :
        print("Invalid Input...")
        print("Please, Enter a valid input...")




        
