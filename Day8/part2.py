from union_find import UnionFind, squared_dist

def part2(points):
  pairs = []
  n = len(points)
  for i in range(n):
      for j in range(i+1, n):
          pairs.append((squared_dist(points[i], points[j]), i, j))
  # deterministic tie-breaker by indices
  pairs.sort(key=lambda t: (t[0], t[1], t[2]))

  uf = UnionFind(n)
  unions_made = 0
  last_pair = None

  for dist2, i, j in pairs:
    if uf.union(i, j):
      unions_made += 1
      last_pair = (i, j)
    if unions_made == n - 1:
      break
  a, b = last_pair
  return points[a][0] * points[b][0]