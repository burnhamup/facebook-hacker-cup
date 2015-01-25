from unittest import TestCase
from autocomplete import auto_complete, LetterNode
__author__ = 'Chris'


class TestAuto_complete(TestCase):

  def test_letter_node(self):
    node = LetterNode('hi')
    self.assertEquals(len(node.children), 0)
    self.assertEquals(node.rest_of_text, 'hi')
    self.assertEquals(node.add_word('hello'), 2)
    self.assertEquals(len(node.children), 1)
    self.assertEquals(node.rest_of_text, None)
    self.assertIn('h', node.children)
    self.assertEquals(len(node.children['h'].children), 2)
    self.assertIn('i', node.children['h'].children)
    self.assertIn('e', node.children['h'].children)

    self.assertEquals(node.add_word('lol'), 1)
    self.assertEquals(node.add_word('hills'), 3)
    self.assertEquals(node.add_word('hill'), 4)

  def test_auto_complete(self):
    self.assertEquals(
      auto_complete([
        'hi',
        'hello',
        'lol',
        'hills',
        'hill'
      ]),
      11
    )

