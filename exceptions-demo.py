try:
	print("hello")
except:
	print("unknown")
finally:
	print("Ending")

print(1)
print(2)
	# try:
	# 	# fdfd
	# 	f = open("..help")
	# except FileNotFoundError:
	# 	print("The file does not exist")
	# except Exception as e:
	# 	print(e)
	# finally:
	# 	print("Tis message")


n = 0
if n == 0:
	raise Exception("n can't be 0!")

print(1/n)