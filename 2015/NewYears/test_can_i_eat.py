from unittest import TestCase
from newyears import can_i_eat
__author__ = 'Chris'


class TestCan_i_eat(TestCase):
  def test_can_i_eat(self):
    self.assertTrue(can_i_eat(
      (100, 100, 100),
      [
        (100, 100, 100)
      ]
    ))

    self.assertFalse(can_i_eat(
      (100, 100, 100),
      [
        (10, 10, 40),
        (10, 30, 10),
        (10, 60, 50)
      ]
    ))

    self.assertTrue(can_i_eat(
      (100, 100, 100),
      [
        (40, 70, 30),
        (30, 10, 40),
        (20, 20, 50),
        (10, 50, 90),
        (40, 10, 20)
      ]
    ))

    self.assertFalse(can_i_eat(
      (292, 264, 512),
      [
        (909, 302, 261),
        (705, 597, 823),
        (291, 51, 126),
        (28, 697, 57),
        (593, 31, 826),
        (311, 256, 57),
        (292, 14, 47),
        (29, 730, 716),
        (12, 529, 146),
        (768, 16, 439),
        (37, 472, 15),
        (350, 192, 34),
        (163, 468, 238),
        (69, 173, 10),
        (203, 72, 690),
        (424, 875, 213),
        (223, 593, 292),
        (151, 46, 10),
        (88, 90, 16),
        (773, 653, 711),
      ]
    ))

    self.assertTrue(can_i_eat(
      (991, 827, 352),
      [
        (29, 560, 929),
        (139, 681, 102),
        (144, 853, 10),
        (84, 729, 80),
        (218, 20, 67),
        (140, 80, 901),
        (428, 20, 500),
        (520, 970, 128),
        (422, 419, 30),
        (413, 101, 192),
        (467, 448, 501),
        (32, 939, 684),
        (34, 20, 38),
        (251, 317, 132),
        (588, 437, 10),
        (648, 21, 79),
        (391, 25, 14),
        (499, 22, 24),
        (854, 77, 361),
        (405, 25, 20)
      ]
    ))


