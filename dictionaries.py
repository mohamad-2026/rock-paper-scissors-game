person = {
    "name": "Ali",
    "age": 20,
    "city": "Tehran"}


print(person)

print(person["name"])
print(person["age"])
print(person["city"])

person["age"] =21
print(person["age"])

person["job"] = "programmer"
print(person)

for key, value in person.items():
    print(f"{key}: {value}")