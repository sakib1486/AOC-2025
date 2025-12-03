def part2(input):
  invalid_sum = 0
  for rn in input:
    start, end = int(rn.split('-')[0]), int(rn.split('-')[1])
    for n in range(start, end+1):
      id = str(n)
      L = len(id)

      for l in range(1, L//2 + 1):
        if L % l == 0:
          part = id[:l]
          if part * (L//l) == id:
            invalid_sum += n
            break
  
  return invalid_sum