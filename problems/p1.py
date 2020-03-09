# -*- coding: future_fstrings -*-
# -*- coding: utf-8 -*-

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Brute force method
def multiples_sum(limit, nums=[3,5]):
  return sum(x for x in range(limit)
      if any((x % n == 0) for n in nums
    ))


"""
>>> multiples_sum(limit=10)
23
>>> multiples_sum(limit=1000)
233168
"""

if __name__ == '__main__':
  print(multiples_sum(limit=10))
