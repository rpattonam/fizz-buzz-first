import sys
#Fizz Buzz v2
n = [] #list to hold results
x = 1 #variable to start count
try:
	y = sys.argv[1]
	while True:
		try:
			y = int(y)
			break
		except:
			print "The data you provided is not valid!"
			break
except:
	y = raw_input('Please enter a ceiling for the fizz buzz test ')
finally:
	while True:
		try: 
			y = int(y)
			break
		except:
			y = raw_input("Please enter a whole number integer ")
	print "Fizz buzz counting up to {}".format(y) 
	while x <= y:
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

