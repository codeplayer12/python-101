#Strin declaration "" /''
string1 = "I am a string"
string2 = 'I am another string'

# Multiline String
string3 = """ This is a grea string
working with me """

# Using string inside  a declare string
string4 = "I am a \" inside the string "
string5 = 'I am also a \' inside a string'
string6 = "I am another type of string'"

#escaping and new line
string7 = "\\ \x41 \x42 \x43"

#Print a string multiple times
string8 = "aaaaaaaaaa"
string9 = "a"*10

#Identifying length of a string
print(len(string8))

#Finding if string is in string
print("string" in string4)

#Check value starts with
print(string4.startswith("l"))

#Finding index
print(string4.index("string"))

#Upper Lower
print(string4.upper())
print(string4.lower())

#Trim with strip
print(string4.strip())

# Replace values
print(string4.replace("string","check"))


# Split values
print(string4.split(' '))

#encode values
print(string4.encode())
print(string4.encode("utf-8"))
string4 = "b"
print(string4.rjust(25))
print(string4.rjust(25,"X"))
print(string4.ljust(25))
print(string4.rjust(25,"X"))

#Joining two strings
print("I am " + "a string")


print(" String 4 is "+ str(len(string4)) + " characters long")

print(1+2)

print("1"+"1")

# String formarting
print("string 8 is {} characters long".format(len(string8)))

print("{} {} {}".format(len(string8),5.6,90))

print("{2} {1} {0}".format(len(string8),5.6,90))

length1 = len(string4)
print(f"string4 is {length1} characters long")

length3 = len(string3)
print(f"String 3 is {length3:.2f} long")
print(f"String 3 is {length3:x} hex")
print(f"String 3 is {length3:b} bin")
print(f"String 3 is {length3:o} oct")

print(f"String 3 is %d oct" % length1)
