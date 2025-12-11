import re
import math

def parse(line):
    # Extract joltage targets
    target = eval(re.search(r"\{(.*?)\}", line).group(0))
    target = list(map(int, target))

    # Extract button vectors
    buttons = re.findall(r"\((.*?)\)", line)
    A = []
    for b in buttons:
        vec = [0] * len(target)
        if b.strip():
            for idx in map(int, b.split(",")):
                vec[idx] += 1
        A.append(vec)
    return target, A


def min_presses(target, A):
    n = len(target)
    m = len(A)

    # Compute maximum possible presses for each button
    max_press = []
    for j in range(m):
        limits = []
        for i in range(n):
            if A[j][i] > 0:
                limits.append(target[i] // A[j][i])
        if limits:
            max_press.append(min(limits))
        else:
            max_press.append(0)

    best = math.inf
    cur = [0] * n

    def dfs(j, presses_so_far):
        nonlocal best, cur
        if presses_so_far >= best:
            return
        if j == m:
            if cur == target:
                best = presses_so_far
            return

        # Try from 0 → max_press[j]
        for times in range(max_press[j] + 1):
            # apply button j times
            for i in range(n):
                cur[i] += A[j][i] * times

            # prune if any counter exceeds target
            if all(cur[i] <= target[i] for i in range(n)):
                dfs(j + 1, presses_so_far + times)

            # undo changes
            for i in range(n):
                cur[i] -= A[j][i] * times

    dfs(0, 0)
    return best


def part2(lines):
    total = 0
    for line in lines:
        target, A = parse(line)
        total += min_presses(target, A)
    return total