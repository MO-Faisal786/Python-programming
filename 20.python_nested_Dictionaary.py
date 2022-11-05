course = {
    "php":{
        'duration':"3 Months",
        'fees':15000
    },
    "java":{
        'duration':"6 Months",
        'fees':20000
    },
    "python":{
        'duration':"12 Months",
        'fees':30000
    }
    
}
# for i in course['java'].items():
#     print(i)
course['java']['fees'] = 15000

print(course['java']['fees'])

for k,v in course.items():
    print(k,v["duration"],v["fees"])