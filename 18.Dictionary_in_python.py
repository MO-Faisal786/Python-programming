from unicodedata import name


d = {
    "name":"python", 
    "fees":8000, 
    "durarion":"2 Months"
    }
# print(type(d))
# print(type(d["name"]))

# how to iterate 
for i in d:
    print(i,":",d[i])