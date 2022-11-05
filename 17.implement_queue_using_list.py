l = []
while True:
    c = int(input('''
        1: Push Element 
        2: Pop first Element
        3: front Element
        4: last Element
        5: Display Element
        6: to Exit
    '''))

    if c==1:
        n = input("Enter the value:- ")
        l.append(n)
        print(l)
        
    elif c==2:
        if len(l) == 0:
            print("Empty list")
        else :
            del l[0]
            print(l)
    
    elif c==3:
        if len(l) == 0:
            print("Empty list")
        else :
            print("First value of the queue: ",l[0])
    
    elif c==4:
        if len(l) == 0:
            print("Empty list")
        else :
            print("First value of the queue: ", l[-1])

    elif c==5:
        if len(l) == 0:
            print("Empty list")
        else :
            print("All Element are ", l)
    
    elif c==6:
        break

    else :
        print("Invalid Input...")
        print("Please, Enter a valid input...")




        
























