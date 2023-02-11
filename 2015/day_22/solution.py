"""Puzzle explanation: https://adventofcode.com/2015/day/22"""

def main():
    min_mana_spent_my_input = MinManaSpent()
    min_mana_spent_my_input_2 = MinManaSpent()
    print(rec_fight_simulator(50, 0, 500, 58, (None, None, None), 0, min_mana_spent_my_input))
    print(rec_fight_simulator(50, 0, 500, 58, (None, None, None), 0, min_mana_spent_my_input_2, False))

class MinManaSpent:

    def __init__(self, min_mana_spent=None):
        self.min_mana_spent = min_mana_spent

def rec_fight_simulator(wizhp, wizarmour, mana, bosshp, visited, mana_spent, min_inst=None, part_1=True):
    # can I get the names of wizard class methods another way
    # rather than hardcoding?
    wizard_moves = [
        ("magic_missile", 53),
        ("drain", 73),
        ("shield", 113),
        ("poison", 173),
        ("recharge", 229)
    ]
    shield_visited, poison_visited, recharge_visited = visited
    # currently simulating 1 fight with random moves, will iterate recursively over paths later
    for move, mana_cost in wizard_moves:
        shield_visited_temp, poison_visited_temp, recharge_visited_temp = shield_visited, poison_visited, recharge_visited
        temp_wizhp, temp_wizarmour, temp_mana, temp_boss_hp, temp_mana_spent = wizhp, wizarmour, mana, bosshp, mana_spent
        # wiz turn
        if not part_1:
            temp_wizhp -= 1
            if temp_wizhp <= 0:
                continue

        shield_visited_temp, temp_wizarmour = shield_effect(shield_visited_temp, temp_wizarmour)
        poison_visited_temp, temp_boss_hp = poison_effect(poison_visited_temp, temp_boss_hp)
        recharge_visited_temp, temp_mana = recharge_effect(recharge_visited_temp, temp_mana)

        if temp_mana < mana_cost:
            continue

        if move == "magic_missile":
            temp_boss_hp -= 4
            temp_mana -= mana_cost
            temp_mana_spent += mana_cost
        elif move == "drain":
            temp_boss_hp -= 2
            temp_wizhp += 2
            temp_mana -= mana_cost
            temp_mana_spent += mana_cost
        elif move == "shield":
            if shield_visited_temp is not None:
                continue
            temp_wizarmour += 7
            shield_visited_temp = 6
            temp_mana -= mana_cost
            temp_mana_spent += mana_cost
        elif move == "poison":
            if poison_visited_temp is not None:
                continue
            poison_visited_temp = 6
            temp_mana -= mana_cost
            temp_mana_spent += mana_cost
        elif move == "recharge":
            if recharge_visited_temp is not None:
                continue
            recharge_visited_temp = 5
            temp_mana -= mana_cost
            temp_mana_spent += mana_cost

        if min_inst.min_mana_spent is not None and min_inst.min_mana_spent <= temp_mana_spent:
            continue


        # boss turn
        shield_visited_temp, temp_wizarmour = shield_effect(shield_visited_temp, temp_wizarmour)
        poison_visited_temp, temp_boss_hp = poison_effect(poison_visited_temp, temp_boss_hp)
        recharge_visited_temp, temp_mana = recharge_effect(recharge_visited_temp, temp_mana)
        if recharge_visited_temp is not None:
            temp_mana += 101
            recharge_visited_temp -= 1
            if recharge_visited_temp == 0:
                recharge_visited_temp = None

        if temp_boss_hp <= 0:
            if min_inst.min_mana_spent is None:
                min_inst.min_mana_spent = temp_mana_spent
            elif temp_mana_spent < min_inst.min_mana_spent:
                min_inst.min_mana_spent = temp_mana_spent
            return min_inst.min_mana_spent

        if 9 <= temp_wizarmour:
            temp_wizhp -= 1
        else:
            temp_wizhp -= (9 - temp_wizarmour)

        if temp_wizhp <= 0:
            continue

        temp_visited = (shield_visited_temp, poison_visited_temp, recharge_visited_temp)
        rec_fight_simulator(temp_wizhp, temp_wizarmour, temp_mana, temp_boss_hp, temp_visited, temp_mana_spent, min_inst, part_1)

    return min_inst.min_mana_spent

def shield_effect(shield_visited_temp, temp_wizarmour):
    if shield_visited_temp is not None:
        shield_visited_temp -= 1
        if shield_visited_temp == 0:
            temp_wizarmour = 0
            shield_visited_temp = None
    return shield_visited_temp, temp_wizarmour

def poison_effect(poison_visited_temp, temp_boss_hp):
    if poison_visited_temp is not None:
        temp_boss_hp -= 3
        poison_visited_temp -= 1
        if poison_visited_temp == 0:
            poison_visited_temp = None
    return poison_visited_temp, temp_boss_hp

def recharge_effect(recharge_visited_temp, temp_mana):
    if recharge_visited_temp is not None:
            temp_mana += 101
            recharge_visited_temp -= 1
            if recharge_visited_temp == 0:
                recharge_visited_temp = None
    return recharge_visited_temp, temp_mana


if __name__ == "__main__":
    main()
