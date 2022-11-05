# s1 = str(input("Enter a String"))
# s2 = str(input("Enter a input"))
# if s1 == 'paper' or s1 == 'Paper' and s2 == "Rock" or s2 == 'rock':
#     print("The printed string is Paper...")
#
# elif s1 == 'Rock' or s1 =='rock' and s2 == 'Paper' or s2 == 'paper':
#     print("The printed string is rock")
#
# elif s1 == 'Rock' or s1 =='rock' and s2 == 'Rock' or s1 =='rock':
#     print("equel")
# else :
#     print("It is not right...")


from tkinter import *
parent = Tk()
redbutton = Button(parent, text = "Red", fg = "red")
redbutton.pack( side = LEFT)
greenbutton = Button(parent, text = "Black", fg = "black")
greenbutton.pack( side = RIGHT )
bluebutton = Button(parent, text = "Blue", fg = "blue")
bluebutton.pack( side = TOP )
blackbutton = Button(parent, text = "Green", fg = "red")
blackbutton.pack( side = BOTTOM)
parent.mainloop()