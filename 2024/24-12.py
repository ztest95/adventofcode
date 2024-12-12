def solve_star_1(input: list[str]) -> int:
    # solution idea:
    # create a map with key representing region representation (char), and values as array [set of (x, y)] coordinates
    # then for each region (key, value) in map, find the neighbors of each coordinate and find if it should be fenced

    # for row, col in input
    # if char at row,col is in map
    #       check if coordinate is in any of set inside the array value of the map
    #           if yes,
    #               continue
    #           if no:
    #               create set
    #               do recursion
    #               add the set to the array value of the map
    # else
    #       create set      
    #       do the recursion 
    #       add new char as key, and set value

    # total fences = 0
    # for each key, value in map
    #       for each set in value
    #           region fences = 0
    #           check neighboring coordinates
    #           increment var accordingly
    #        total fences += region fence

    for row in range(len(input)):
        input[row] = list(input[row])

    regions = {}
    for x in range(len(input)):
        for y in range(len(input[x])):
            char = input[x][y]
            if char in regions.keys():
                # for every set in array[set] value
                all_coords = set()
                for c_set in regions[char]:
                    all_coords = all_coords.union(c_set)

                if (x, y) in all_coords:
                    continue
                else:
                    new_set = set()
                    new_set = new_set.union(find_region(new_set, (x, y), input))
                    regions[char].append(new_set)
            else:
                new_set = set()
                new_set = new_set.union(find_region(new_set, (x, y), input))
                regions[char] = [new_set]

    res = 0 # total fencing
    for key, value in regions.items():
        for set_idx in range(len(value)):
            fences = 0
            for coord in value[set_idx]:
                x, y = coord[0], coord[1]
                char = input[x][y]

                if x-1 < 0 or input[x-1][y] != char:
                    fences += 1
                if y+1 > len(input[0]) - 1 or  input[x][y+1] != char:
                    fences += 1
                if x+1 > len(input) - 1 or  input[x+1][y] != char:
                    fences += 1
                if y-1 < 0 or input[x][y-1] != char:
                    fences += 1

            res += len(value[set_idx]) * fences

    return res

def find_region(coord_set: set, coord: tuple, map: list) -> set:
    x, y = coord[0], coord[1]
    if coord in coord_set:
        return coord_set

    coord_set.add(coord)
    char = map[x][y]

    rows = len(map)
    cols = len(map[0])
    
    if x > 0 and map[x-1][y] == char:
        coord_set = coord_set.union(find_region(coord_set, (x-1, y), map))
    if y < cols - 1 and map[x][y+1] == char:
        coord_set = coord_set.union(find_region(coord_set, (x, y+1), map))
    if x < rows - 1 and map[x+1][y] == char:
        coord_set = coord_set.union(find_region(coord_set, (x+1, y), map))
    if y > 0 and map[x][y-1] == char:
        coord_set = coord_set.union(find_region(coord_set, (x, y-1), map))
    
    return coord_set


def solve_star_2(input: list[str]) -> int:
    # solution idea
    # save two coordinates in set, the coord of the plot and then the neighobor plot its comparing to
    # we can then compare whether the two coords beside a coord is already in the set
    #   if yes, then we can skip the coord
    #   if no, then we can add the coord to the set
    # instead of saving all coords such as (coord 1, coord 2)
    # for top bottom comparison vertical comparisons / horizontal fences check
    #   we can just save x coord 
    # for left right comparison horizontal comparisons / vertical fences check
    #   we can just save y coord
    for row in range(len(input)):
        input[row] = list(input[row])

    regions = {}
    for x in range(len(input)):
        for y in range(len(input[x])):
            char = input[x][y]
            if char in regions.keys():
                # for every set in array[set] value
                all_coords = set()
                for c_set in regions[char]:
                    all_coords = all_coords.union(c_set)

                if (x, y) in all_coords:
                    continue
                else:
                    new_set = set()
                    new_set = new_set.union(find_region(new_set, (x, y), input))
                    regions[char].append(new_set)
            else:
                new_set = set()
                new_set = new_set.union(find_region(new_set, (x, y), input))
                regions[char] = [new_set]


    for key, value in regions.items():
        for i in range(len(value)):
            regions[key][i] = sorted(value[i], key=lambda coord: (coord[0], coord[1]))

    res = 0 # total fencing
    for key, value in regions.items():
        for set_idx in range(len(value)):
            v_set = set()
            h_set = set()
            hh_set = set()
            vv_set = set()
            fences = 0
            for coord in value[set_idx]:
                x, y = coord[0], coord[1]
                char = input[x][y]
                z = v_set.union(vv_set)

                if x-1 < 0 or input[x-1][y] != char:
                    if f"({x}{y-1})-({x-1}{y-1})" in z or f"({x}{y+1})-({x-1}{y+1})" in z:
                        vv_set.add(f"({x}{y})-({x-1}{y})")
                        pass
                    else:
                        v_set.add(f"({x}{y})-({x-1}{y})")
                        fences += 1
                if y+1 > len(input[0]) - 1 or  input[x][y+1] != char:
                    if f"({x-1}{y})-({x-1}{y+1})" in h_set.union(hh_set) or f"({x+1}{y})-({x+1}{y+1})" in h_set.union(hh_set):
                        hh_set.add(f"({x}{y})-({x}{y+1})")
                    else:
                        h_set.add(f"({x}{y})-({x}{y+1})")
                        fences += 1
                if x+1 > len(input) - 1 or  input[x+1][y] != char:
                    if f"({x}{y+1})-({x+1}{y+1})" in z or f"({x}{y-1})-({x+1}{y-1})" in z:
                        vv_set.add(f"({x}{y})-({x+1}{y})")
                    else:
                        v_set.add(f"({x}{y})-({x+1}{y})")
                        fences += 1
                if y-1 < 0 or input[x][y-1] != char:
                    if f"({x+1}{y})-({x+1}{y-1})" in h_set.union(hh_set) or f"({x-1}{y})-({x-1}{y-1})" in h_set.union(hh_set):
                        hh_set.add(f"({x}{y})-({x}{y-1})")
                    else:
                        h_set.add(f"({x}{y})-({x}{y-1})")
                        fences += 1

            # i was stuck for a while even though i had the right solution
            # the problem was, each plot of garden were being processed randomly because i was using a set
            # fixed this by sorting them first by x, then by y
            res += fences * len(value[set_idx])

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))