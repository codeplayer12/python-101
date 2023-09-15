# Defining Integer
t1_int = 1

#Defining Float
t1_float =  1.0

#Declaring Complex Numbers
t1_complex = 3.14j

#Declaring hex values
t1_hex = 0xa

#Declaring Octal value
t1_octal =  0o10

# Add Int + Hex + Oct
print(1 + 0x1 + 0o1)

#Print Absolute values
print(abs(4))
print(abs(-4))

#Rounding values
print(round(8.4))
print(round(8.5))
print(round(6.9))

#Binary values
print(bin(8))

#Hexadecimal
print(hex(8))

# Function to print the type and the value
def display_type(value):
	print(type(value))
	print(value)

display_type(t1_int)
display_type(t1_float)
display_type(t1_complex)
display_type(t1_hex)
display_type(t1_octal)
