def part1(input):
  zero = 0
  start = 50

  for seq in input:
    s = seq.strip()
    notation, rotation = s[0], int(s[1:])

    start = (start + rotation) % 100 if notation == 'R' else (start - rotation) % 100

    zero = zero + 1 if start == 0 else zero

  return zero