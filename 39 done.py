'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import math

#generate solutions given a perimeter p
def getsolutions(p):
  solutions = []
  for i in range(1,p/2):
    a = i
    b = (p ** 2 - p * 2 * a) / (p * 2 - 2 * a)
    if b == int(b) and not a > b:
      c = math.sqrt(a ** 2 + b ** 2)
      if c == int(c):
        solutions.append([int(a), int(b), int(c)])
  return solutions

solutioncounts = [0, 0]  #number, count
for i in range(1000):
  s = getsolutions(i)
  if len(s) > solutioncounts[1]:
    solutioncounts = [i, len(s)]

print solutioncounts
print getsolutions(solutioncounts[0])