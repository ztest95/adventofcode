def solve_star_1(input: list[str]) -> int:
    # two pointer solution
    # when an empty block is found, swap it with the furthest non-empty block

    res = 0

    disk_map = input[0]

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
    
    # calculating results
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

    # parsing disk map
    # this part is changed from part 1 solution
    id_mapped_disk_map = []
    id = 0
    for i in range(len(disk_map)):
        val = int(disk_map[i])
        if i % 2 == 0:
            id_mapped_disk_map.append((id, val))
            id += 1
        else:
            id_mapped_disk_map.append((None, val))
            

    i = 0
    l = len(id_mapped_disk_map)
    # we update i and l every iteration because we are messing with list num
    while i < l: 
        if id_mapped_disk_map[i][0] == None:
            filled = False
            j = len(id_mapped_disk_map) - 1
            while not filled and j > i:
                # if i its not an empty block
                if id_mapped_disk_map[j][0] != None and id_mapped_disk_map[j][1] > 0:
                    # sourrce block size is equal to target block size
                    if id_mapped_disk_map[j][1] == id_mapped_disk_map[i][1]:
                        # just swap
                        id_mapped_disk_map[i], id_mapped_disk_map[j] = id_mapped_disk_map[j], id_mapped_disk_map[i]
                        filled = True

                    # if source block is bigger than the target block (ex. block "..." being replaced by 99)
                    elif id_mapped_disk_map[j][1] < id_mapped_disk_map[i][1]:
                        # create temp vars
                        i_temp = (id_mapped_disk_map[i][0], id_mapped_disk_map[i][1])
                        j_temp = (id_mapped_disk_map[j][0], id_mapped_disk_map[j][1])
                        # add new block in front of empty
                        id_mapped_disk_map.insert(i, (j_temp[0], j_temp[1]))
                        # subtract count of empty block
                        id_mapped_disk_map[i+1] = (None, i_temp[1] - j_temp[1]) 
                        # empty the source block
                        id_mapped_disk_map[j+1] = (None, j_temp[1])
                        
                        filled = True
                j -= 1 # move to the left
        i += 1
        l = len(id_mapped_disk_map)

    # parsing the sorted disk map
    parsed_disk_map = []
    for i in range(len(id_mapped_disk_map)):
        if id_mapped_disk_map[i][0] != None:
            for j in range(id_mapped_disk_map[i][1]):
                parsed_disk_map.append(str(id_mapped_disk_map[i][0]))
        else:
            for j in range(id_mapped_disk_map[i][1]):
                parsed_disk_map.append('.')

    # calcuating the result
    for i in range(len(parsed_disk_map)):
        if parsed_disk_map[i] != '.':
            res += i * int(parsed_disk_map[i])


    return res  

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))