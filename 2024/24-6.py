def solve_star_1(input: list[str]) -> int:
    # Get index of guard
    # Check the next index where guard is facing
    # increment for every block
    # if wall, turn 90%
    # if index is out of bounds, count
    res = 0

    for i in range(len(input)):
        input[i] = list(input[i])

    i, j = 0, 0

    faces = ['^', '>', 'v', '<']
    faces_set = set(faces) # just to save some time checking if in\
    init_face = 0

    found = False
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] in faces_set:
                # get index of face
                for f_idx in range(len(faces)):
                    if input[i][j] == faces[f_idx]:
                        init_face = f_idx
                        found = True
                        break
                if found:
                    break
        if found:
            break

    blocks = 0
    max_i = len(input)  
    max_j = len(input[0])
    forward = (i, j)
    curr = input[forward[0]][forward[1]]

    if init_face == 0:
        i -= 1
    elif init_face == 1:
        j += 1
    elif init_face == 2:
        i += 1
    elif init_face == 3:
        j -= 1
    forward = (i, j)

    while i < max_i and j < max_j:

        next = input[forward[0]][forward[1]]
        # print('CURR', curr, 'NEXT', next)
        if next != '#': # if not wall
            if next == '.': # if not visited
                blocks += 1 # increment blocks
                input[forward[0]][forward[1]] = 'X'
            
        else: # if wall
            init_face = (init_face + 1) % 4

            if init_face == 0:  
                j += 1
                i -= 1
            elif init_face == 1:
                i += 1
                j += 1
            elif init_face == 2:
                j -= 1
                i += 1
            elif init_face == 3:
                i -= 1
                j -= 1
                
            
            forward = (i, j)
            
            continue

        # put next to curr
        curr = input[forward[0]][forward[1]]
        # update next index
        if init_face == 0:
            i -= 1
        elif init_face == 1:
            j += 1
        elif init_face == 2:
            i += 1
        elif init_face == 3:
            j -= 1
        
        forward = (i, j)

    # for x in input:
    #     print(x)
    return blocks + 1

def solve_star_2(input: list[str]) -> int:
    res = 0
    
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))
