import re
import time
import numpy as np
from PIL import Image

def solve_star_1(input: list[str]) -> int:
    # solution idea:
    
    res = 0

    ## example:
    # SECS = 5
    # COL_MAX = 11
    # ROW_MAX = 7

    SECS = 100
    COL_MAX = 101
    ROW_MAX = 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line_idx in range(len(input)):
        p, v = input[line_idx].split(' ')
        p = tuple(map(int, re.findall(r'\d+,\d+', p)[0].split(',')))
        v = tuple(map(int, re.findall(r'-?\d+,-?\d+', v)[0].split(',')))
        print(p, v, end=" ")

        p = ((p[0] + (v[0] * SECS)) , (p[1] + (v[1] * SECS)))
        p = ((p[0] % COL_MAX) , (p[1] % ROW_MAX))
        
        if p[0] == COL_MAX // 2 or p[1] == ROW_MAX // 2:
            continue
        elif p[0] < COL_MAX // 2:
            if p[1] < ROW_MAX // 2:
                q1 += 1
            else:
                q4 += 1
        else:
            if p[1] < ROW_MAX // 2:
                q2 += 1
            else:
                q3 += 1

        # determine quadrant

    res = q1 * q2 * q3 * q4

    return res


def solve_star_2(input: list[str]) -> int:
    # solution idea:
    # use a for loop to iterate positions of robots at each loop
    # i think if left and right quadraants are equal, its a christmas three
    res = 0

    ## example:
    # SECS = 5
    # COL_MAX = 11
    # ROW_MAX = 7

    SECS = 100
    COL_MAX = 101
    ROW_MAX = 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line_idx in range(len(input)):
        p, v = input[line_idx].split(' ')
        p = tuple(map(int, re.findall(r'\d+,\d+', p)[0].split(',')))
        v = tuple(map(int, re.findall(r'-?\d+,-?\d+', v)[0].split(',')))
        input[line_idx] = [p, v]
    
    print("PART 2")
    for i in range(9999):
        print(i)
        # print("======================================================================================================")
        q1, q2, q3, q4 = 0, 0, 0, 0
        sset = set()

        board = []  
        for x in range(COL_MAX):
            line = []

            for y in range(ROW_MAX):
                line.append(False)

            board.append(line)
        
        for x in range(len(input)):
            p = input[x][0]
            v = input[x][1]

            p = ((p[0] + (v[0])) % COL_MAX , (p[1] + (v[1])) % ROW_MAX)
            input[x] = [p, v]
            # print(p)
            sset.add(p)

            if p[0] < COL_MAX // 2:
                if p[1] < ROW_MAX // 2:
                    q1 += 1
                else:
                    q4 += 1
            else:
                if p[1] < ROW_MAX // 2:
                    q2 += 1
                else:
                    q3 += 1

        # # get quadrants
        # if q1 == q2 and q3 == q4 and q1 != 0: # board is inversed
        #     print('found christmas tree')
        #     res = i
        #     break
        # creating tree
        for coord in sset:
            board[coord[0]][coord[1]] = True
        # time.sleep(1)
        # for line in board:
            # print(line)
            # print("".join(line))

        np_arr = board
        image_arr = np.where(np_arr, 255, 0).astype(np.uint8)
        
        if i > 4658:
            img = Image.fromarray(image_arr , 'L')
            img.save(f"output_{i}.png")
    # print("PART 2")
    # i = 0
    # while res == 0:
    #     print(i)
    #     q1, q2, q3, q4 = 0, 0, 0, 0
    #     sset = set()

    #     board = []  
    #     for x in range(COL_MAX):
    #         line = []

    #         for y in range(ROW_MAX):
    #             line.append('.')

    #         board.append(line)
        
    #     for x in input:
    #         p = x[0]
    #         v = x[1]

    #         p = ((p[0] + (v[0])) % COL_MAX , (p[1] + (v[1])) % ROW_MAX)
    #         # print(p)
    #         sset.add(p)

    #         if p[0] < COL_MAX // 2:
    #             if p[1] < ROW_MAX // 2:
    #                 q1 += 1
    #             else:
    #                 q4 += 1
    #         else:
    #             if p[1] < ROW_MAX // 2:
    #                 q2 += 1
    #             else:
    #                 q3 += 1

    #     # get quadrants
    #     if q1 == q2 and q3 == q4 and q1 != 0: # board is inversed
    #         print('found christmas tree')
    #         res = i
    #         break

    #     i += 1

    #     for coord in sset:
    #         board[coord[0]][coord[1]] = 'X'

    #     time.sleep(.25)
    #     for line in board:
    #             print("".join(line))
    #     # creating tree

    # return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))

# References:
# https://stackoverflow.com/questions/37558523/converting-2d-numpy-array-of-grayscale-values-to-a-pil-image