'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

numers.txt
'''


reader = open("numbers.txt", "rb")
numbers = [l for l in reader]

sum = 0
for n in numbers:
  sum += int(n)

print str(sum)[0:10]


##5537376230