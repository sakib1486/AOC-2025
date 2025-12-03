def count_max_jolt(input: list, k: int) -> int:
  jolt = 0
  for i in input:
    i = i.strip('\n').strip()
    s = len(i)

    stk = []
    drop = s - k

    for d in i:
      while drop and stk and stk[-1] < d:
        stk.pop()
        drop -= 1
      stk.append(d)
    
    max_num = ''.join(stk[:k])
    jolt += int(max_num)
    
  return jolt