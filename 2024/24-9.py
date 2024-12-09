def solve_star_1(input: list[str]) -> int:
    res = 0

    disk_map = input[0]
    # print(disk_map)

    # parsing disk map
    parsed_disk_map = []
    id = 0
    for i in range(len(disk_map)):
        val = int(disk_map[i])
        if i % 2 == 0:
            for j in range(1, val+1):
                parsed_disk_map.append(str(id))
            id += 1
        else:
            for j in range(val):
                parsed_disk_map.append('.')
            
    # print(parsed_disk_map)
    sorted_disk_map = parsed_disk_map.copy()

    # sorting
    # using two pointers
    last = len(parsed_disk_map) - 1

    for i in range(len(sorted_disk_map)):
        if sorted_disk_map[i] == '.':
            sorted_disk_map[i], sorted_disk_map[last] = sorted_disk_map[last], sorted_disk_map[i]
            last -= 1

        while sorted_disk_map[last] == '.':
            last -= 1
        
        if i >= last:
            break
    # print("".join(sorted_disk_map))
    sorted_disk_map = "00992111777.44.333....5555.6666.....8888.."
    for i in range(len(sorted_disk_map)):
        if sorted_disk_map[i] != '.':
            res += i * int(sorted_disk_map[i])

    return res  

def solve_star_2(input: list[str]) -> int:
    # for part 2, 
    # change the parsing of the disk map
    # instead actually parsing, lets save them as tuples, (id, count)
    res = 0

    disk_map = input[0]
    # print(disk_map)

    # parsing disk map
    id_mapped_disk_map = []
    id = 0
    for i in range(len(disk_map)):
        val = int(disk_map[i])
        if i % 2 == 0:
            id_mapped_disk_map.append((id, val))
            id += 1
        else:
            id_mapped_disk_map.append((None, val))
            
    # print(parsed_disk_map)
    # print('asd')
    print(id_mapped_disk_map)
    i = 0
    l = len(id_mapped_disk_map)
    while i < l: 
        # print('iter', i)
        if id_mapped_disk_map[i][0] == None:
            # print("found none", i)
            filled = False
            j = len(id_mapped_disk_map) - 1
            while not filled and j > i:
                # fi its not an empty block
                if id_mapped_disk_map[j][0] != None and id_mapped_disk_map[j][1] > 0:
                    if id_mapped_disk_map[j][1] == id_mapped_disk_map[i][1]:
                        # print('swapping', id_mapped_disk_map[i], id_mapped_disk_map[j])
                        id_mapped_disk_map[i], id_mapped_disk_map[j] = id_mapped_disk_map[j], id_mapped_disk_map[i]
                        # print(id_mapped_disk_map)
                        filled = True
                    elif id_mapped_disk_map[j][1] < id_mapped_disk_map[i][1]:
                        # print('subtracting', id_mapped_disk_map[i], id_mapped_disk_map[j])
                        
                        # create temp vars
                        i_temp = (id_mapped_disk_map[i][0], id_mapped_disk_map[i][1])
                        j_temp = (id_mapped_disk_map[j][0], id_mapped_disk_map[j][1])

                        # print('before', id_mapped_disk_map)
                        id_mapped_disk_map.insert(i, (j_temp[0], j_temp[1]))
                        # print('after', id_mapped_disk_map)

                        id_mapped_disk_map[i+1] = (None, i_temp[1] - j_temp[1]) 
                        # remove the block
                        id_mapped_disk_map[j+1] = (None, j_temp[1])
                        # print('after after', id_mapped_disk_map)
                        # move in front of empty block
                        
                        filled = True
                j -= 1
        i += 1
        l = len(id_mapped_disk_map)

    parsed_disk_map = []
    for i in range(len(id_mapped_disk_map)):
        if id_mapped_disk_map[i][0] != None:
            for j in range(id_mapped_disk_map[i][1]):
                parsed_disk_map.append(str(id_mapped_disk_map[i][0]))
        else:
            for j in range(id_mapped_disk_map[i][1]):
                parsed_disk_map.append('.')

    print("".join(parsed_disk_map))
    for i in range(len(parsed_disk_map)):
        if parsed_disk_map[i] != '.':
            res += i * int(parsed_disk_map[i])


    print(id_mapped_disk_map)

    return res  

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))