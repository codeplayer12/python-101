a = 1
print(a)

a+=1
print(a)

#While loop
a = 1
while a <5:
	print(a)
	a+=1


#For loop
for i in [0,1,2,3,4,5]:
	print(i)


print("*"*10)

for i in range(5):
	print(i+1)

for i in range(3):
	for j in range(3):
		print(i,j)

print("%"*20)
for i in range(5):
	if i==2:
		break
	print(i)


print("%"*20)
for i in range(5):
	if i==2:
		continue
	print(i)

print("%"*20)
for i in range(5):
	if i==2:
		pass
	print(i)

for c in "string":
	print(c)

for key, value in {"a":2,"i":5}.items():
	print(key, value)