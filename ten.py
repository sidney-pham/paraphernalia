# Brute force the Make Ten train game.
import itertools, functools

TEN = 10
OPERATORS = ['+', '-', '*', '/']

def permute_operators(operators):
  res = []
  def f(arr, done):
    if done == len(operators) - 1:
      return res.append(arr[:])
    for operator in operators:
      arr[done] = operator
      f(arr, done + 1)
  f([None] * (len(operators) - 1), 0)
  return res

def make_ten(numbers):
  assert len(numbers) > 0
  for num_perm in itertools.permutations(numbers):
    for op_perm in permute_operators(OPERATORS):
      expression = str(numbers[0])
      for i in range(1, len(numbers)):
        expression += op_perm.pop(0) + str(num_perm[i])
      if eval(expression) == TEN:
        print(f'{expression} = {TEN}')

make_ten([3, 5, 8, 5])
