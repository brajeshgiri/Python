from mymodule import person1, greeting
import platform
import datetime
import json

x = platform.system()
y = dir(platform)
print(x)
# print(y)
print(greeting("Brajesh"))
print("Hey, "+person1["name"])
print(datetime.datetime.now())
print(json.dumps(person1))
