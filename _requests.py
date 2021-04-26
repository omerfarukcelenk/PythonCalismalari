import requests
import json


result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
print(result[0]["title"])
print(result[0])

for i in result:
    print(i["title"])


print(type(result))
