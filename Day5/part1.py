def part1(fresh, given):
  c = 0
  for id in given:
    for rs, rl in fresh:
      if rs <= id <= rl:
        c += 1
        break
  return c