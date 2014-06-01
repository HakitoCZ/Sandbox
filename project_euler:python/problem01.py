#!/usr/bin/python3
'''
Problem: http://projecteuler.net/index.php?section=problems&id=1
Solution Author: HakitoCZ
Description: 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
l=[]
def result():
  for num in range(1000):
    num += 1
    if num % 3 == 0:
      l.append(num)
    if num % 5 == 0:
      l.append(num)
  return l

result()
print(sum(result()))
