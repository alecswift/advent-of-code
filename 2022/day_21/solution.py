from re import findall


def parse(input_file):
    in_file = open(input_file, 'r', encoding = 'utf-8')
    with open(input_file, encoding = 'utf-8') as in_file:
        input_data = in_file.read()
    monkeys = findall(r'(\w+): (.+)', input_data)
    monkey_dict = {}
    for name, job in monkeys:
        if job.isdigit():
            monkey_dict[name] = int(job)
        else:
            monkey_dict[name] = findall(r'([a-z]+) (.) ([a-z]+)', job)[0]
    return monkey_dict

print(parse('2022/day_21/input.txt'))
