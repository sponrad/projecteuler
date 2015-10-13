'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from fractions import Fraction

#get list of fractions, nested loops
fractions = [[str(nume), str(denume)] for denume in xrange(10, 100) for nume in xrange(10, denume)]

#shorten to list of nontrivial, make a copy for comparison
def goodfractiontest(fraction):
  if "0" in fraction[0] and "0" in fraction[1]:
    return False
  #filter out fractions that do not have matching numbers to cancel out
  if not fraction[0][0] in fraction[1] or not fraction[0][1] in fraction[1]:
    return False
  originalfraction = Fraction(int(fraction[0]), int(fraction[1]))
  #weird cancellation	
  for i in range(2):
    for j in range(2):
      if int(fraction[1][j]) == int(fraction[0][i]):
        d = fraction[1].replace(fraction[1][j], "")
        n = fraction[0].replace(fraction[0][i], "")
        newfraction = Fraction(int(n)
        if  == originalfraction:
          print fraction
          return True
  return False
  
goodfractions = [fraction for fraction in fractions if goodfractiontest(fraction)]
print goodfractions

#make product for numerator and denominator
finalnume = reduce(lambda x, y: x*y, [int(fraction[0]) for fraction in goodfractions])
finaldenume = reduce(lambda x, y: x*y, [int(fraction[1]) for fraction in goodfractions])
finalfraction = Fraction(finalnume, finaldenume)
print finalfraction
#reduce