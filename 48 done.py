print "start"

sum = 0
for i in xrange(1001):
	sum += i**i

sum -= 1 #to account for 0**0

print str(sum)[-10:]