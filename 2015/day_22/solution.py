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


def fight_sim(whp, armor, mana, bhp, effects, mana_spent, min_inst, part_1=True):
    wiz_moves = [
        ("magic_missile", 53),
        ("drain", 73),
        ("shield", 113),
        ("poison", 173),
        ("recharge", 229),
    ]
    shield, poison, recharge = effects

    for move, mana_cost in wiz_moves:
        shield_cp, poison_cp, recharge_cp = shield, poison, recharge
        cp_whp, cp_armor, cp_mana, cp_bhp, cp_mana_spent = (
            whp,
            armor,
            mana,
            bhp,
            mana_spent,
        )
        # wizard turn
        if not part_1:
            cp_whp -= 1
            if cp_whp <= 0:
                continue

        shield_cp, cp_armor = shield_effect(shield_cp, cp_armor)
        poison_cp, cp_bhp = poison_effect(poison_cp, cp_bhp)
        recharge_cp, cp_mana = recharge_effect(recharge_cp, cp_mana)

        not_enough_mana_for_move = cp_mana < mana_cost
        if not_enough_mana_for_move:
            continue

        match move:
            case "magic_missile":
                cp_bhp -= 4
            case "drain":
                cp_bhp -= 2
                cp_whp += 2
            case "shield":
                if shield_cp is not None:
                    continue
                cp_armor += 7
                shield_cp = 6
            case "poison":
                if poison_cp is not None:
                    continue
                poison_cp = 6
            case "recharge":
                if recharge_cp is not None:
                    continue
                recharge_cp = 5

        cp_mana -= mana_cost
        cp_mana_spent += mana_cost

        min_initialized = min_inst.min_mana_spent is not None
        if min_initialized and min_inst.min_mana_spent <= cp_mana_spent:
            continue

        # boss turn
        shield_cp, cp_armor = shield_effect(shield_cp, cp_armor)
        poison_cp, cp_bhp = poison_effect(poison_cp, cp_bhp)
        recharge_cp, cp_mana = recharge_effect(recharge_cp, cp_mana)

        if cp_bhp <= 0:
            if not min_initialized:
                min_inst.min_mana_spent = cp_mana_spent
            elif cp_mana_spent < min_inst.min_mana_spent:
                min_inst.min_mana_spent = cp_mana_spent
            return min_inst.min_mana_spent

        if 9 <= cp_armor:
            cp_whp -= 1
        else:
            cp_whp -= 9 - cp_armor

        if cp_whp <= 0:
            continue

        cp_effects = (shield_cp, poison_cp, recharge_cp)
        fight_sim(
            cp_whp,
            cp_armor,
            cp_mana,
            cp_bhp,
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


def poison_effect(poison_cp, cp_bhp):
    if poison_cp is not None:
        cp_bhp -= 3
        poison_cp -= 1
        if poison_cp == 0:
            poison_cp = None
    return poison_cp, cp_bhp


def recharge_effect(recharge_cp, cp_mana):
    if recharge_cp is not None:
        cp_mana += 101
        recharge_cp -= 1
        if recharge_cp == 0:
            recharge_cp = None
    return recharge_cp, cp_mana


if __name__ == "__main__":
    main()
