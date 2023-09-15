def function1():
	print("Hello from function1")

function1()
function1()

def function2():
	return "Hello from function2"

return_from_function2 = function2()
print(return_from_function2)


def function3(s):
	print("\t{}".format(s))

function3("James".lower())

def function4(s1,s2):
	print("{} {}".format(s1,s2))

function4("Hello", "Jamie")

def function5(s1="default"):
	print("{}".format(s1))

function5()

#Function handling unknown values
def function6(s1, *more):
	print("{} {}".format(s1, " ".join([s for s in more])))

function6("John","randy", 'Alex')


def function7(**ks):
	for a in ks:
		print(a, ks[a])

function7(a="1",b="6")

# Variables declared in a function have a local scope 
# variables outside a function have a global scope and can be used in a function

# Recursion using functions
def function12(x):
	print(x)
	if x > 0:
		function12(x-1)

function12(10)