dict1 = {"a":1,"b":2,"c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"])
print(dict1.get("a"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1.update({"a":10})

dict1.pop("c")
print(dict1)

del dict1["b"]
print(dict1)

dict1["c"] = {"a":1,"b":2}
print(dict1)