import re
from itertools import product

def parse(line):
    lights = re.search(r"\[(.*?)\]", line).group(1)
    target = [1 if c == '#' else 0 for c in lights]

    buttons = re.findall(r"\((.*?)\)", line)
    btns = []
    for b in buttons:
        if b.strip() == "":
            btns.append([])
        else:
            btns.append(list(map(int, b.split(','))))
    return target, btns


def solve_machine(target, buttons):
    n = len(target)
    m = len(buttons)

    # Build matrix A (n x m, bits)
    A = [[0] * m for _ in range(n)]
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i][j] = 1

    # Gaussian elimination over GF(2)
    row = 0
    pivots = [-1] * n
    for col in range(m):
        pivot = None
        for r in range(row, n):
            if A[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue

        # swap row and pivot
        A[row], A[pivot] = A[pivot], A[row]
        target[row], target[pivot] = target[pivot], target[row]
        pivots[row] = col

        # eliminate
        for r in range(n):
            if r != row and A[r][col] == 1:
                for c in range(col, m):
                    A[r][c] ^= A[row][c]
                target[r] ^= target[row]
        row += 1

    # find free vars
    pivot_cols = set(p for p in pivots if p != -1)
    free = [c for c in range(m) if c not in pivot_cols]

    best = None

    # brute all free var combinations
    for free_choice in product([0,1], repeat=len(free)):
        x = [0]*m
        for c, val in zip(free, free_choice):
            x[c] = val

        # back substitute
        for r in reversed(range(n)):
            pc = pivots[r]
            if pc == -1:
                if target[r] != 0:
                    break
                continue
            s = target[r]
            for c in range(pc+1, m):
                s ^= (A[r][c] & x[c])
            x[pc] = s
        else:
            # valid solution
            presses = sum(x)
            if best is None or presses < best:
                best = presses

    return best


def part1(lines):
    total = 0
    for line in lines:
        target, buttons = parse(line)
        total += solve_machine(target, buttons)
    return total

