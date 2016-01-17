'''
"Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”."
'''

#print(isinstance(x/y,int))

x = 0

#multiples of 3
f = 'Fizz'
#multiples of 5
b = 'Buzz'
#multiples of both = FizzBuzz

while x <= 99:
	x += 1
	if x%15 == 0:
		print(f+b)
	elif x%3 == 0:
		print(f)
	elif x%5 == 0:
		print(b)
	else:
		print(x)