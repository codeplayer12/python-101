import sys
print(sys.version)
print(sys.executable)
print(sys.platform)


# for line in sys.stdin:
# 	pass
# 	if line.strip() == "exit":
# 		break
# 	sys.stdout.write(">>> {}".format(line))


# for i in range(1,5):
# 	sys.stdout.write(str(i))
# 	sys.stdout.flush()


import time

for i in range(0,51):
	time.sleep(0)
	sys.stdout.write("{} [{}{}]\r".format(i*2 ,'#'*i, "."*(50-i)))
	sys.stdout.flush()
sys.stdout.write("\n")

print(sys.argv)

if len(sys.argv) != 3:
	print("[X] to run '{}' enter a username and password.".format(sys.argv[0]))
	sys.exit(5)

username = sys.argv[1]
password =sys.argv[2]

print("{} {}".format(username,password))

print(sys.path)
print(sys.modules)
sys.exit(0)