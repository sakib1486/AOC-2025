from max_jolt import count_max_jolt

def main():
    fp = open('input.txt', 'r')
    input = fp.readlines()

    # --- Add further manipulations --- #
    
    p1_ans = count_max_jolt(input=input, k=2)
    p2_ans = count_max_jolt(input=input, k=12)

    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")

if __name__=="__main__":
    main()