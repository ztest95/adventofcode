def solve_star_1(input: list[str]) -> int:
    # solution idea:
    
    res = 0
    
    grid_size = 7
    mapp = [ [0] * grid_size for _ in range(grid_size) ]
    print(mapp)
    walls = set()
    for i in range(1024):
        x, y = tuple(map(int, input[i].split(',')))
        mapp[x][y] = 1
        walls.add((x,y))


    for i in range(len(mapp)):      
        print(mapp[i])

    res = dfs(mapp, walls, (0,0), 0)

    return res

def dfs(grid: list, wall: set, coord: tuple, steps: int) -> int:
    x, y = coord[0], coord[1]
    print(x,y)
    if (x, y) == (6, 6):
        print(steps)
        return steps

    dirs = {(-1,0), (0, 1), (1, 0), (0, -1)}
    around = {(x+dx, y+dy) for dx, dy in dirs}
    walls = wall.copy()
    walls.add((x, y))
    asd = []
    for xx, yy in around:
        # print(xx > 0)
        # print(yy > 0)
        # print(xx < 7)
        # print(yy < 7)
        # print((xx,yy) not in wall)
        if xx > -1 and yy > -1 and xx < 7 and yy < 7 and (xx, yy) not in wall:
            asd.append(dfs(grid, walls, (xx, yy), steps + 1))
        else:
            asd.append(10000)
    return min(asd) if around else 9 ** 10


def solve_star_2(input: list[str]) -> int:
    # solution idea

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/24-18test.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))
