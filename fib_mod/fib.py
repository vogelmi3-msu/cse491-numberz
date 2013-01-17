# this is an implementation of the 'fib' functionality using a module.
print "fib 1"
last_1 = 1
last_2 = 1

print "fib 2"
def next():
	print "fib 3"
	global last_1, last_2
	print "fib 4"
	next_fib = last_1 + last_2
	last_1, last_2 = last_2, next_fib
	return next_fib
