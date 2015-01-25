__author__ = 'Chris'


def find_min_max(n):
  # Find the min
  # Find the smallest digit and move it to the front of the numbe
  def min(digit, smallest_digit):
    return digit <= smallest_digit

  def max(digit, largest_digit):
    return digit >= largest_digit
  return find_swap(n, min), find_swap(n, max)

def find_swap(n, comparison):
  start_index = 0
  list_numbers = list(str(n))
  while start_index < len(list_numbers):
    current_digit = None
    smallest_index = None
    for index in range(start_index, len(list_numbers)):
      digit = list_numbers[index]
      if start_index == 0 and digit == '0':
        continue
      if current_digit is None or comparison(digit, current_digit):
        current_digit = digit
        smallest_index = index
    if current_digit and current_digit != list_numbers[start_index]:
      list_numbers[start_index], list_numbers[smallest_index] = list_numbers[smallest_index], list_numbers[start_index]
      return int(''.join(list_numbers))
    else:
      start_index += 1
  return n


def parse_file(filename):
  f = open(filename)
  number_of_tests = int(f.readline())
  for test in range(number_of_tests):
    n = int(f.readline())
    min, max = find_min_max(n)
    print "Case #%s: %s %s" % (test+1, min, max)

if __name__ == "__main__":
  parse_file('input.txt')