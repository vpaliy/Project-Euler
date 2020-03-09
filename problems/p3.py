# -*- coding: future_fstrings -*-
# -*- coding: utf-8 -*-

"""
Problem Statement:
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?
"""


"""
Discussion:
  This problem brings up a new problem: generating prime numbers.
  This could be done using the fundamental theorem of arithmetic, but the algorithm would be quite slow.
"""

"""
 Naive implementation for a naive prime generator
 using the fundamental theorem of arithmetic
"""
def naive_prime_gen(limit):
  if not limit or limit < 2:
    return
  yield (2)
  primes = set([2])
  for num in xrange(3, limit):
    for prime in primes:
      if (num % prime) == 0:
        break
    else:
      primes.add(num)
      yield num


# TODO: Implement Sieve of Atkin for generating prime numbers


"""
Very naive and inefficient brute force solution.
"""
def max_prime_factor_naive(number):
  largest = None
  for prime in naive_prime_gen(number):
    if (number % prime) == 0:
      largest = max(largest, prime)
  return largest


"""
Efficient solution using division.
Basically, the gist is to divide the given number by primes until two things happen:

1) The quotient becomes a prime (in this case it is the largest prime)

2) The number gets reduced to 1 and the largest prime is the prime we used in the last division
"""
def max_prime_factor(num):
    if num < 4:
      return num
    primes = naive_prime_gen(num)
    prime = primes.next()
    while (prime**2) <= num:
        while num % prime == 0:
            num /= prime
        prime = primes.next()
    return num if num > 1 else prime


"""
>>> max_prime_factor(10)
5
>>> max_prime_factor(43)
43
"""

if __name__ == '__main__':
  number = input("Enter a number:")
  print(f'Largest prime factor of {number} is {max_prime_factor(number)}')
