import json
file = open("file name to be open", "mode read or write ")
# store data in a variable 
data = file.read() # you can pass the number of charector to reaad in the read function
finalData = json.loads(data)

for i in finalData:
    print(i)
    print(i['tittle'], i['name'])