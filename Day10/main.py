from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(input):
    lines = []
    lines  = [l.strip() for l in input if l.strip()]
    return lines

def main():
    fp = open('input1.txt', 'r')
    input = fp.readlines()

    lines = sanitize_input(input)

    print(part1(lines))
    print(part2(lines))

if __name__=="__main__":
    main()