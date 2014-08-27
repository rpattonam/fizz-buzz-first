import sys
#Fizz Buzz Refactor

def isdivisible(x,y):
    if x % y == 0:
	return True
    else:
	return False

def routine(z):
    for x in range(z):
        if isdivisible(x,15) == True:
            print 'FizzBuzz'
	elif isdivisible(x,3) == True:
	    print 'Fizz'
	elif isdivisible(x,5) == True:
	    print 'Buzz'
	else:
	    print x

if len(sys.argv) > 1 :
    z = sys.argv[1]
    while not isinstance(z,int):
	z = raw_input('Error! No valid integer detected. Please enter a ceiling for the fizz buzz test ')
	try: 
	    z = int(z)
	except ValueError:
	    z = raw_input('Error! No valid integer detected. Please enter a ceiling for the fizz buzz test ')
    routine(z)
else:
    while not isinstance(z,int):
	 z = raw_input('Welcome to the Fizz Buzz Test. Please enter the number you wish to test.')
	 try:
	    z = int(z)
	 except ValueError:
	    z = raw_input('Error! You have not entered a valid integer. Please try again.')
	 routine(z)
