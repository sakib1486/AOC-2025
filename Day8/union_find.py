from typing import Tuple, List
import heapq

### HELPERS
def squared_dist(a: Tuple[int, int, int], b: Tuple) -> int:
  return sum([(a[i] - b[i])**2 for i in range(len(a))])

def k_closest_pairs_indices(points: List[Tuple[int,int,int]], k: int):
    """
    Return the k smallest unordered pairs (dist2, i, j) where i < j,
    sorted ascending by dist2. Uses heapq.nsmallest to keep memory
    proportional to number of pairs iterated (O(n^2) time, O(k) heap).
    """
    n = len(points)
    if k <= 0:
        return []

    def gen_pairs():
        # generate (dist2, i, j) for all i<j
        for i in range(n):
            pi = points[i]
            for j in range(i+1, n):
                yield (squared_dist(pi, points[j]), i, j)

    # nsmallest reads the generator and maintains a heap of size k
    # result is returned sorted ascending
    total_pairs = n*(n-1)//2
    k_actual = min(k, total_pairs)
    smallest = heapq.nsmallest(k_actual, gen_pairs(), key=lambda t: (t[0], t[1], t[2]))
    return smallest

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, a: int) -> int:
        # path compression
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def component_size(self, a: int) -> int:
        return self.size[self.find(a)]