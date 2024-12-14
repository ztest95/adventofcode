import re
import time
import numpy as np
from PIL import Image

def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # just multiply the sec to velocity to get final displacement 
    # and then get the coord by using modulo to row & col, to get remainder

    res = 0

    SECS = 100
    COL_MAX = 101
    ROW_MAX = 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line_idx in range(len(input)):
        pos, vel = input[line_idx].split(' ')
        pos = tuple(map(int, re.findall(r'\d+,\d+', pos)[0].split(',')))
        vel = tuple(map(int, re.findall(r'-?\d+,-?\d+', vel)[0].split(',')))

        pos = ((pos[0] + (vel[0] * SECS)) , (pos[1] + (vel[1] * SECS))) # add pos with distance * time 
        pos = ((pos[0] % COL_MAX) , (pos[1] % ROW_MAX)) # get remainder (board coordinate)
        
        if pos[0] == COL_MAX // 2 or pos[1] == ROW_MAX // 2: # disregard pos on the centers
            continue
        elif pos[0] < COL_MAX // 2: 
            if pos[1] < ROW_MAX // 2:
                q2 += 1
            else:
                q3 += 1
        else:
            if pos[1] < ROW_MAX // 2:
                q1 += 1
            else:
                q4 += 1

        # determine quadrant

    res = q1 * q2 * q3 * q4

    return res


def solve_star_2(input: list[str]) -> int:
    # solution idea:
    # use a for loop to iterate positions of robots at each loop
    # i think if left and right quadraants are equal, its a christmas three
    # edit, after watching my cli for a while for each 100 sec cycle
    # i looked online for answers,
    # and decided to use save each arr as image
    res = 0

    SECS = 100
    COL_MAX = 101
    ROW_MAX = 103

    for line_idx in range(len(input)):
        p, v = input[line_idx].split(' ')
        p = tuple(map(int, re.findall(r'\d+,\d+', p)[0].split(',')))
        v = tuple(map(int, re.findall(r'-?\d+,-?\d+', v)[0].split(',')))
        input[line_idx] = [p, v]
        
    for i in range(9999):
        positions = set()
        # Create Board
        board = [ [False] * ROW_MAX for _ in range(COL_MAX) ]
        
        for x in range(len(input)):
            pos = input[x][0]
            vel = input[x][1]

            pos = ((pos[0] + vel[0]) % COL_MAX , (pos[1] + vel[1]) % ROW_MAX)
            input[x] = [pos, vel]
            positions.add(pos)

        for coord in positions:
            board[coord[0]][coord[1]] = True

        # Save Images
        # np_arr = np.array(board)
        # image_arr = np.where(np_arr, 255, 0).astype(np.uint8)
        # img = Image.fromarray(image_arr , 'L')
        # img.save(f"output_{i+1}.png")

    return None

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))

# References:
# https://stackoverflow.com/questions/37558523/converting-2d-numpy-array-of-grayscale-values-to-a-pil-image