

def find_house(target):
    houses = {}
    for elf in range(1, target // 11):
        for house in range(elf, 51 * elf, elf):
            if house not in houses:
                houses[house] = elf * 11
            else:
                houses[house] += elf * 11
        if target <= houses[elf]:
            return elf
        del houses[elf]

target1 = 36000000
print(find_house(target1))
