

def find_house(target):
    houses = {}
    for elf in range(1, target // 25):
        for house in range(elf, target // 25, elf):
            if house not in houses:
                houses[house] = elf * 10
            else:
                houses[house] += elf * 10
        if target <= houses[elf]:
            return elf
        del houses[elf]

target1 = 36000000
print(find_house(target1))
