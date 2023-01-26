"""
Convert snafu (a made up number system based on pentary) to decimal
and decimal back to snafu
"""


def parse(input_file):
    """Return the input data with the lines split and reversed"""
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    split_lines = input_data.split("\n")
    return [line[::-1] for line in split_lines]


def decimal_from(snafu):
    """Return a decimal number from a given snafu string"""
    number = 0
    for index, digit in enumerate(snafu):
        if digit.isdigit():
            number += int(digit) * (5**index)
        if digit == "-":
            number += -1 * (5**index)
        if digit == "=":
            number += -2 * (5**index)
    return number


def decode_input_data(input_file):
    """Return the decimal sum of all input numbers"""
    input_data = parse(input_file)
    numbers = []
    for snafu in input_data:
        numbers.append(decimal_from(snafu))
    return sum(numbers)


def snafu_from(decimal):
    """Return a snafu string from a decimal number"""
    penta_array = []
    if decimal == 0:
        return "0"
    while decimal != 0:
        decimal, remainder = divmod(decimal, 5)
        penta_array.insert(0, remainder)
    snafu_array = []
    carry = 0
    for num in range(-1, -len(penta_array) - 3, -1):
        if num < -len(penta_array):
            penta_num = 0 + carry
        else:
            penta_num = penta_array[num] + carry
        carry = 0
        if penta_num < 3:
            snafu_array.insert(0, str(penta_num))
        if penta_num == 3:
            snafu_array.insert(0, "=")
            carry += 1
        if penta_num == 4:
            snafu_array.insert(0, "-")
            carry += 1
        if penta_num == 5:
            snafu_array.insert(0, "0")
            carry += 1
    return "".join(snafu_array)


print(snafu_from(decode_input_data("2022/day_25/input.txt")))
