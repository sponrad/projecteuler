'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def check(x):
	y = list(set(sorted(str(x))))
	if not y == list(set(sorted(str(2*x)))): return False
	if not y == list(set(sorted(str(3*x)))): return False
	if not y == list(set(sorted(str(4*x)))): return False
	if not y == list(set(sorted(str(5*x)))): return False
	if not y == list(set(sorted(str(6*x)))): return False 
	return True


for i in xrange(1000000):
	if check(i):
		print i

print "End: ", i
	