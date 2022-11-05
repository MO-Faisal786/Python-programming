# format() Method in Python String
# The format()  Method format the specified value(s) and insert them inside the string's  placeholder.
# The placeholder is defined using brackets :{}.

text1 = "Welcome to {fname} {lname}".format(fname = "Faisal", lname = "Malik")
print(text1)
# text2 = "Welcome to {0} {1}".format("Faisal ", "Malik")
text2 = "Welcome to {1} {0}".format("Faisal ", "Malik")
print(text2)
# text3 = "Welcome to {b:>10} {a}".format(b = 45, a = 23) # to right use >
# text3 = "Welcome to {b:<10} {a}".format(b = 45, a = 23) # to left use <
text3 = "Welcome to {b:^10} {a}".format(b = 45, a = 23) #  to center use ^
print(text3)

text3 = "Welcome to {} {}".format(45, 23) 
print(text3)







