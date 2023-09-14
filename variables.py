name = "jtom"
print("My name is " + name)

name_length = 4
print(f"My favorite number is {name_length}")

print(type(name)) # to print the type of the variable
print(type(name_length))

name_length = "4"
print(type(name_length))

#Type conversion should be done with the correct datatype
name_length = int("4")
print(type(name_length))

#Case sensitive
name_length = 4
Name_length = 5
print(name_length)
print(Name_length)

# List datatype
name_list =['jamie','rob','bob']
print(type(name_list))

print(name_list)
#Unpack a list
name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)


#Tuple datatype
name_tuple =('jamie','rob','bob')
print(type(name_tuple))

print(name_tuple)
# Dictionary Datatype
name_dictionary = {"check":3,"range":10}
print(type(name_dictionary))

print(name_dictionary)
#Boolean type
name_boolean = True
print(type(name_boolean))
print(name_boolean)

# Range
name_range =range(6)
print(type(name_range))
print(name_range)
#Bytes
name_bytes = b"test"
print(type(name_bytes))

print(name_bytes)