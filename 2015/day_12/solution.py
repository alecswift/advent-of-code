"""Puzzle Explanation: https://adventofcode.com/2015/day/12"""


def main():
    input_file = "2015/day_12/input.txt"
    in_file = open(input_file, "r", encoding="utf-8")
    with open(input_file, encoding="utf-8") as in_file:
        input_data = in_file.read()
    part_1 = add_all_numbers(input_data)
    print(f"The total sum of all numbers is: {part_1}")

    data = eval(input_data)
    part_2 = search_nested_data(data)
    print(f"The sum of all numbers with 'red' not in the same object is: {part_2}")


def add_all_numbers(input_data):
    current_num = ""
    total = 0
    for index, char in enumerate(input_data):
        if char.isdigit() or char == "-":
            current_num += char
        elif input_data[index - 1].isdigit():
            total += int(current_num)
            current_num = ""
    return total


def search_nested_data(data, numbers=[]):
    if isinstance(data, dict):
        for element in data.values():
            check_element(element, numbers)
    if isinstance(data, list):
        for element in data:
            check_element(element, numbers)
    return sum(numbers)


def check_element(element, numbers):
    if isinstance(element, dict):
        if "red" in element.values():
            return None
        search_nested_data(element, numbers)
    if isinstance(element, list):
        search_nested_data(element, numbers)
    if isinstance(element, int):
        numbers.append(element)


if __name__ == "__main__":
    main()
