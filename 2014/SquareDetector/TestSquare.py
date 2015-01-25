'''
Created on Dec 26, 2013

@author: Chris
'''
from square import hasSquare
import unittest

class TestSquare(unittest.TestCase):


    def test1(self):
        self.assertTrue(hasSquare(
                  ['..##',
                   '..##',
                   '....',
                   '....']))
    def test2(self):
        self.assertFalse(hasSquare(
                  ['..##',
                   '..##',
                   '....',
                   '#...']))
    def test3(self):
        self.assertFalse(hasSquare([
                   '#####',
                   '#####',
                   '#####',
                   '#####',
                   '.....']))
    def test4(self):
        self.assertFalse(hasSquare(
                   ['####',
                   '#..#',
                   '#..#',
                   '####']))
    def test5(self):
        self.assertTrue(hasSquare(
                  ['#####',
                   '#####',
                   '#####',
                   '#####',
                   '#####']))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()