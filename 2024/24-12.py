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

    print(input[0])
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
        print(key, value)
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

            # print(fences)
            res += len(value[set_idx]) * fences

    print(regions)
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

    res = 0

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))