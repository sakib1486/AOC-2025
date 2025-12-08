from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(lines):
    grid = [line.rstrip('\n') for line in lines]
    start = None

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
          if col == 'S':
            start = (x, y)

    return grid, start

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    input, start = sanitize_input(lines)


    print(part1(input, start))
    print(part2(input, start))

if __name__=="__main__":
    main()