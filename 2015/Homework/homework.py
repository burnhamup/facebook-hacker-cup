__author__ = 'Chris'


def find_primacity(a, b, k):
  results = 0
  for i in range(a, b+1):
    number_of_factors = len(set(fac(i)))
    if number_of_factors == k:
      results += 1
  return results

from math import floor, sqrt
try:
    long
except NameError:
    long = int

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]


def parse_file(filename):
  f = open(filename)
  number_of_tests = int(f.readline())
  for test in range(number_of_tests):
    a, b, k = map(int, f.readline().split())
    result = find_primacity(a,b,k)
    print "Case #%s: %s" % (test+1, result)

if __name__ == "__main__":
  parse_file('input.txt')