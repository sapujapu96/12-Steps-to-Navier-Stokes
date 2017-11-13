def simpleadd(a,b):
	return a+b
print(simpleadd(3,4))

def fibonacci(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
	return a
print(fibonacci(7))

for n in range(10):
	print(fibonacci(n))