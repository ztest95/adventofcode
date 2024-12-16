def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # simple dfs

    res = 0
    
    S = 0, 0
    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == "S":
                S = x, y

    res = dfs(S, None, -1, set())
        

    return res

def dfs(coord: tuple, prev: tuple, minn: int, visi: set):
    x = coord[0]
    y = coord[1]
    

    minn += 1
    visited = visi.copy()
    # found end
    if input[x][y] == "E":
        return minn

    visited.add((x, y))

    mins = set()
    ss = False
    if input[x-1][y] != "#" and (x-1, y) not in visited: # top
        if prev != "bottom":
            ss = ((dfs((x-1, y), "bottom", minn + 1000, visited)))
        else:
            ss = ((dfs((x-1, y), "bottom", minn, visited)))

        if ss:
            mins.add(ss)

    if input[x][y+1] != "#" and (x, y+1) not in visited: # right
        if prev != "left":
            ss = ((dfs((x, y+1), "left", minn + 1000, visited)))
        else:
            ss = (dfs((x, y+1), "left", minn, visited))

        if ss:
            mins.add(ss)

    if input[x+1][y] != "#" and (x+1, y) not in visited: # bottom
        if prev != "top":
            ss = (dfs((x+1, y), "top", minn + 1000, visited))
        else:
            ss =  (dfs((x+1, y), "top", minn, visited))

        if ss: 
            mins.add(ss)

    if input[x][y-1] != "#" and (x, y-1) not in visited: #left
        if prev != "right":
            ss = (dfs((x, y-1), "right", minn + 1000, visited))
        else:
            ss = mins.add(dfs((x, y-1), "right", minn, visited))
        
        if ss:
            mins.add(ss)

    if mins:
        minn = min(mins)
        return minn

    return 0

def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/testinput.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))
