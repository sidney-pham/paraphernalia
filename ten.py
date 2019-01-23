# Brute force the Make Ten train game.
# TODOS:
# - Make more efficient.
import itertools, math

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
  solutions = []
  for num_perm in set(itertools.permutations(numbers)):
    for op_perm in permute_operators(OPERATORS):
      expression = str(num_perm[0])
      for i in range(1, len(numbers)):
        expression += op_perm.pop(0) + str(num_perm[i])
      if math.isclose(eval(expression), TEN): # Account for FPE.
        solutions.append(f'{expression} = {TEN}')

  if solutions:
    print('\n'.join(set(solutions)))
  else:
    print(f'Can\'t make {TEN} with {", ".join(map(str, numbers))}!')

if __name__ == '__main__':
  numbers = input('Enter the numbers (e.g. \'2468\'): ')
  while numbers:
    make_ten([int(num) for num in numbers])
    numbers = input('Enter the numbers (e.g. \'2468\'): ')
