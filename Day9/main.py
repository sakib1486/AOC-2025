from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(lines):
    points =[]

    for l in lines:
        pts_str = l.rstrip('\n').split(',')
        points.append([int(pts_str[0]),int(pts_str[1])])

    return points

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    points = sanitize_input(lines)

    print(part1(points))
    print(part2(points))

if __name__=="__main__":
    main()