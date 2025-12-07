import math

def part2(input):
  c = 0
  for op, probs in input.items():
    if op == '+':
      for p in probs:
        c += sum(p)
    elif op == '*':
      for p in probs:
        c += math.prod(p)
  return c