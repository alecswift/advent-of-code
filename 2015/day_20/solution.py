

def find_house(target):
    houses = {}
    for elf in range(1, target // 10):
        for house in range(elf, target // 10, elf):
            if house not in houses:
                houses[house] = elf * 10
            else:
                houses[house] += elf * 10
    for house, presents in houses.items():
        if target <= presents:
            return house

target1 = 36000000
print(find_house(target1))
