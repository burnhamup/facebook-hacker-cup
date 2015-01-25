'''
Created on Feb 2, 2013

@author: Chris
'''

mod = 1000000007
from gmpy2 import comb
import random

def card(n,k,a):
    result = 0
    a.sort(reverse=True)
    x = 0
    for i in range(n-1,k-2,-1):
        result += (a[x] * comb(i,k-1)) % mod
        x+=1
    return result % mod
    


def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        (n,k) = map(int,f.readline().split())
        a = map(int,f.readline().split())
        result = card(n,k,a)
        print "Case #"+str(test+1) + ": " + str(result)

parseFile('input.txt')
#print card(10,1,[1,2,3,4,5,6,7,8,9,10])


