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
    
    for i in range(len(sorted_disk_map)):
        if sorted_disk_map[i] != '.':
            res += i * int(sorted_disk_map[i])

    return res  

def solve_star_2(input: list[str]) -> int:
    res = 0

    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))