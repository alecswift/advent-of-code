"""Puzzle explanation: https://adventofcode.com/2015/day/22"""


def main():
    min_mana_spent = MinManaSpent()
    min_mana_spent_2 = MinManaSpent()
    effects = (None, None, None)
    print(fight_sim(50, 0, 500, 58, effects, 0, min_mana_spent))
    print(fight_sim(50, 0, 500, 58, effects, 0, min_mana_spent_2, False))


class MinManaSpent:
    def __init__(self, min_mana_spent=None):
        self.min_mana_spent = min_mana_spent


def fight_sim(
    wizhp, armor, mana, bosshp, effects, mana_spent, min_inst=None, part_1=True
):
    # can I get the names of wizard class methods another way
    # rather than hardcoding?
    wizard_moves = [
        ("magic_missile", 53),
        ("drain", 73),
        ("shield", 113),
        ("poison", 173),
        ("recharge", 229),
    ]
    shield, poison, recharge = effects
    # currently simulating 1 fight with random moves, will iterate recursively over paths later
    for move, mana_cost in wizard_moves:
        shield_cp, poison_cp, recharge_cp = shield, poison, recharge
        cp_wizhp, cp_armor, cp_mana, cp_boss_hp, cp_mana_spent = (
            wizhp,
            armor,
            mana,
            bosshp,
            mana_spent,
        )
        # wiz turn
        if not part_1:
            cp_wizhp -= 1
            if cp_wizhp <= 0:
                continue

        shield_cp, cp_armor = shield_effect(shield_cp, cp_armor)
        poison_cp, cp_boss_hp = poison_effect(poison_cp, cp_boss_hp)
        recharge_cp, cp_mana = recharge_effect(recharge_cp, cp_mana)

        if cp_mana < mana_cost:
            continue

        if move == "magic_missile":
            cp_boss_hp -= 4
            cp_mana -= mana_cost
            cp_mana_spent += mana_cost
        elif move == "drain":
            cp_boss_hp -= 2
            cp_wizhp += 2
            cp_mana -= mana_cost
            cp_mana_spent += mana_cost
        elif move == "shield":
            if shield_cp is not None:
                continue
            cp_armor += 7
            shield_cp = 6
            cp_mana -= mana_cost
            cp_mana_spent += mana_cost
        elif move == "poison":
            if poison_cp is not None:
                continue
            poison_cp = 6
            cp_mana -= mana_cost
            cp_mana_spent += mana_cost
        elif move == "recharge":
            if recharge_cp is not None:
                continue
            recharge_cp = 5
            cp_mana -= mana_cost
            cp_mana_spent += mana_cost

        if (
            min_inst.min_mana_spent is not None
            and min_inst.min_mana_spent <= cp_mana_spent
        ):
            continue

        # boss turn
        shield_cp, cp_armor = shield_effect(shield_cp, cp_armor)
        poison_cp, cp_boss_hp = poison_effect(poison_cp, cp_boss_hp)
        recharge_cp, cp_mana = recharge_effect(recharge_cp, cp_mana)

        if cp_boss_hp <= 0:
            if min_inst.min_mana_spent is None:
                min_inst.min_mana_spent = cp_mana_spent
            elif cp_mana_spent < min_inst.min_mana_spent:
                min_inst.min_mana_spent = cp_mana_spent
            return min_inst.min_mana_spent

        if 9 <= cp_armor:
            cp_wizhp -= 1
        else:
            cp_wizhp -= 9 - cp_armor

        if cp_wizhp <= 0:
            continue

        cp_effects = (shield_cp, poison_cp, recharge_cp)
        fight_sim(
            cp_wizhp,
            cp_armor,
            cp_mana,
            cp_boss_hp,
            cp_effects,
            cp_mana_spent,
            min_inst,
            part_1,
        )

    return min_inst.min_mana_spent


def shield_effect(shield_cp, cp_armor):
    if shield_cp is not None:
        shield_cp -= 1
        if shield_cp == 0:
            cp_armor = 0
            shield_cp = None
    return shield_cp, cp_armor


def poison_effect(poison_cp, cp_boss_hp):
    if poison_cp is not None:
        cp_boss_hp -= 3
        poison_cp -= 1
        if poison_cp == 0:
            poison_cp = None
    return poison_cp, cp_boss_hp


def recharge_effect(recharge_cp, cp_mana):
    if recharge_cp is not None:
        cp_mana += 101
        recharge_cp -= 1
        if recharge_cp == 0:
            recharge_cp = None
    return recharge_cp, cp_mana


if __name__ == "__main__":
    main()
