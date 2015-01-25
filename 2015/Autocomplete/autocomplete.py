

class LetterNode(object):
  def __init__(self, word):
    self.children = {}
    self.rest_of_text = word

  def add_word(self, word):
    if len(word) == 0:
      return 0

    first_letter = word[0]
    if first_letter in self.children:
      node = self.children[first_letter]
      return node.add_word(word[1:]) + 1
    else:
      if self.rest_of_text == word:
        return 1
      else:
        if self.rest_of_text:
          my_next_letter = self.rest_of_text[0]
          node = LetterNode(self.rest_of_text[1:])
          self.children[my_next_letter] = node
          self.rest_of_text = None
          if first_letter == my_next_letter:
            return node.add_word(word[1:]) + 1
        self.children[first_letter] = LetterNode(word[1:])
        return 1


def auto_complete(words):
  letter_tree = LetterNode(words[0])
  results = 1
  for word in words[1:]:
    results += letter_tree.add_word(word)
  return results

def parse_file(filename):
  f = open(filename)
  number_of_tests = int(f.readline())
  for test in range(number_of_tests):
    number_of_words = int(f.readline())
    letter_tree = LetterNode(f.readline().strip())
    results = 1
    for i in range(1, number_of_words):
      word = f.readline().strip()
      results += letter_tree.add_word(word)
    print "Case #%s: %s" % (test+1, results)

if __name__ == "__main__":
  parse_file('input.txt')

