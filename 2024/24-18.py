GRID_SIZE = 71
DROPS = 1024


def solve_star_1(input: list[str]) -> int:
    # solution idea:

    res = 0

    mapp = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    walls = set()
    for i in range(DROPS):
        x, y = tuple(map(int, input[i].split(",")))
        mapp[x][y] = 1
        walls.add((x, y))

    res = bfs(mapp, walls, (0, 0), 0)

    return res

def bfs(grid: list, wall: set, coord: tuple, steps: int) -> int:
    x, y = coord[0], coord[1]

    paths = [coord]

    walls = wall.copy()
    walls.add((x, y))

    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}

    found = False
    new_layer_count = 0
    curr_layer_count = len(paths)
    while curr_layer_count > 0:
        x, y = paths.pop(0)
        if (x, y) == (GRID_SIZE - 1, GRID_SIZE - 1):
            found = True
            break

        around = {(x + dx, y + dy) for dx, dy in dirs}
        for xx, yy in around:
            if (
                xx > -1
                and yy > -1
                and xx < GRID_SIZE
                and yy < GRID_SIZE
                and (xx, yy) not in walls
            ):
                paths.append((xx, yy))
                walls.add((xx, yy))
                new_layer_count += 1

        curr_layer_count -= 1
        if curr_layer_count == 0:
            curr_layer_count = new_layer_count
            new_layer_count = 0
            steps += 1

    if found:
        return steps

    return -1


def solve_star_2(input: list[str]) -> int:
    # solution idea:
    # brute force every iter

    res = 0

    mapp = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    walls = set()
    for i in range(len(input)): # use entire input
        print(i)
        x, y = tuple(map(int, input[i].split(",")))
        mapp[x][y] = 1
        walls.add((x, y))

        if bfs(mapp, walls, (0, 0), 0) == -1: # find drop that closes path
            res = (x, y)
            break

    return res


if __name__ == "__main__":

    with open("2024/24-18.txt") as f:
        input = [line.strip("\n") for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input.copy()))

# References
# https://youtu.be/KiCBXu4P-2Y
# this is actually my first time impementing bfs