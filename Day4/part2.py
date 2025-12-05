def count_rolls_p2(grid, cx, cy, steps, cn):
  rows, cols = len(grid), len(grid[0])
  return sum(
        1
        for dr, dc in steps
        if 0 <= (nx := cx + dr) < rows and 0 <= (ny := cy + dc) < cols
        and grid[nx][ny] == '@'
    )

def part2(grid):
  cn = []
  run = True
  steps = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ]
  
  while run:
    current_indices = []
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '@' and count_rolls_p2(grid=grid, cx=i, cy=j, steps=steps, cn=cn) < 4:
          current_indices.append([i, j])
    
    # remove indices
    if len(current_indices) == 0:
      run = False
    else:
      for i, j in current_indices:
        grid[i][j] = '.'
      cn = cn + current_indices

  return len(cn)