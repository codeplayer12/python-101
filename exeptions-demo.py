try:
	print("hello")
except:
	print("unknown")
finally:
	print("Ending")

print(1)
print(2)
try:
	f = open("jama")
except FileNotFoundError:
	print("The file does not exist")
except Exception as e:
	print(e)
finally:
	print("Tis message")


n = 0
if n == 0:
	raise Exception("n can't be 0!")

if type(n) is not int:
	raise Exception("n must be an int!")

n = 0
assert(n !=0)
print(1/n)