from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(lines):
    devices = {}
    for l in lines:
        temp = l.rstrip('\n')
        o, d = temp.split(':')[0], temp.split(':')[1].strip().split(' ')
        devices[o] = d
    return devices

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    devices = sanitize_input(lines)

    print(part1(devices))
    print(part2(devices))

if __name__=="__main__":
    main()