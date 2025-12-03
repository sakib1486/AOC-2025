def part1(input):
  jolt = 0
  for i in input:
    i = i.strip('\n').strip()
    s = len(i)
    max1 = max(i[:s-1])
    idx1 = i.index(max1)
    max2 = max(i[idx1+1:])

    jolt += int(max1+max2)

  return jolt