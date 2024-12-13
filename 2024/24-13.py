import re

def solve_star_1(input: list[str]) -> int:
    # solution idea:
    res = 0

    games = []
    for line_idx in range(0, len(input), 4):
        games.append(input[line_idx:line_idx+3])

    for i in range(len(games)):
        a = tuple(map(int, re.findall(r'\d+', games[i][0])))
        b = tuple(map(int, re.findall(r'\d+', games[i][1])))
        prize = tuple(map(int, re.findall(r'\d+', games[i][2])))
        games[i] = [a, b, prize]

    print('calculating tokens...')
    for i in range(len(games)):

        print("============")
        print('Game:', i+1)
        # tokens = calc(games[i][0], games[i][1], (0, 0), games[i][2])
        max_x = max(games[i][0][0], games[i][1][0])
        min_x = min(games[i][0][0], games[i][1][0])
        target = games[i][2][0]
        print(max_x, min_x, target)
        res += calc(games[i][0], games[i][1], games[i][2])


    return res

# def calc(a: tuple, b: tuple, sum: tuple, prize: tuple[int]) -> int:
#     # print(sum)
#     # return is min number of tokens to reach prize
        
#     if sum > prize:
#         return float('inf')
    
#     if sum == prize:
#         return 0
    
    
#     z = 3 + calc(a, b, (sum[0] + a[0], sum[1] + a[1]), prize)
#     y = 1 + calc(a, b, (sum[0] + b[0], sum[1] + b[1]), prize)

#     return min(y, z)

def calc(a, b, target):

    possible_as = [] # multipliers of a[0] that can be used to reach target
    possible_bs = [] # multipliers of b[0] that can be used to reach target
    for i in range(a[0], target[0], a[0]):
        # for multiples of a[0]

        if (target[0] - i) % b[0] == 0: # if the remainder is 0
            possible_as.append(i // a[0])
            possible_bs.append((target[0] - i) // b[0])

    print('possible_as:', possible_as)
    print('possible_bs:', possible_bs)
    tokens = 0
    for x, y in zip(possible_as, possible_bs):
        if x > 100 or y > 100:
            continue

        print((a[1] * x, b[1] * y))

        if (a[1] * x) + (b[1] * y) == target[1]:
            temp_tokens = (x * 3) + y
            if temp_tokens < tokens or tokens == 0:
                tokens = temp_tokens


    print(tokens)
    return tokens

def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))