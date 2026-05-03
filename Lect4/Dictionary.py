info = {
    "name": "Dictionary",
    "description": "A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable, meaning that they can be changed after they are created.",
    "list": [2, 4, 6, 8],
    "nested_dict": {
        "key1": "value1",
    }
}

print(info)  
print(info["name"])

info["name"] = "Omkar"
print(info["name"])

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))
info.update({"name": "Chinya"})
print(info["name"])