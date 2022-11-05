'''
  Data types in Python:
    Numeric:
        Integers
        float
        Complex NUmber
                                                    python debide into two type of ata type
  Sequence Type                                         1: Mutable data type
            String                                          -> List
            List                                            -> Dictionary
            Touple                                          -> Byte array
                                                        2: Immutable Data Type
      Dictionary                                            -> Int
  set                                                       -> Float
                                                            -> Complex
                                                            -> Touple
                                                            -> Set
'''
# 1: Number
a = 5
print(type(a))

a = 2.00
print(type(a))

a = 2j
print(type(a))


# 2: String:
#     -> A string is a collection of one or more than one charecters put in a single quote, double quote or trple quote.
#     -> Multi line string can be denoted using triple quote, that is '''String ''' or """String"""

s = "This is a string"
print(s)

s = 'This is single qoute String'
print(s)

s = '''This is a triple 
quote String'''
print(s)

s = """This is second 
        triple qoute"""
print(s)

s = "10"
print(type(s))

# List:
#     -> List is an ordered sequence of items
#     -> It is one of the most used data type in python and is very flexible
#       -> []
a = [1,2,4, "Apple"]
print(a, type(a))
a[len(a)-1] = "Banana"
print(a)


# Toupe:
#     -> Toupe is an ordered sequence of items same as a list.
#     -> It is defined within parentheses() where items are separated by commas.
t = (3, 'apple', 5j)
# t[1] = 'banana'
print(t, type(t))
t = (6)
print(t, type(t))

# Dictionary:
#     -> Dictionary is an unordered collection of key-value paires.
#     -> In Python, Dictionaries are defined within braces {} with each item being a pair in the form key:value
dic = {1:"Apple", "name":"faisal Malik", "courseName":"Pyhton"}
print(dic, type(dic))
print(dic[1])
print(dic["courseName"])


# Set:
#     -> A set is a unoredered colection of items .
#     -> Every set element is unique (no duplicate) and must be immutable (cannot be changed)
#     -> {}
mySet = {1,2 ,3}
print(mySet)

# Data types are compeleted























