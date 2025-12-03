def part1(input):
  invalid_sum = 0
  for rn in input:
    start, end = int(rn.split('-')[0]), int(rn.split('-')[1])
    for n in range(start, end+1):
      id = str(n)
      mid = len(id)//2
      if id[:mid] == id[mid:]:
        invalid_sum += n
  
  return invalid_sum