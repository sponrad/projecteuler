'''
In England the currency is made up of pound, lb, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).
It is possible to make 2 in the following way:

11 + 150p + 220p + 15p + 12p + 31p
How many different ways can 2 be made using any number of coins?
'''

#start at largest 2P, that is a solution
# 2 = 1a + 2b + 5c + 10d + 20e + 50f + 100g + 200h
#nested loop with each one counting down to zero?
#tock the ticker as each one is found

sum = 0

for h in range(2)[::-1]:
    for g in range(3)[::-1]:
        for f in range(6)[::-1]:
            for e in range(11)[::-1]:
                for d in range(21)[::-1]:
                    for c in range(51)[::-1]:
                        for b in range(101)[::-1]:
                            for a in range(201)[::-1]:
			        if (a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h) == 200:
                                    sum += 1

print sum
