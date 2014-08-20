#Fizz Buzz v1
n = [] #list to hold results
x = 1 #variable to count
print "Fizz buzz counting up to " 
while x <= 100:
	fizz = x % 3
	buzz = x % 5
	if fizz == 0 and buzz == 0:
		print "fizz buzz"
		n.append('fizz buzz')
	elif fizz == 0:
		print "fizz"
		n.append('fizz')
	elif buzz == 0:
		print "buzz"
		n.append('buzz')
	else:
		print x
		n.append(x)
	x += 1

