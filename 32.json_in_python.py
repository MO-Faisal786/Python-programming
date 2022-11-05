# JSON(javascript object notation)
# It is mainly used for storing and transferring data between the browser and the server
# JSON is text, written with Javascript object notation.
# Python too support JSON with a built-in package called json 
import json
d = {"name":"python", "fees":15000}

j = json.dumps(d)
print(j)
print(type(j))

p = json.loads(j)
print(p)
print(type(p))