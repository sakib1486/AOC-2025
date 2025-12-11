def part2(devices):
    start = 'svr'
    dest = 'out'
    required_all = {'dac', 'fft'}

    if start not in devices:
        return 0

    # cache: (node, frozenset(remaining_required)) -> count
    cache = {}

    def dfs(node, visited, remaining_required):
        if node == dest:
            return 1 if not remaining_required else 0

        if node in visited:
            return 0

        key = (node, frozenset(remaining_required))
        if key in cache:
            return cache[key]

        visited.add(node)
        total = 0
        for nb in devices.get(node, []):
            if nb in visited:
                continue
            # update remaining_required
            new_remaining = remaining_required - {nb} if nb in remaining_required else remaining_required
            total += dfs(nb, visited, new_remaining)
        visited.remove(node)

        cache[key] = total
        return total

    initial_remaining = required_all - ({start} if start in required_all else set())
    return dfs(start, set(), initial_remaining)
