import re

def solve_star_1(input: list[str]) -> int:
    
    all_matches = []
    for line_index in  range(len(input)):
        regex = r"mul\((\d*\,\d*)\)"
        matches = re.findall(regex, input[line_index])

        all_matches = all_matches + matches
    
    muls = []
    for ele in all_matches:
        a, b = map(int, ele.split(","))
        muls.append(a * b)

    res = 0
    for i in range(len(muls)):
        res += muls[i]

    return res


def solve_star_2(input: list[str]) -> int:
    all_matches = []
    for line_index in  range(len(input)):
        regex = r"mul\(\d*\,\d*\)|do\(\)|don\'t\(\)"
        matches = re.findall(regex, input[line_index])
        # print(matches)
        all_matches = all_matches + matches
    
    muls = []
    do = True
    for ele in all_matches:
        if ele == "do()":
            do = True
            continue
        elif ele == "don't()":
            do = False
            continue
        elif ele.startswith("mul") and do:
            q = ele.strip("mul(").strip(")")
            a, b = map(int, q.split(","))
            muls.append(a * b)

    res = 0
    for i in range(len(muls)):
        res += muls[i]

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))


# https://regex101.com/
# https://www.geeksforgeeks.org/write-regular-expressions/