def part2(fresh, given):
  fresh_sorted = sorted(fresh, key=lambda x: x[0])
  c = 0
  cs, cl = fresh_sorted[0]

  for i in range(1, len(fresh_sorted)):
    if fresh_sorted[i][0] > cl:
      c += cl - cs + 1
      cs, cl = fresh_sorted[i]
    else:
      cl = max(cl, fresh_sorted[i][1])
  
  c += cl - cs + 1

  return c