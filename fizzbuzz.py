## Basic FizzBuzz Test, pre actual unit
count = [1]
for x in count:
	if x <= 100:
		fizz = x % 3
		buzz = x % 5
		if fizz == 0:
			x = x + 1
			count.append('Fizz')
		elif buzz == 0:
			x = x + 1
			count.append('Buzz')
		else: 
			x = x + 1;
			count.append(x)
	else:
		print count
exit()
