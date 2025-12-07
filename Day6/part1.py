import math

def part1(input):
  c = 0
  for row in input:
    if row[-1] == 1:
      c += sum(row[:-1])
    else:
      c += math.prod(row[:-1])
  return c