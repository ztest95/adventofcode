def solve_star_1(input: list[str]) -> int:
    # idea:
    # create a map with key as character of each unique antennae, and value as the coordinates of the antennaes
    # get every possible pair combination in a value of the map,
    #   calculate the displacement between the two coordinates (x, y)
    #   and subtract the displacement to the lower coordinate (closer to top left), 
    #   and add the displacement to the higher coordinate (closer to bottom right)
    #   for both of these, if the resulting coordinate is not out of bounds / does not contains another antennae,
    #      +1 to count

    res = 0
    allowed_chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

    antennae = {}
    # creating map
    for y in range(len(input)):
        for j in range(len(input[y])):
            if input[y][j] in allowed_chars:
                coord = (y, j)
                if input[y][j] not in antennae:
                    antennae[input[y][j]] = []
                
                antennae[input[y][j]].append(coord)

    cols = len(input[0])
    rows = len(input)

    anti_nodes = set()
    for key in antennae:
        for i in range(len(antennae[key])):
            
            for j in range(i + 1, len(antennae[key])):
                coord_1 = antennae[key][i]
                coord_2 = antennae[key][j]

                displacement = calc_displacement(coord_1, coord_2)
                
                # anti node
                an_1 = (coord_1[0] - displacement[0], coord_1[1] - displacement[1])
                an_2 = (coord_2[0] + displacement[0], coord_2[1] + displacement[1])
                

                # check if anti node is out of bounds
                if an_1[0] >= 0 and an_1[1] >= 0 and an_1[0] < rows and an_1[1] < cols:
                    anti_nodes.add(an_1)

                if an_2[0] >= 0 and an_2[1] >= 0 and an_2[0] < rows and an_2[1] < cols:
                    anti_nodes.add(an_2)

    res = len(anti_nodes)
    return len(set(anti_nodes))


def calc_displacement(coord1: tuple[int, int], coord2: tuple[int, int]) -> tuple[int, int]:
    return (coord2[0] - coord1[0], coord2[1] - coord1[1])


def solve_star_2(input: list[str]) -> int:
    res = 0

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))