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
    for i in range(0, target[0]+a[0], a[0]):
        # for multiples of a[0]

        if (target[0] - i) % b[0] == 0: # if the remainder is 0
            print(i, (target[0] - i) // b[0])
            possible_as.append(i // a[0])
            possible_bs.append((target[0] - i) // b[0])

    print('possible_as:', possible_as)
    print('possible_bs:', possible_bs)
    tokens = 0
    # a[0] = button a's x
    # b[0] = button b's x
    print(target)
    for x, y in zip(possible_as, possible_bs):
        if x > 100 or y > 100:
            continue
        print((x * a[0] + y * b[0], x * a[1] + y * b[1]))

        if (a[1] * x) + (b[1] * y) == target[1]:
            temp_tokens = (x * 3) + y
            if temp_tokens < tokens or tokens == 0:
                tokens = temp_tokens


    print(tokens)
    return tokens

def solve_star_2(input: list[str]) -> int:
    # solution idea

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
        print("=====================================")
        print('Game:', i+1)
        print(games[i])
        res += calc2(games[i][0], games[i][1], games[i][2])

    print("res:", res)  
    return res

def calc2(a, b, target):

    possible_as = [] # multipliers of a[0] that can be used to reach target
    possible_bs = [] # multipliers of b[0] that can be used to reach target
    x_ww = 10000000000000 // a[0] # get the number of times a[0] can be multiplied to reach num
    x_rem = 10000000000000 % a[0] # get the remainder

    y_ww = 10000000000000 // a[1] 
    y_rem = 10000000000000 % a[1]

    new_target = (target[0] + x_rem, target[1] + x_rem) # add the remainder to the target 

    sols = []
    for i in range(a[0], new_target[0], a[0]):
        # for multiples of a[0]

        if (new_target[0] - i) % b[0] == 0: # if the remainder is 0
            aaa = i // a[0]
            possible_as.append(aaa)
            bbb = (new_target[0] - i) // b[0]
            possible_bs.append(bbb)

            if a[1] * aaa + b[1] * bbb == new_target[1]:
                print('asd', (aaa * a[1], bbb * b[1]))

    print('possible_as:', possible_as)
    print('possible_bs:', possible_bs)
    tokens = 0



    print("TARGETS:")
    print(target)
    print((new_target[0], new_target[1]))
    for x, y in zip(possible_as, possible_bs):
        print((x * a[0] + y * b[0], x * a[1] + y * b[1]))
        # remove 100 button limit
        # if x > 100 or y > 100:
        #     continue

        if (a[1] * x) + (b[1] * y) == new_target[1]:
            # calculate num of token
            # num of a button press * 3
            # num of b button press * 1
            temp_tokens = ((x + x_ww) * 3) + y
            
            # save the minimum
            if temp_tokens < tokens or tokens == 0:
                tokens = temp_tokens

    print(tokens)

    return tokens

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))