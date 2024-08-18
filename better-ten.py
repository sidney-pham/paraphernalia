# Ram's much cleverer version.

import collections, math

OPS = [ ('+', lambda x, y: x + y)
      , ('×', lambda x, y: x * y)
      , ('-', lambda x, y: x - y)
      , ('/', lambda x, y: x / y)
      ]

def make_ten(digits):
    return _make_ten(collections.Counter(digits), len(digits) - 1, [], [])

def _make_ten(digits, ops_left, stack, out):
    if ops_left == 0:
        assert sum(digits.values()) == 0 and len(stack) == 1
        if math.isclose(stack[0], 10):
            yield tuple(out)
        return

    if len(stack) >= 2:
        right = stack.pop()
        left = stack.pop()

        for op_name, op_f in OPS:
            try:
                new = op_f(left, right)
            except:
                continue

            out.append(op_name)
            stack.append(new)
            yield from _make_ten(digits, ops_left - 1, stack, out)
            stack.pop()
            out.pop()

        stack.append(left)
        stack.append(right)

    for digit in range(10):
        if digits[digit] > 0:
            digits[digit] -= 1

            out.append(digit)
            stack.append(digit)
            yield from _make_ten(digits, ops_left, stack, out)
            stack.pop()
            out.pop()

            digits[digit] += 1

print(list(make_ten([9,5,9,1])))