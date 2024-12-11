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
        # print(stones)
    
    # print(len(stones))
    res = len(stones)
    return res

# def process(list: list[str]) -> list[str]:



def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))