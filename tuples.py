#Tuples are mutable and cannot be changed
tuple_items = ("item1", "item2", "item3")
print (tuple_items)
print(type(tuple_items))

tuple_number = (1,23,4)
print(tuple_number)
print(type(tuple_number))

tuple_repeatv = ('COmbine!',) * 5
print(tuple_repeatv)
print(type(tuple_repeatv))
mixed_tuple = ("A",1,("A",1))
print(mixed_tuple)
print(type(mixed_tuple))

#Combining tuples
tuple_combined = tuple_items + tuple_number
print(tuple_combined)
print(type(tuple_combined))

item1,item2, item3 =tuple_items
print(item1)
print(item2)
print(item3)

print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index("item1"))

print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

print(len(tuple_items))

#Print last item
print(tuple_items[-1])
print(tuple_items[-2])

#Slicing
print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])

string1  = "I am string"
print(string1[0:4])
print(string1[:-1])