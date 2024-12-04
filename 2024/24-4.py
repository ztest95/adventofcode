def solve_star_1(input: list[str]) -> int:
    res = 0

    # COUNT ALL HORIZONTAL -> RIGHTWARD
    for row_idx in range(len(input)):
        count = re.findall(r'XMAS', input[row_idx])
        res += len(count)
    # print("Horizontal-Right: ", res)

    # COUNT ALL HORIZONTAL -> LEFTWARD
    reversed_input = [line[::-1] for line in input]
    for row_idx in range(len(input)):
        count = re.findall(r'XMAS', reversed_input[row_idx])
        res += len(count)
    # print("Horizontal-Left: ", res)

    shifted_list = []
    new = input.copy()
    for line_index in range(len(new)):
        new[line_index] = new[line_index].strip('\n')
    
    shifted_list = []
    cols = len(new[0])
    rows = len(new)

    for i in range(cols):
        shifted_list.append(''.join([new[j][i] for j in range(rows)]))

    # Count all VERTICAL 
    for row_idx in range(len(shifted_list)):
        count_right = re.findall(r'XMAS', shifted_list[row_idx])
        count_left = re.findall(r'XMAS', shifted_list[row_idx][::-1])
        res += len(count_right) + len(count_left)
    # print("Vertical: ", res)

    # Convert List to Diagonal

    cols = len(shifted_list[0])
    rows = len(shifted_list)
    diagonal_list = []

    diagonal_list = [ [] for i in range(rows + cols - 1) ]
    for x in range(rows):
        for i in range(cols):
            char = shifted_list[x][i]
            diagonal_list[x+i].append(char)
    
    for i in range(len(diagonal_list)):
        diagonal_list[i] = ''.join(diagonal_list[i])

    # READ DIAGONAL ASCENDING
    for row_idx in range(len(diagonal_list)):
        count_right = re.findall(r'XMAS', diagonal_list[row_idx])
        count_left = re.findall(r'XMAS', diagonal_list[row_idx][::-1])
        res += len(count_right) + len(count_left)
    # print("Bottom Left to Top Right: ", res)
    
    reverse = []
    for i in range(len(shifted_list)):
        reverse.append(shifted_list[i][::-1])
    
    diagonal_list_2 = [ [] for i in range(rows + cols - 1) ]
    for x in range(rows):
        for i in range(cols):
            char = reverse[x][i]
            diagonal_list_2[x+i].append(char)
    
    for i in range(len(diagonal_list_2)):
        diagonal_list_2[i] = ''.join(diagonal_list_2[i])

    for row_idx in range(len(diagonal_list_2)):
        count_right = re.findall(r'XMAS', diagonal_list_2[row_idx])
        count_left = re.findall(r'XMAS', diagonal_list_2[row_idx][::-1])
        res += len(count_right) + len(count_left)
    # print("Bottom Right to Top Left: ", res)

    return res

def solve_star_2(input: list[str]) -> int:
    res = 0

    for i, current_line in enumerate(input):

        for a in range(len(current_line)):
            if current_line[a] == 'A' and (a != 0 and a != len(current_line.strip('\n'))-1) and (i != 0 and i < len(input)-1):
                around_1 = input[i-1][a-1] + 'A' + input[i+1][a+1]
                around_2 = input[i-1][a+1] + 'A' + input[i+1][a-1]
                
                if around_1 in ('MAS', 'SAM') and around_2 in ('MAS', 'SAM'):
                    res += 1
    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))

# References:
# AoC 2023/day/3 
