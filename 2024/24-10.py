def solve_star_1(input: list[str]) -> int:
    res = 0

    # convert input to integer
    
    for line_idx in range(len(input)):
        input[line_idx] = [int(x) for x in list(input[line_idx])]

    # find base
    bases = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                bases.append((i, j))

    def find_trail(level, index, list, peaks):
        # print('level:', level, 'inspecting:', index, 'with value of ', list[index[0]][index[1]])
        if level == 9:
            # look up coordinate
            # print('9 founds')
            if index in peaks:
                return peaks
            else:
                peaks.append(index)
                return peaks

        # top
        x, y = index
        if x - 1 >= 0 and list[x - 1][y] == level + 1:
            # print('top')
            peaks = find_trail(level + 1, (x - 1, y), list, peaks)

        # Check boundary and then compare the value for right
        if y + 1 < len(list[0]) and list[x][y + 1] == level + 1:
            # print('right')
            peaks = find_trail(level + 1, (x, y + 1), list, peaks)

        # Check boundary and then compare the value for bottom
        if x + 1 < len(list) and list[x + 1][y] == level + 1:
            # print('bottom')
            peaks = find_trail(level + 1, (x + 1, y), list, peaks)

        # Check boundary and then compare the value for left
        if y - 1 >= 0 and list[x][y - 1] == level + 1:
            # print('left')
            peaks = find_trail(level + 1, (x, y - 1), list, peaks)

        return peaks

    
    mapp = {}
    for base in bases:
        peaks_coords = []
        peaks_coords = find_trail(0, base, input, peaks_coords)
        mapp[base] = len(peaks_coords)
        res += len(peaks_coords)

    # i started coding wiwthout reading the entire problem lmao
    return res

def solve_star_2(input: list[str]) -> int:
    res = 0

    # convert input to integer
    
    for line_idx in range(len(input)):
        input[line_idx] = [int(x) for x in list(input[line_idx])]

    # find base
    bases = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                bases.append((i, j))

    def find_trail(level, index, list, peaks):
        # print('level:', level, 'inspecting:', index, 'with value of ', list[index[0]][index[1]])
        if level == 9:
            # just add wen 9 is found
            peaks.append(index)
            return peaks

        # top
        x, y = index
        if x - 1 >= 0 and list[x - 1][y] == level + 1:
            # print('top')
            peaks = find_trail(level + 1, (x - 1, y), list, peaks)

        # Check boundary and then compare the value for right
        if y + 1 < len(list[0]) and list[x][y + 1] == level + 1:
            # print('right')
            peaks = find_trail(level + 1, (x, y + 1), list, peaks)

        # Check boundary and then compare the value for bottom
        if x + 1 < len(list) and list[x + 1][y] == level + 1:
            # print('bottom')
            peaks = find_trail(level + 1, (x + 1, y), list, peaks)

        # Check boundary and then compare the value for left
        if y - 1 >= 0 and list[x][y - 1] == level + 1:
            # print('left')
            peaks = find_trail(level + 1, (x, y - 1), list, peaks)

        return peaks

    
    mapp = {}
    for base in bases:
        peaks_coords = []
        peaks_coords = find_trail(0, base, input, peaks_coords)
        mapp[base] = len(peaks_coords)
        res += len(peaks_coords)
    
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))