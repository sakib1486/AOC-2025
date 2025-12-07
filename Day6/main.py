from part1 import part1
from part2 import part2

# helper for part1 sanitize
def convert(value):
    if value == '+':
        return 1
    if value == '*':
        return 2
    return int(value)

# helper for part2 sanitize
def check_blank_column(column):
    return all(value == ' ' for value in column)

# sanitize input
def sanitize_input(lines, part):

  if part == 1:
    grid = []
    for line in lines:
      grid.append(list(line.strip().split()))

    lines_t = list(map(list, zip(*grid)))

    problems = [[convert(x) for x in row] for row in lines_t]

    return problems
  else:
    grid = [line.rstrip('\n') for line in lines]

    
    max_len = max(len(row) for row in grid)
    grid = [r.ljust(max_len) for r in grid]

    # transpose grid
    columns = list(map(list, zip(*grid)))

    problems = {}
    co = None
    so_far = [] 

    for col in columns:
        if check_blank_column(col):
            # end of current problem
            if so_far and co:
                so_far = list(reversed(so_far))  # read numbers right-to-left
                if co not in problems:
                    problems[co] = [so_far]
                else:
                    problems[co].append(so_far)
            co = None
            so_far = []
        elif col[-1] in ('*', '+'):
            co = col[-1]
            num_str = ''.join(ch for ch in col[:-1] if ch != ' ')
            if num_str:
                so_far.append(int(num_str))
        else:
            num_str = ''.join(ch for ch in col if ch != ' ')
            if num_str:
                so_far.append(int(num_str))

    # handle last problem
    if so_far and co:
        so_far = list(reversed(so_far))
        if co not in problems:
            problems[co] = [so_far]
        else:
            problems[co].append(so_far)

    return problems


def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    input_part1 = sanitize_input(lines, 1)
    input_part2 = sanitize_input(lines, 2)


    print(part1(input_part1))
    print(part2(input_part2))

if __name__=="__main__":
    main()