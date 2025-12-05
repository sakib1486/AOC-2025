def count_rolls_p1(grid, cx, cy, steps):
  rows, cols = len(grid), len(grid[0])
  return sum(
        1
        for dr, dc in steps
        if 0 <= (nx := cx + dr) < rows and 0 <= (ny := cy + dc) < cols
        and grid[nx][ny] == '@'
    )

def part1(grid):
  cn = 0
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
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '@' and count_rolls_p1(grid=grid, cx=i, cy=j, steps=steps) < 4:
        cn += 1
  return cn