from unittest import TestCase
from books import find_min_max
__author__ = 'Chris'


class TestFind_min_max(TestCase):
  def test_find_min_max(self):
    self.assertEquals(find_min_max(0), (0, 0), "Minimum input")
    self.assertEquals(find_min_max(999999999), (999999999, 999999999), "Maximum Input")

    self.assertEquals(find_min_max(623885686), (263885686, 823885666))

    self.assertEquals(find_min_max(623885686), (263885686, 823885666))

    self.assertEquals(find_min_max(691917617), (191917667, 991617617))
    self.assertEquals(find_min_max(4015), (1045, 5014))

    self.assertEquals(find_min_max(31524), (13524, 51324))
    self.assertEquals(find_min_max(897), (798, 987))
    self.assertEquals(find_min_max(123), (123, 321))
    self.assertEquals(find_min_max(10), (10, 10))
    self.assertEquals(find_min_max(5), (5, 5))