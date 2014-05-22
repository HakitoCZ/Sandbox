#!/usr/bin/python3

from random import randint

side = randint(1,2)

if side == 1:
  a='head'
else:
  a='tail'

print('You flipped a coin and it\'s a',a)
