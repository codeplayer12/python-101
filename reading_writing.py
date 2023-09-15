#Reading Files
f = open('top-100.txt')
print(f)

# Read Text
f = open('top-100.txt', 'rt')
print(f)

print(f.read())
print(f.readlines())

print(f.readlines())
f.seek(0)
print(f.readlines())

f.seek(0)

for line in f:
	print(line.strip())

f.close()
#Write mode
f = open("test.txt","w")
f.write("test line!")
f.write("test line two!")
f.close()

# Append mode
f = open("test.txt","a")
f.write("test line!")
f.write("test line two!")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

with open('rockyou.txt', encoding='latin-1') as f:
	for line in f:
		pass
