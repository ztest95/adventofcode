
def solve_star_1(input: list[str]) -> int:

    lst = [] * len(input)

    safe_count = 0
    for line_index in range(len(input)):
        temp = list(map(int, input[line_index].strip("\n").split(" ")))

        asc = temp[0] < temp[1]

        prev = temp[0]
        safe = True # initialize true

        if asc: #Ascending, check if item is greater than previous
            for i in range(1, len(temp)):
                a = temp[i] - prev
                if a > 3 or a < 1:
                    safe = False
                    break
                prev = temp[i]

        else: # Descending, check if item is smaller than previous
            for i in range(1, len(temp)):
                a = prev - temp[i]
                if a > 3 or a < 1:
                    safe = False
                    break
                prev = temp[i]

        if safe:
            safe_count += 1

    return safe_count


def solve_star_2(input: list[str]) -> int:
    lst = [] * len(input)

    safe_count = 0
    for line_index in range(len(input)):
        temp = list(map(int, input[line_index].strip("\n").split(" ")))

        asc = temp[0] < temp[1]

        prev = temp[0]
        safe = True # initialize true
        
        if asc: #Ascending, check if item is greater than previous
            for i in range(1, len(temp)):
                a = temp[i] - prev
                if a > 3 or a < 1:
                    safe = False
                    break
                prev = temp[i]

        else: # Descending, check if item is smaller than previous
            for i in range(1, len(temp)):
                a = prev - temp[i]
                if a > 3 or a < 1:
                    safe = False
                    break
                prev = temp[i]

        if not safe:
            ssafe = 0
            for i in range(len(temp)):
                temp_2 = temp.copy()
                temp_2.pop(i)

                asc = temp_2[0] < temp_2[1]

                prev = temp_2[0]
                safe = True # initialize true
                
                if asc: #Ascending, check if item is greater than previous
                    for i in range(1, len(temp_2)):
                        a = temp_2[i] - prev
                        if a > 3 or a < 1:
                            safe = False
                            break
                        prev = temp_2[i]

                else: # Descending, check if item is smaller than previous
                    for i in range(1, len(temp_2)):
                        a = prev - temp_2[i]
                        if a > 3 or a < 1:
                            safe = False
                            break
                        prev = temp_2[i]

                if safe:
                    break

        if safe:
            safe_count += 1

    return safe_count

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line for line in f.readlines()]

    print(solve_star_1(input))
    print(solve_star_2(input))
