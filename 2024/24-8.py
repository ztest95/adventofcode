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
    ALLOWED_CHARS = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    COLS = len(input[0]) # get the number of rows and columns for checking out of bounds
    ROWS = len(input)

    antennae = {}
    # creating map
    # { 'char': [(x1, y1), (x2, y2), ...] }
    for y in range(len(input)):
        for j in range(len(input[y])):
            if input[y][j] in ALLOWED_CHARS:
                coord = (y, j)
                if input[y][j] not in antennae:
                    antennae[input[y][j]] = []
                
                antennae[input[y][j]].append(coord)

    anti_nodes = set() # set to store unique anti nodes coordinates
    for key in antennae:
        for i in range(len(antennae[key])):
            
            for j in range(i + 1, len(antennae[key])):
                coord_1 = antennae[key][i]
                coord_2 = antennae[key][j]

                displacement = calc_displacement(coord_1, coord_2)
                
                # anti node coordinates
                an_1 = (coord_1[0] - displacement[0], coord_1[1] - displacement[1])
                an_2 = (coord_2[0] + displacement[0], coord_2[1] + displacement[1])
                

                # check if anti node is out of bounds
                if an_1[0] >= 0 and an_1[1] >= 0 and an_1[0] < ROWS and an_1[1] < COLS:
                    anti_nodes.add(an_1)

                if an_2[0] >= 0 and an_2[1] >= 0 and an_2[0] < ROWS and an_2[1] < COLS:
                    anti_nodes.add(an_2)

    res = len(anti_nodes)
    return res


def calc_displacement(coord1: tuple[int, int], coord2: tuple[int, int]) -> tuple[int, int]:
    return (coord2[0] - coord1[0], coord2[1] - coord1[1])


def solve_star_2(input: list[str]) -> int:
    # for part 2, we just need to repeat subtracting / adding the displacement to the coordinates
    # we also need to add the coordinates of antennae to the anti nodes
    res = 0

    ALLOWED_CHARS = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    COLS = len(input[0])
    ROWS = len(input)

    antennae = {}
    for y in range(len(input)):
        for j in range(len(input[y])):
            if input[y][j] in ALLOWED_CHARS:
                coord = (y, j)
                if input[y][j] not in antennae:
                    antennae[input[y][j]] = []
                
                antennae[input[y][j]].append(coord)

    anti_nodes = set()
    for key in antennae:
        for i in range(len(antennae[key])):
            
            for j in range(i + 1, len(antennae[key])):
                coord_1 = antennae[key][i]
                coord_2 = antennae[key][j]
                
                # add antennae to anti nodes
                anti_nodes.add(coord_1)
                anti_nodes.add(coord_2)

                displacement = calc_displacement(coord_1, coord_2)
                
                an_1 = (coord_1[0] - displacement[0], coord_1[1] - displacement[1])
                an_2 = (coord_2[0] + displacement[0], coord_2[1] + displacement[1])
                
                # convert the if statements to while loops
                
                # repeat subtracting displacement to the lower coordinate
                while an_1[0] >= 0 and an_1[1] >= 0 and an_1[0] < ROWS and an_1[1] < COLS:
                    anti_nodes.add(an_1)
                    an_1 = (an_1[0] - displacement[0], an_1[1] - displacement[1])
                    
                # repeat adding displacement to the higher coordinate
                while an_2[0] >= 0 and an_2[1] >= 0 and an_2[0] < ROWS and an_2[1] < COLS:
                    anti_nodes.add(an_2)
                    an_2 = (an_2[0] + displacement[0], an_2[1] + displacement[1])

    res = len(anti_nodes) 

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))