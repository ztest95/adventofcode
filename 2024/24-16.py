import time

def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # simple dfs - max recursion dept
    # use loop when moving forward, recurse only when intersection

    res = 0
    
    S = 0, 0
    for x in range(len(input)):
        input[x] = list(input[x])
        for y in range(len(input[x])):
            if input[x][y] == "S":
                S = x, y

    q = input.copy( )
    res = dfs(S, (S[0], S[1]-1), -1, set(), q)
        

    return res

def dfs(coord: tuple, prev: tuple, minn: int, visi: set, input):
    x, y = coord[0], coord[1]


    # print("CHANGED DIRECTION", prev, "->", coord)
    # print("================")
    copy = input.copy()
    # for l in copy:
    #     print("".join(l))
    # print(minn)
    # print("================")


    visited = visi.copy()
    # found end
    copy[x][y] = "X"
    visited.add((x, y))

    mins = set()
    prev_x = prev[0]
    prev_y = prev[1]
    tt = False
    while input[x][y] != "#":
        # time.sleep(.1)
        minn += 1
        
        if input[x][y] == "E":
            # print("FOUND E", minn)
            return minn
        
        visited.add((x, y))
        copy[x][y] = "X"
        # check for intersection at every step
        dirs = {(x-1, y), (x, y+1), (x+1, y), (x, y-1)}
        # prev coord - curr coord = backward direction
        # curr coord - prev coord = forward direction
        dirs.remove((prev_x, prev_y)) # remove prev, dont recurse
        forward = (x - prev_x, y - prev_y)
        dirs.remove((x + forward[0], y + forward[1])) # remove recurse on next, it will be on next iter

        for xx, yy in dirs:
            if input[xx][yy] != "#" and (xx, yy) not in visited:
                mins.add(dfs((xx, yy), (x, y), minn + 1000, visited, copy.copy()))
        # print("================")
        # for l in copy:
        #     print("".join(l))
        # print(minn)
        # print("================")

        prev_x = x
        prev_y = y
        x += forward[0]
        y += forward[1]

    if mins:
        minn = min(mins)
        return minn

    if tt:
        # print("FOUND E", minn)
        return minn
    else:
        return 9 ** 10

    return minn

def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/testinput.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))
