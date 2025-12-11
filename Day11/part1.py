def part1(devices):
    s = 'you'
    d = 'out'

    if s not in devices.keys():
        return 0
    cache = {}

    def dfs_cached(node, visited):
        if node == d:
            return 1
        if node in visited:
            return 0
        if node in cache:
            return cache[node]
        
        visited.add(node)
        total = 0

        for nb in devices.get(node, []):
            total += dfs_cached(nb, visited)
        visited.remove(node)
        cache[node] = total
        return total
    
    return dfs_cached(s, set())
