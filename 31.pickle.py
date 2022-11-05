# The Pickle Module implement, but powerful algorithm for serializing and de-serializing a python object structure. 
# Pickle has two main methods. The first is dump, which dumps an object and the second one is load, which loads an object from a file object

# Python pickle function 
    # dump() This function is called to serialized object hierarchy
    # load() This function is called to de-serializ a data stream 

import pickle
# dic = {
#     "name" : "faisal",
#     "class" : "12th",
#     "subject" : "maths",
#     "marks" : 45
#     }

# file = open("WriteData.txt", "wb")
# pickle.dump(dic,file)
# file.close()

file = open("WriteData.txt", "rb")
l = pickle.load(file)
print(l)
file.close()