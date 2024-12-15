def solve_star_1(input: list[str]) -> int:
    res = 0

    input = input.copy()
    for line_idx in range(len(input)):
        temp = input[line_idx].split(':')
        target = int(temp[0])
        nums = list(map(int, temp[1].strip(' ').split(' ')))

        results = [nums[0]]

        found = False
        for j in range(1, len(nums)):
            new_results = [] # just to check if target is in each new result
            for result in results:
                
                new_results.append(result + nums[j])
                new_results.append(result * nums[j])
                

                if target in new_results: # look for target
                    found = True
                    break
            
            results = new_results

            if found:
                break
        
        if found:
            res += target


    return res

def solve_star_2(input: list[str]) -> int:
    res = 0

    input = input.copy()
    for line_idx in range(len(input)):
        temp = input[line_idx].split(':')
        target = int(temp[0])
        nums = list(map(int, temp[1].strip(' ').split(' ')))

        results = [nums[0]]

        found = False
        for j in range(1, len(nums)):
            new_results = [] # just to check if target is in each new result
            for result in results:
                
                new_results.append(result + nums[j])
                new_results.append(result * nums[j])
                new_results.append(int(str(result) + str(nums[j])))

                if target in new_results: # look for target
                    found = True
                    break
            
            results = new_results

            if found:
                break
        
        if found:
            res += target


    return res

if __name__ == "__main__":

    with open('2024/input.txt') as f:
        input = [line.strip('\n') for line in f.readlines()]
    
    print(solve_star_1(input))
    print(solve_star_2(input.copy()))