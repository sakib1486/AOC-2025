def part2(input,start):
  c = 0
  row, col = len(input), len(input[0])
  memo = {}
    
  # dfs search to identify timeline with memoization
  def count_timelines(sx, sy, visited):
      # Base case: 1 timeline
      if sx >= row or sy < 0 or sy >= col:
          return 1
      # memoization check
      if (sx, sy) in memo:
          return memo[(sx, sy)]
      
      if (sx, sy) in visited:
          return 0
      
      current = input[sx][sy]
      new_visited = visited | {(sx, sy)}
      timelines = 0
        
      # If current is available, check if can go down
      if current == '.' or current == 'S':
            return count_timelines(sx + 1, sy, new_visited)
        
      # Splitter
      elif current == '^':
          left_timelines = 0
          right_timelines = 0
            
          # Left timeline branch
          if sy - 1 >= 0:
              left_timelines = count_timelines(sx + 1, sy - 1, new_visited)
            
          # Right timeline branch
          if sy + 1 < col:
              right_timelines = count_timelines(sx + 1, sy + 1, new_visited)
            
          # Total timelines is the sum of both branches
          timelines = left_timelines + right_timelines
  
      memo[(sx, sy)] = timelines
      return timelines

  return count_timelines(start[0], start[1], set())