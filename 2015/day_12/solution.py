input_file = "2015/day_12/input.txt"
in_file = open(input_file, "r", encoding="utf-8")
with open(input_file, encoding="utf-8") as in_file:
    input_data = in_file.read()

current_num = ""
total = 0
for index, char in enumerate(input_data):
    if char.isdigit() or char == "-":
        current_num += char
    elif input_data[index - 1].isdigit():
        total += int(current_num)
        current_num = ""

print(total)

def search(data, numbers = []):
    if isinstance(data, dict):
        for element in data.values():
            if isinstance(element, dict):
                if "red" in element.values():
                    continue
                search(element, numbers)
            if isinstance(element, list):
                search(element, numbers)
            if isinstance(element, int):
                numbers.append(element)
        return sum(numbers)
    if isinstance(data, list):
        for element in data:
            if isinstance(element, dict):
                if "red" in element.values():
                    continue
                search(element, numbers)
            if isinstance(element, list):
                search(element, numbers)
            if isinstance(element, int):
                numbers.append(element)
        return sum(numbers)

data = eval(input_data)
print(search(data))
