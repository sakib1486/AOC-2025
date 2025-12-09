from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(lines):
    pts = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        x,y,z = s.split(',')
        pts.append((int(x), int(y), int(z)))
    return pts

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    input = sanitize_input(lines)

    print(part1(input))
    print(part2(input))

if __name__=="__main__":
    main()