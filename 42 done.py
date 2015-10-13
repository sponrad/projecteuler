'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import csv, string

reader = csv.reader(open('words.txt'), delimiter=",")
for r in reader:
  WORDS = r

LETTERVALUES = {}
for i in range(len(string.uppercase)):
  LETTERVALUES[string.uppercase[i]] = i+1

def getlistoftrianglenumbers(n):
  trianglenumbers = [(i * (i + 1) / 2) for i in range(n)]
  return trianglenumbers

def getwordvalue(word):
  wordvalue = 0
  for w in word:
    wordvalue += LETTERVALUES[w]
  return wordvalue

print LETTERVALUES
print WORDS[28]
print getwordvalue(WORDS[28])
print getlistoftrianglenumbers(100)

TRIANGLENUMBERS = getlistoftrianglenumbers(150)
COUNT = 0
for word in WORDS:
  if getwordvalue(word) in TRIANGLENUMBERS:
    COUNT += 1

print COUNT