# this is an implementation of the 'sieve' functionality using
# a generator.

def sieve():
	_primeslist = [2]
	while 1:
		start = _primeslist[-1] + 1
		while 1:
			if _is_prime(_primeslist, start):
				_primeslist.append(start)
				yield start
			start += 1
		
def _is_prime(primes, n):
    for i in primes:
        if n % i == 0:
            return False
    return True