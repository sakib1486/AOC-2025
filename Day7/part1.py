def part1(input,start):
  c = 0
  row, col = len(input), len(input[0])
  visited = set()
    
  # dfs search to identify count
  def split_beam(input, c, sx, sy, row, col):
      # Base case: reached bottom of grid
      if sx >= row or sy < 0 or sy >= col:
          return c
      if (sx, sy) in visited:
          return c
      
      visited.add((sx, sy))
      current = input[sx][sy]
        
      # If current is available, check if can go down
      if current == '.' or current == 'S':
          if sx + 1 < row:
              c = split_beam(input, c, sx + 1, sy, row, col)
          return c
        
      # Splitter
      elif current == '^':
          c += 1
          if sx + 1 < row:
              if sy - 1 >= 0:
                  c = split_beam(input, c, sx + 1, sy - 1, row, col)
              if sy + 1 < col:
                  c = split_beam(input, c, sx + 1, sy + 1, row, col)
          return c
      return c
    
  c = split_beam(input, c, start[0], start[1], row, col)
  return c