from part1 import part1
from part2 import part2

# sanitize input
def sanitize_input(lines):
  fresh = set()
  given = set()
  i = 0

  for i in range(len(lines)):
    if lines[i] == '\n':
      break
    r_strt, r_end = lines[i].strip('\n').split('-')
    fresh.add((int(r_strt), int(r_end)))
  
  for j in range(i+1, len(lines)):
    given.add(int(lines[j].strip('\n')))

  return fresh, given

def main():
    fp = open('input.txt', 'r')
    lines = fp.readlines()

    fresh, given = sanitize_input(lines)
    
    print(part1(fresh, given))
    print(part2(fresh, given))

if __name__=="__main__":
    main()