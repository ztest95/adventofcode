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

    for x in input:
        print(''.join(x))
    return blocks + 1

def solve_star_2(input: list[str]) -> int:
    # i want to save the coordinates of all the wall
    # then everytime i encounter a visited block, 
    #       ill save this coordinate, and following coordinate
    #       i will check if the path to the right is visited until the next block
    #       if yes, 
    #               ill turn right, forward, 
    #               and continue the path with my movement rule. 
    #               if i reach a non-visited block, 
    #                      break this (not a loop)
    #               if i reach the same coordinate
    #                       then a wall in the following coordinate creates a loop
    #                       loop + 1
    #       if no
    #               go back to the coordianate i saved
    #
    # do this until im out of bound
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
    # input[i][j] = 'X'
    blocks = 1
    max_i = len(input)  
    max_j = len(input[0])
    curr_idx = (i, j)
    curr = input[i][j] # set starting position to curr
    
    # get the coordinate of faced block
    if init_face == 0:
        i -= 1
    elif init_face == 1:
        j += 1
    elif init_face == 2:
        i += 1
    elif init_face == 3:
        j -= 1
    forward = (i, j) # set forward to the faced block

    loops = 0
    while i < max_i and j < max_j:

        next = input[forward[0]][forward[1]]

        # if current position not visited
        if input[curr_idx[0]][curr_idx[1]] == '.' or input[curr_idx[0]][curr_idx[1]] in faces_set:
            blocks += 1 
            input[curr_idx[0]][curr_idx[1]] = 'X' # mark as visited
        # do nothing if already visited

        elif input[curr_idx[0]][curr_idx[1]] == 'X':
            loop_curr_idx = (curr_idx[0], curr_idx[1])    # save the current index
            loop_face = (init_face + 1) % 4 # change face
            
            loop_i, loop_j = loop_curr_idx
            if loop_face == 0:  
                # loop_j += 1
                loop_i -= 1
            elif loop_face == 1:
                # loop_i += 1
                loop_j += 1
            elif loop_face == 2:
                # loop_j -= 1
                loop_i += 1
            elif loop_face == 3:
                # loop_i -= 1
                loop_j -= 1
            loop_forward = (loop_i, loop_j)
            
            not_a_loop = False
            # After this, guard is temporary rotated
            # Standing at the intersection block, and Next block is the forward block
            while loop_forward != curr_idx and not not_a_loop:
                loop_next = input[loop_forward[0]][loop_forward[1]]
                if loop_next == ".":
                    not_a_loop = True
                    break

                if loop_next == "#":
                    loop_face = (loop_face + 1) % 4 # rorate
                    # get the next block

                    loop_curr_idx = loop_forward

                    if loop_face == 0:  
                        loop_j += 1
                        loop_i -= 1
                    elif loop_face == 1:
                        loop_i += 1
                        loop_j += 1
                    elif loop_face == 2:
                        loop_i += 1
                        loop_j -= 1
                    elif loop_face == 3:
                        loop_i -= 1
                        loop_j -= 1
                    
                    loop_forward = (loop_i, loop_j)
                    continue
                
                loop_curr_idx = loop_forward
                # input[loop_curr_idx[0]][loop_curr_idx[1]] = '|'

                if loop_face == 0:  
                    # loop_j += 1
                    loop_i -= 1
                elif loop_face == 1:
                    # loop_i += 1
                    loop_j += 1
                elif loop_face == 2:
                    # loop_j -= 1
                    loop_i += 1
                elif loop_face == 3:
                    # loop_i -= 1
                    loop_j -= 1

                loop_forward = (loop_i, loop_j)

            if not not_a_loop:
                loops += 1
 

        # Check Next Block
        if next == '#': # if wall
            init_face = (init_face + 1) % 4 # rotate gurad
            # get the next block
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

        # Move to next block
        # put next to curr
        curr_idx = forward
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
        # next will be updated in the next iteration

    for x in input:
        print(''.join(x))
    return loops

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    x = input.copy()
    print(solve_star_1(input))
    print(solve_star_2(x))
