def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # rules:
    # if num = 0 -> num = 1
    # if len(str(num)) % 2 == 0 -> replace by two stones,  leftstrip 0, split str to ints again
    # else; stone * 2024
    # we are not going to do the actual rules
    # just split when the second rule is met 

    # edit:
    # okay, we are going to follow the actual instructions
    res = 0

    stones = list(map(len ,input[0].split(' ')))
    # print(stones)
    # res = len(stones)
    # for i in range(25):
    #     print('iteration:', i)
    #     j = 0
    #     l = len(stones)
    #     while j < l and j < 10:
    #         # print('j:', j, 'stone:', stones[j])
    #         if stones[j] == 0:
    #             stones[j] = 1
    #         elif stones[j] % 2 == 0:
    #             # print('splitting', stones[j])
    #             stones[j] = 1
    #             stones.insert(j, 1)
    #             j += 1
    #         else:
    #             stones[j] = stones[j] * 2024
    #         print(stones)
    #         j += 1
    #         l = len(stones)

    stones =  input[0].split(' ')
    # print(stones)
    for i in range(25):
        print(i)
        j = 0
        l = len(stones)
        while j < l:
            if stones[j] == '0':
                stones[j] = '1'
            elif len(stones[j]) % 2 == 0:
                # print('splitting', stones[j])
                half = len(stones[j]) // 2 # get half
                temp = stones[j] 
                stones[j] = temp[:half] # left stone is left half
                half = temp[half:].lstrip('0') # right half
                stones.insert(j+1, '0' if len(half.lstrip('0')) == 0 else half) # right stone is right half
                j += 1
            else:
                stones[j] = str(int(stones[j]) * 2024)
            j += 1
            l = len(stones)

    res = len(stones)
    return res

# def process(list: list[str]) -> list[str]:


def solve_star_2(input: list[str]) -> int:
    res = 0

    stones = list(map(len ,input[0].split(' ')))

    stones =  input[0].split(' ')
    for i in range(len(stones)):
        stones[i] = (len(stones[i]), stones[i])

    # print(stones)
    ITER = 6
    def calc(num_str, i, n_split=0):
        # print(i)
        if i == 30:
            return n_split
        
        if len(num_str) % 2 == 0:
            # print('rule 2: ', num_str)
            l_half = num_str[:len(num_str)//2]
            r_half = '0' if len(num_str[len(l_half):].lstrip('0')) == 0 else num_str[len(l_half):].strip('0')
            # print('num_str:', num_str, 'splitting:' ,'l_half:', l_half, 'r_half:', r_half)
            a = calc(l_half, i+1, 0) 
            b = calc(r_half, i+1, 0) 
            n_split += 1
            if a:
                n_split += a
            if b:
                n_split += b
        elif num_str == '0':
            # print('rule 1: ', num_str)
            c = calc('1', i+1, 0) 
            if c:
                n_split += c
        else:
            # print('rule 3: ', num_str)
            d = calc(str(int(num_str) * 2024), i+1, 0) 
            if d:
                n_split += d
        
        return n_split
    
    temp = []
    for stone in stones:
        temp.append(calc(stone[1], 0, 0))
        # print(temp)

    print(temp)
    for x in temp:
        res += x

    return res + len(stones)

if __name__ == "__main__":

    with open('2024/testinput.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    # print(solve_star_1(input))
    print(solve_star_2(input.copy()))


# def solve_star_2(input: list[str]) -> int:
#     # try to make it faster whiel waiting
#     res = 0

#     stones = list(map(int ,input[0].split(' ')))

#     stones =  input[0].split(' ')
#     for i in range(len(stones)):
#         stones[i] = (len(stones[i]), int(stones[i]))
#     # print(stones)
#     print(stones)
#     for i in range(75):
#         print('interation:', i)
#         j = 0
#         l = len(stones)
#         while j < l:
#             val = stones[j][1]
#             # print(stones[j])
#             if val == 0:
#                 stones[j] = (1, 1)
#                 # print('rule 1')
#             elif (stones[j][0] % 2) == 0:
#                 half = stones[j][0] // 2 # get half
#                 temp = str(val) 
#                 # print('stones[j][0] // 2 = ', half)
#                 stones[j] = (half, int(temp[:half])) # left stone is (len, left half)
#                 l_half = temp[half:].lstrip('0') # right half
#                 stones.insert(j+1, (len(l_half), (0 if len(str(l_half)) == 0 else int(l_half)))) # right stone is (len, right half)
#                 j += 1
#                 # print('rule 2')
#             else:
#                 new = val * 2024
#                 stones[j] = (len(str(new)), new)
#                 # print(' rule 3')
#             j += 1
#             l = len(stones)

#         # print("[", end = " ")
#         # for i in range(len(stones)):
#         #     print(stones[i][1], end =", ")
#         # print(" ]")
    
#     # print(len(stones))
#     res = len(stones)
#     return res

# if __name__ == "__main__":

#     with open('2024/testinput.txt') as f:
#         input = [line.strip('\n') for line in f.readlines()]
    
#     # print(solve_star_1(input))
#     print(solve_star_2(input.copy()))