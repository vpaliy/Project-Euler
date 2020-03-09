# -*- coding: future_fstrings -*-
# -*- coding: utf-8 -*-

"""
Problem Statement:
  Finite Sequence Generator
  https://projecteuler.net/problem=693
Status: Unsolved
"""


# Brute force implementation
def finite_seq_gen(x, y):
  # x and y are positive and x > y
  assert (x > 0) and (y > 0) and (x > y)
  # initial setup
  a, z = y, x
  while (a > 1):
    yield a
    a, z =pow(a, 2) % z, z + 1
  yield a


def g_max(x):
  largest = None
  for y in xrange(x-1,1, -1):
    a, z = y, x
    while (a > 1):
      a, z = pow(a, 2) % z, z + 1
    largest = max(z-x+1, largest)
  return largest


# Naive brute force implementation 
def f_max(n):
  largest = None
  for x in range(2, n+1):
    largest = g_max(x)
  return largest


if __name__ == '__main__':
  x = input('Enter X = ')
  y = input('Enter Y = ')
  seq = list(finite_seq_gen(x, y))

  print(','.join(map(str, (a for a in seq))))
  print(f'Length: {len(seq)}')
  print(f'Largest for X = {x} is {g_max(x)}')

  n = input('Enter N = ')
  print(f'Largest for N = {n} is {f_max(n)}')
