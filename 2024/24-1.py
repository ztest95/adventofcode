
from collections import Counter

def solve_star_1(input: list[str]) -> int:
    
    # Parse into two lists
    a, b = [], []
    for i in range(len(input)):
        temp = input[i].split("   ")
        a.append(int(temp[0]))
        b.append(int(temp[1].strip("\n")))
    
    a.sort()
    b.sort()

    # Calculate the sum of the absolute differences
    sum_of_diff = 0
    for i in range(len(a)):
        sum_of_diff += abs(a[i] - b[i])

    return sum_of_diff


def solve_star_2(input: list[str]) -> int:
    
    # Parse into two lists
    a, b = [], []
    for i in range(len(input)):
        temp = input[i].split("   ")
        a.append(int(temp[0]))
        b.append(int(temp[1].strip("\n")))

    # Create a Counter
    # This could also be done using collections.Counter, which is much faster
    b_counter = {}
    keys_set = set() # Use set instead of dict.keys() for faster lookups
    for i in b:
        if i not in keys_set: 
            b_counter[i] = 1
            keys_set.add(i)
        else:
            b_counter[i] += 1
            
    # Calculate the similarity score
    sim_score = 0
    for ele in a:
        if ele in keys_set:
            sim_score += ele * b_counter[ele]
        else:
            sim_score += 0

    return sim_score


if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))
