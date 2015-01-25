import copy
import logging
from pygments import console


def can_i_eat(constraints, foods):
  sums = [sum(x) for x in zip(*foods)]
  max_value = min(constraints)
  # Fast fail if there is no way to reach the constraint
  for max_constraint, constraint in zip(sums, constraints):
    if max_constraint < constraint:
      return False
  index = constraints.index(max_value)
  food = zip(*foods)[index]
  results = list()
  results.append([Solution(food[0] == s, [0]) for s in range(max_value+1)])
  for i in range(1, len(food)):
    results.append([])
    for s in range(max_value+1):
      new_solution = Solution(False, None)
      # Carry over working Solutions
      if results[i - 1][s].is_solution:
        new_solution.is_solution = True
        new_solution.possible_solutions = results[i-1][s].get_solutions()
      # Start a new solution
      if food[i] == s:
        new_solution.is_solution = True
        new_solution.add_solution([i])
      # Add to previous solutions
      if s-food[i] > 0:
        adding_self = results[i-1][s-food[i]]
        if adding_self.is_solution:
          new_solution.is_solution = True
          for solution in adding_self.get_solutions():
            solution.append(i)
            new_solution.add_solution(solution)
      results[i].append(new_solution)


  # print results[len(food)-1][max_value]

  # Test solution
  for solution in results[len(food)-1][max_value].get_solutions():
    test = [0, 0, 0]
    for index in solution:
      for food_index in range(3):
        test[food_index] += foods[index][food_index]
    if tuple(test) == tuple(constraints):
      return True

  return False


class Solution(object):
  def __init__(self, is_solution, possible_solution):
    self.is_solution = is_solution
    self.possible_solutions = []
    if possible_solution:
      self.possible_solutions = [possible_solution]

  def copy(self):
    my_copy = Solution(self.is_solution, [])
    my_copy.possible_solutions = self.possible_solutions
    return my_copy

  def add_solution(self, solution):
    self.possible_solutions.append(list(solution))

  def is_solution(self):
    return self.is_solution

  def get_solutions(self):
    return copy.deepcopy(self.possible_solutions)

  def __repr__(self):
    if self.is_solution:
      return str(self.possible_solutions)
    else:
      return "No Solution"



def subsetSum(index, constraints, sum):
  pass


def parse_file(filename):
  f = open(filename)
  number_of_tests = int(f.readline())
  # print (number_of_tests)
  for test in range(number_of_tests):
    constraints = map(int, f.readline().split())
    number_of_foods = int(f.readline())
    foods = []
    for food in range(number_of_foods):
      foods.append(map(int, f.readline().split()))
    # print(constraints)
    # print (number_of_foods)
    # print (foods)
    result = can_i_eat(constraints, foods)
    print "Case #%s: %s" % (test+1, 'yes' if result else 'no')

if __name__ == "__main__":
  parse_file('input.txt')