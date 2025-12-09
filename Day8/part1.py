from collections import Counter
from union_find import UnionFind, k_closest_pairs_indices

def part1(points, k_pairs = 1000):
  n = len(points)
  uf = UnionFind(n)

  pairs = k_closest_pairs_indices(points, k_pairs)

  # pairs are sorted ascending by dist squared
  # iterate in order and union when they link different components
  for dist2, i, j in pairs:
      uf.union(i, j)

  # compute sizes of each root
  roots = [uf.find(i) for i in range(n)]
  cnt = Counter()
  for r in roots:
      cnt[r] += 1
  sizes = sorted(cnt.values(), reverse=True)
  # if less than 3 components, multiply what's available (spec says three largest)
  top3 = sizes[:3] + [1]*max(0, 3-len(sizes))
  prod = 1
  for s in top3:
      prod *= s
  return prod