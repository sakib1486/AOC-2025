from part1 import part1
from part2 import part2

def main():
    fp = open('input.txt', 'r')
    input_str = fp.readlines()

    input = input_str[0].strip().split(',')
    
    p1_ans = part1(input)
    p2_ans = part2(input)

    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()