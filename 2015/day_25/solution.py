"""Puzzle explanation: https://adventofcode.com/2015/day/25"""

def main():
    code_num = find_code_num(3029, 2947)
    code = find_code(code_num)
    print(code)

def find_code_num(col_num, row_num):
    code_num = 1
    pos = 2
    while pos <= col_num:
        code_num = pos**2 - code_num
        pos += 1

    for num in range(row_num - 1):
        code_num += col_num + num

    return code_num

def find_code(code_num):
    current_code = 20151125
    for _ in range(code_num - 1):
        current_code *= 252533
        current_code %= 33554393
    return current_code

if __name__ == "__main__":
    main()
