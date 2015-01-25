from unittest import TestCase
from homework import find_primacity
__author__ = 'Chris'


class TestFind_primacity(TestCase):
  def test_find_primacity(self):
    self.assertEquals(5, find_primacity(5, 15, 2))
    self.assertEquals(7, find_primacity(2, 10, 1))
    self.assertEquals(2, find_primacity(24, 42, 3))
    self.assertEquals(0, find_primacity(1000000, 1000000, 1))
    self.assertEquals(1, find_primacity(1000000, 1000000, 2))
