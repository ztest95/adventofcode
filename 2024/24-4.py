import re


def solve_star_1(input: list[str]) -> int:
    res = 0

    # Counting Horizontal and Vertical "XMAS"

    input = input.copy()
    # COUNT ALL HORIZONTAL -> RIGHTWARD
    for row_idx in range(len(input)):
        count = re.findall(r'XMAS', input[row_idx])
        res += len(count)

    # Reverse Horizontal and COUNT ALL HORIZONTAL -> LEFTWARD   
    reversed_input = [line[::-1] for line in input] # create a reversed list that will be used later
    for row_idx in range(len(input)):
        count = re.findall(r'XMAS', reversed_input[row_idx])
        res += len(count)

    # Rotate list, making vertical to horizontal
    shifted_list = []
    cols = len(input[0])
    rows = len(input)

    # Convert List to Vertical
    shifted_list = [''.join([input[j][i] for j in range(rows)]) for i in range(cols)]

    # Count all 'VERTICAL', 'UPWARD' and 'DOWNWARD'
    for row_idx in range(len(shifted_list)):
        count_right = re.findall(r'XMAS', shifted_list[row_idx])
        count_left = re.findall(r'XMAS', shifted_list[row_idx][::-1])
        res += len(count_right) + len(count_left)

    # Counting Diagonal "XMAS"

    # Creating Diagonal List
    
    # Visit each element in the list and append to the diagonal list
    # ex.
    # 1, 3, 6
    # 2, 5, 8 
    # 4, 7, 9

    cols = len(input[0])
    rows = len(input)

    diagonal_list = [ [] for i in range(rows + cols - 1) ]
    for y in range(rows):
        for x in range(cols):
            diagonal_list[y+x].append(input[y][x])

    # Convert List to String
    diagonal_list = [''.join(diagonal_list[i]) for i in range(len(diagonal_list))]

    # Count all 'DIAGONAL', 'BOTTOM LEFT to TOP RIGHT' and 'TOP RIGHT to BOTTOM LEFT'
    for row_idx in range(len(diagonal_list)):
        count_right = re.findall(r'XMAS', diagonal_list[row_idx])
        count_left = re.findall(r'XMAS', diagonal_list[row_idx][::-1])
        res += len(count_right) + len(count_left)
    
    # Creating the other Diagonal List
    
    # Visit each element in the list and append to the diagonal list
    # ex.
    # 6, 3, 1
    # 8, 5, 2 
    # 9, 7,4

    diagonal_list_2 = [ [] for i in range(rows + cols - 1) ]
    for x in range(rows):
        for i in range(cols):
            char = reversed_input[x][i] # use the reversed list
            diagonal_list_2[x+i].append(char)
    
    diagonal_list_2 = [''.join(diagonal_list_2[i]) for i in range(len(diagonal_list_2))]

    # Count all 'DIAGONAL', 'BOTTOM RIGHT to TOP LEFT' and 'TOP LEFT to BOTTOM RIGHT'
    for row_idx in range(len(diagonal_list_2)):
        count_right = re.findall(r'XMAS', diagonal_list_2[row_idx])
        count_left = re.findall(r'XMAS', diagonal_list_2[row_idx][::-1])
        res += len(count_right) + len(count_left)

    return res

def solve_star_2(input: list[str]) -> int:
    res = 0

    for i, current_line in enumerate(input):

        # check every "A"
        for a in range(len(current_line)):
            # check if A is not at the edge
            if current_line[a] == 'A' and (a != 0 and a != len(current_line.strip('\n'))-1) and (i != 0 and i < len(input)-1):
                around_1 = input[i-1][a-1] + 'A' + input[i+1][a+1]
                around_2 = input[i-1][a+1] + 'A' + input[i+1][a-1]
                # check "X-MAS"
                if around_1 in ('MAS', 'SAM') and around_2 in ('MAS', 'SAM'):
                    res += 1
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))

# References:
# Star 2
# AoC 2023/day/3 
