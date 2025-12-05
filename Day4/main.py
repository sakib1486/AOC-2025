from part1 import part1
from part2 import part2

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    grid = [list(line.strip('\n')) for line in lines]
    
    print(part1(grid))
    print(part2(grid))

if __name__=="__main__":
    main()