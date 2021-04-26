# dict
import json

person_string = '{"name":"ali","languages":["python","C#"]}'

# JSON string to dic
"""
result = json.loads(person_string)
result = result["name"]
result = result["languages"]
"""
"""
with open("person.json") as f:
    data = json.load(f)
    print(data["name"])
    print(data["languages"])
"""

person_dict = {
    "name":"ali",
    "languages":["python","c#"]
}

# Dict to json string
"""
result = json.dumps(person_dict)
print(result)
print(type(result))

"""
"""
with open("person.json","w") as file:
    json.dump(person_dict, file) 

"""    

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent= 4, sort_keys= True)  
print(person_dict)
print(result)