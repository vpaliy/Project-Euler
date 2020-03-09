# -*- coding: future_fstrings -*-
# -*- coding: utf-8 -*-

"""
Problem Statement:

  The sum of the squares of the first ten natural numbers is 385
  The square of the sum of the first ten natural numbers is 3025
  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

"""
Simple algebra
"""

def get_sq_sums(n):
  v, l = n*(n+1) // 2, n*(n+1)*(2*n+6) // 2
  return (v, l)


if __name__ == '__main__':
  n = input('Enter N = ')
  v, l = get_sq_sums(n)
  print(f"({'+'.join(map(str, (x for x in xrange(1, n+1))))})² = {pow(v, 2)}")
  print(f'Difference:{pow(v, 2)-l}')
