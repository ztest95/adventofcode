    
def check_lastline_for_digits(indx: int, line) -> int:
    index = indx # index starts at top left corner of index of symbol
    line_sum = 0
    last_line = line
    # Top Left Corner Index
    digit_strings = '.'


    l = 1
    while last_line[index-l].isdigit():
        digit_strings = last_line[index-l] + digit_strings
        l += 1

    line_sum = line_sum if (digit_strings == '.') else line_sum + int(digit_strings[0:-1])
    digit_strings1 = digit_strings
    first_len = len(digit_strings)
    r = 1
    while last_line[index+r].isdigit():
        digit_strings = digit_strings + last_line[index+r]
        r += 1
    second_len = len(digit_strings)
    line_sum = line_sum if (first_len == second_len) else line_sum + int(digit_strings.replace(digit_strings1, ''))

    if last_line[index].isdigit():
        digit_strings = digit_strings.replace('.', last_line[index])
        last_line = list(last_line)
        last_line[index] = '.'
        last_line = ''.join(last_line)
        line_sum = digit_strings.strip('.')
        line_sum = int(line_sum)
   
    digit_strings = digit_strings.strip('.')

    last_line = list(last_line)
    last_line[index-l:index] = ['.' for i in range(l)]
    last_line[index+1:index+r+1] = ['.' for i in range(r)]
    last_line = ''.join(last_line)

    # # Top Index

    # if last_line[index].isdigit(): 
    #     digit_strings = ''

    #     k = 0
    #     while last_line[index+k].isdigit():
    #         digit_strings = digit_strings + last_line[index+k]
    #         k += 1
        
    #     line_sum = int(digit_strings) + line_sum

    #     last_line = list(last_line)
    #     last_line[index] = '.'
    #     last_line = ''.join(last_line)

    # index += 1

    # # Top Right Index
    # if last_line[index].isdigit():
    #     digit_strings = ''

    #     k = 0
    #     while last_line[index+k].isdigit():
    #         digit_strings = digit_strings + last_line[index+k]
    #         k += 1

    #     line_sum = int(digit_strings) + line_sum

    #     last_line = list(last_line)
    #     last_line[index:index+k] = ['.' for i in range(k)]
    #     last_line = ''.join(last_line)

    return last_line , line_sum

def check_currentline_for_digits(indx, line):
    index = indx
    line_sum = 0
    current_line = line
    # Left Index
    digit_strings = ''
    k = 1
    while current_line[index-k].isdigit():
        digit_strings = current_line[index-k] + digit_strings
        k += 1
    
    line_sum = line_sum if (digit_strings == '') else line_sum + int(digit_strings)
 
    current_line = list(current_line)
    current_line[index-k:index] = ['.' for i in range(k)]
    current_line = ''.join(current_line)

    digit_strings = ''
    k = 1
    while current_line[index+k].isdigit():
        digit_strings = digit_strings + current_line[index+k]
        k += 1
    
    line_sum = line_sum if (digit_strings == '') else line_sum + int(digit_strings)

    current_line = list(current_line)
    current_line[index+1:index+k+1] = ['.' for i in range(k)]
    current_line = ''.join(current_line)

    return current_line , line_sum
            
if __name__ == "__main__":

    arrWords = []
    with open("day-3/q.txt") as f:
        for line in f.readlines():
            arrWords.append(line)
    
    
    symbols = ['*', '-', '$', '@', '=', '#', '+', '/', '%', '&']

    q = len(arrWords[0])
    sum = 0
    


    last_line = '.' * q
    for i in range(len(arrWords)):
        current_line = arrWords[i]
        if i != len(arrWords)-1:
            next_line = arrWords[i+1]
        else:
            next_line = '.'
        for j in range(len(current_line)):
            if current_line[j] in symbols:
                # scans last line for digits
                tup = check_lastline_for_digits(j, last_line)
                tup2 = check_currentline_for_digits(j, current_line)
                arrWords[i-1] = tup[0]
                arrWords[i] = tup2[0]

                sum += tup2[1] + tup[1]
                if i != len(arrWords)-1:
                    tup3 = check_lastline_for_digits(j, next_line)
                    arrWords[i+1] = tup3[0]
                    sum += tup3[1]

        last_line = current_line

    for x in arrWords:
        print(x)
    print(sum)