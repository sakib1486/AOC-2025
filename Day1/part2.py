def part2(input):
  zero = 0
  start = 50

  for seq in input:
    s = seq.strip()
    notation, rotation = s[0], int(s[1:])

    new_start = (start + rotation) if notation == 'R' else (start - rotation)
    
    # cross 100
    c = abs(new_start // 100 - start // 100)
    zero += c

    start = new_start % 100
  
  return zero