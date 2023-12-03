    
def check_lastline_for_digits(indx: int, line) -> int:
    index = indx - 1 # index starts at top left corner of index of symbol
    line_sum = 0
    last_line = line
    # Top Left Corner Index
    if last_line[index].isdigit():
        # Check for digit in front
        digit_strings = '' 
        
        k = 0
        while last_line[index-k].isdigit():
            digit_strings = last_line[index-k] + digit_strings
            k += 1
        
        last_line = list(last_line)
        last_line[index-k:index+1] = ['.' for i in range(k+1)]
        last_line = ''.join(last_line)

        k = 0
        while last_line[index+k].isdigit():
            digit_strings = digit_strings + last_line[index+k]
            k += 1

        print(digit_strings)
        line_sum = int(digit_strings) + line_sum

        last_line = list(last_line)
        last_line[index-k:index+1] = ['.' for i in range(k+1)]
        last_line = ''.join(last_line)

        digit_strings.strip('.').split('.')
        for i in digit_strings:
            line_sum += int(i)

    index += 1
    # Top Index

    if last_line[index].isdigit(): 
        digit_strings = ''

        k = 0
        while last_line[index+k].isdigit():
            digit_strings = digit_strings + last_line[index+k]
            k += 1
        
        line_sum = int(digit_strings) + line_sum

        last_line = list(last_line)
        last_line[index] = '.'
        last_line = ''.join(last_line)


    index += 1

    # Top Right Index
    if last_line[index].isdigit():
        digit_strings = ''

        k = 0
        while last_line[index+k].isdigit():
            digit_strings = digit_strings + last_line[index+k]
            k += 1

        line_sum = int(digit_strings) + line_sum

        last_line = list(last_line)
        last_line[index:index+k] = ['.' for i in range(k)]
        last_line = ''.join(last_line)

    return last_line
            
if __name__ == "__main__":

    arrWords = []
    with open("day-3/q.txt") as f:
        for line in f.readlines():
            arrWords.append(line)
    
    
    symbols = ['*', '-', '$', '@', '=', '#', '+', '/', '%', '&']

    q = len(arrWords[0])
    sum = 0
    

    arrWords = arrWords[:3]

    # for x in arrWords:
    #     print(x)

    last_line = '.' * q
    for i in range(len(arrWords)):
        current_line = arrWords[i]

        for j in range(q):
            if current_line[j] in symbols:
                # scans last line for digits
                # print(current_line[j], j)
                last_line = check_lastline_for_digits(j, last_line)
                arrWords[i-1] = last_line

        last_line = current_line

    for x in arrWords:
        print(x)
        
    print(sum)