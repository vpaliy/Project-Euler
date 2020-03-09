
"""
Problem Statement: Arithmetic Derivative
  https://projecteuler.net/problem=484

  The arithmetic derivative is defined by:
    p' = 1 for any prime p
    (ab)' = a'b + ab' for all integers a, b (Leibniz rule)
  For example, 20' = 24.
"""

from functools import reduce
from operator import mul


def prime_factorization(num):
    if num < 4:
      return [num]
    primes, prime = [], 2
    while (prime**2) <= num:
        while num % prime == 0:
            num /= prime
            primes.append(prime)
        prime += 1
    if num > 1:
      primes.append(num)
    return primes


def arithmetic_derivate(num):
  primes = prime_factorization(num)
  return sum(reduce(mul,
    primes[:i] + primes[i+1:])
    for i in xrange(len(primes)
  ))


def gcd(x, y):
  if (y == 0):
    return x
  return gcd(y, x % y)


def gcd_derivative_sum(limit):
  return sum(gcd(x, arithmetic_derivate(x)) for x in xrange(1, limit))


if __name__ == '__main__':
#  n = input('Enter N = ')
  print(gcd_derivative_sum(10))
