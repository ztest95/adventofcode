    
def check_line_for_digits(symbol_index: int, line) -> (str, int):
    symbol_numbers = 0
    digit_strings = ''

    # Scan Left Digits
    l = 1
    while line[symbol_index-l].isdigit():
        l += 1

    # Scan Right Digits
    r = 1
    while line[symbol_index+r].isdigit():
        r += 1

    digit_strings = line[symbol_index-l+1:symbol_index+r]

    if line[symbol_index].isdigit():
        # if middle index is digit
        # digit_strings = digit_strings.replace('.', last_line[symbol_index])
        symbol_numbers = [int(digit_strings.replace('.', line[symbol_index]))]
    else:
        # if middle index is not a digit
        symbol_numbers = digit_strings.split(".")
        symbol_numbers = [int(i) for i in symbol_numbers if i != '']

    # Convert Digits to '.'    
    new_line = list(line)
    new_line[symbol_index-l+1:symbol_index+r] = ['.' for i in range(l+r-1)]
    new_line = ''.join(new_line)

    return new_line , symbol_numbers

def check_currentline_for_digits(symbol_index, line):

    symbol_numbers = 0
    digit_strings = ''

    # Scan Left Digits
    l = 1
    while line[symbol_index-l].isdigit():
        l += 1

    # Scan Right Digits
    r = 1
    while line[symbol_index+r].isdigit():
        r += 1

    digit_strings = line[symbol_index-l+1:symbol_index+r]

    # Middle index will always be a digit
    symbol_numbers = digit_strings.split(line[symbol_index])
    symbol_numbers = [int(i) for i in symbol_numbers if i != '']

    # Convert Digits to '.'    
    new_line = list(line)
    new_line[symbol_index-l+1:symbol_index+r] = ['.' for i in range(l+r-1)]
    new_line = ''.join(new_line)

    return new_line , symbol_numbers

if __name__ == "__main__":

    symbols = ['*', '-', '$', '@', '=', '#', '+', '/', '%', '&']

    sums = 0

    new_lines = []

    with open("day-3/q.txt") as f:
        lines = f.readlines()
        new_lines = lines

        for i, current_line in enumerate(lines):

            if i < len(lines) - 1:
                next_line = lines[i+1]
            else:
                next_line = '.'

            # Don't need this, but this makes the code work incase there is symbol on first line
            if i < 1: 
                last_line = '.' * len(current_line)

            for j in range(len(current_line)):

                if current_line[j] in symbols: 
            
                    before_currline = check_line_for_digits(j, last_line) 
                    the_currline = check_currentline_for_digits(j, current_line)
                    after_currline = check_line_for_digits(j, next_line)
                    # new_line: str, symbol_numbers: list[int]

                    # Append the coordinates of the symbol to the key
                    # that corresponds to the number of digits beside them in each line
                    # Their key can not exceed 2 yet

                    sums += sum(before_currline[1]) + sum(the_currline[1]) + sum(after_currline[1])

            last_line = current_line

            i += 1

    print(sums)

## How the solution works
# 1. Scan each line for symbols
# 2. If symbol is found, scan around the symbol
#       starting from top (before the line where symbol is at)
#       current line (line where symbol is at)
#       bottom (after the line where symbol is at)
# 3. If digits are found, convert them to '.' and put the digits in a list
# Each symbol will have 3 function calls for top digits, current digits, bottom digits
